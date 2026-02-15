# world/state/world_state.py

from dataclasses import dataclass
from .voxel_grid import VoxelGrid
from .agent_state import AgentState


@dataclass
class WorldState:
    """
    Authoritative simulation state.

    This is the single source of truth for:
    - voxel grid
    - agent state
    - tick counter
    - version metadata
    """

    voxel_grid: VoxelGrid
    agent_state: AgentState
    tick_id: int
    physics_version: str
    terrain_version: str
    world_seed: int

    # Tick Management
    def increment_tick(self) -> None:
        self.tick_id += 1

    # Snapshot Support
    def snapshot(self) -> dict:
        """
        Returns serializable snapshot of world state.
        Used for logging and replay.
        """
        return {
            "tick_id": self.tick_id,
            "physics_version": self.physics_version,
            "terrain_version": self.terrain_version,
            "world_seed": self.world_seed,
            "agent_position": self.agent_state.position,
            "agent_energy": self.agent_state.energy,
        }
