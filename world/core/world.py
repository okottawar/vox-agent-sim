# world/core/world.py

from world.config import (
    WorldConfig,
    TerrainConfig,
    PhysicsConfig,
    ObservationConfig
)

from world.enums import Orientation
from world.state.agent_state import AgentState
from world.state.world_state import WorldState
from world.terrain.terrain_generator import TerrainGenerator
from world.physics.physics_v1 import PhysicsEngineV1
from world.core.action_resolver import ActionResolver
from world.core.tick_manager import TickManager


class World:
    """
    Top-level simulation container.
    """

    def __init__(self, world_config: WorldConfig):

        self.world_config = world_config

        terrain_config = TerrainConfig(
            size=world_config.size,
            seed=world_config.seed
        )

        terrain_generator = TerrainGenerator(terrain_config)
        voxel_grid = terrain_generator.generate()

        spawn_position = self._compute_spawn_position(voxel_grid)
        agent_state = AgentState(
            position=spawn_position,
            orientation=Orientation.NORTH,
            energy=100.0  # initial energy (can move to config later)
        )

        self.state = WorldState(
            voxel_grid=voxel_grid,
            agent_state=agent_state,
            tick_id=0,
            physics_version=world_config.physics_version,
            terrain_version=world_config.terrain_version,
            world_seed=world_config.seed
        )

        physics_config = PhysicsConfig()
        physics_engine = PhysicsEngineV1(physics_config)

        resolver = ActionResolver(physics_engine)

        observation_config = ObservationConfig()

        self.tick_manager = TickManager(
            self.state,
            physics_engine,
            resolver,
            observation_config
        )

    def step(self, action):
        return self.tick_manager.step(action)

    def reset(self):
        """
        Resets world by re-instantiating everything.
        """
        self.__init__(self.world_config)

    def _compute_spawn_position(self, voxel_grid):

        size = voxel_grid.size
        center_x = size // 2
        center_z = size // 2

        # Find highest non-air voxel
        column = voxel_grid.grid[center_x, :, center_z]
        non_air = column.nonzero()[0]

        if len(non_air) == 0:
            return (center_x, 0, center_z)

        surface_y = int(non_air.max())

        return (center_x, surface_y + 1, center_z)