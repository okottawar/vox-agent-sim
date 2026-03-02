# world/physics/physics_v1.py

from world.enums import VoxelType, ActionType
from world.config import PhysicsConfig
from world.schemas import ActionResult


class PhysicsEngineV1:
    """
    Deterministic discrete physics engine.
    """

    def __init__(self, config: PhysicsConfig):
        self.config = config

    # Movement Resolution
    def resolve_action(self, state, action: ActionType) -> ActionResult:

        if action == ActionType.IDLE:
            return ActionResult(True, 0.0, 0.0, False)

        if action == ActionType.BREAK:
            return self._handle_break(state)

        return self._handle_movement(state, action)


    # Movement Logic
    def _handle_movement(self, state, action):

        current_pos = state.agent_state.position
        target_pos = self._compute_target_position(state, action)

        if not state.voxel_grid.in_bounds(*target_pos):
            return ActionResult(False, 0.0, 0.0, False)

        voxel = state.voxel_grid.get(*target_pos)

        if voxel not in (VoxelType.AIR, VoxelType.WATER):
            return ActionResult(False, 0.0, 0.0, False)

        # Apply energy cost
        cost = self._energy_cost(voxel)

        state.agent_state.move_to(target_pos)
        state.agent_state.change_energy(-cost)

        done = not state.agent_state.is_alive

        return ActionResult(True, 0.0, -cost, done)

    # Break Logic
    def _handle_break(self, state):

        target_pos = self._compute_target_position(state, ActionType.MOVE_FORWARD)

        if not state.voxel_grid.in_bounds(*target_pos):
            return ActionResult(False, 0.0, 0.0, False)

        voxel = state.voxel_grid.get(*target_pos)

        if voxel == VoxelType.AIR:
            return ActionResult(False, 0.0, 0.0, False)

        state.voxel_grid.set(*target_pos, VoxelType.AIR)

        return ActionResult(True, 0.0, 0.0, False)

    # Gravity
    def apply_gravity(self, state):

        if not self.config.gravity_enabled:
            return

        x, y, z = state.agent_state.position

        if y == 0:
            return

        below = state.voxel_grid.get(x, y - 1, z)

        if below == VoxelType.AIR:
            state.agent_state.move_to((x, y - 1, z))

    # Helpers
    def _compute_target_position(self, state, action):

        x, y, z = state.agent_state.position
        orientation = state.agent_state.orientation

        dx, dz = self._direction_vector(orientation, action)

        return (x + dx, y, z + dz)

    def _direction_vector(self, orientation, action):

        # Base forward vectors
        forward = {
            0: (0, -1),   # NORTH
            1: (1, 0),    # EAST
            2: (0, 1),    # SOUTH
            3: (-1, 0),   # WEST
        }

        dx, dz = forward[orientation]

        if action == ActionType.MOVE_FORWARD:
            return dx, dz
        elif action == ActionType.MOVE_BACKWARD:
            return -dx, -dz
        elif action == ActionType.MOVE_LEFT:
            return -dz, dx
        elif action == ActionType.MOVE_RIGHT:
            return dz, -dx

        return 0, 0

    def _energy_cost(self, voxel_type):

        if voxel_type == VoxelType.GRASS:
            return self.config.energy_cost_grass
        elif voxel_type == VoxelType.ROCK:
            return self.config.energy_cost_rock
        elif voxel_type == VoxelType.WATER:
            return self.config.energy_cost_water

        return 0.0