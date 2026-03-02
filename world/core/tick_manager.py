# world/core/tick_manager.py

from world.schemas import Observation


class TickManager:
    """
    Controls deterministic tick execution order.
    """

    def __init__(self, state, physics_engine, action_resolver, observation_config):
        self.state = state
        self.physics = physics_engine
        self.resolver = action_resolver
        self.obs_config = observation_config

    def step(self, action):
        """
        Executes one simulation tick.

        Order:
        1. Resolve action
        2. Apply gravity
        3. Check termination
        4. Increment tick
        5. Build observation
        """

        # 1️⃣ Resolve action
        result = self.resolver.resolve(self.state, action)

        # 2️⃣ Apply gravity
        self.physics.apply_gravity(self.state)

        # 3️⃣ Determine termination
        done = not self.state.agent_state.is_alive
        result.done = done

        # 4️⃣ Increment tick
        self.state.increment_tick()

        # 5️⃣ Build observation
        observation = self._build_observation()

        return observation, result

    def _build_observation(self):

        agent = self.state.agent_state
        radius = self.obs_config.window_radius

        local_window = self.state.voxel_grid.get_local_window(
            agent.position,
            radius
        )

        return Observation(
            local_voxels=local_window,
            energy=agent.energy,
            position=agent.position,
            orientation=agent.orientation
        )