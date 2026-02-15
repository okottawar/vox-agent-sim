# world/state/agent_state.py

from dataclasses import dataclass
from typing import Tuple
from enums import Orientation


@dataclass
class AgentState:
    """
    Stores agent-specific state.
    Contains no world logic.
    """

    position: Tuple[int, int, int]
    orientation: Orientation
    energy: float

    # Derived Properties
    @property
    def is_alive(self) -> bool:
        return self.energy > 0.0

    # State Updates
    def move_to(self, new_position: Tuple[int, int, int]) -> None:
        self.position = new_position

    def change_energy(self, delta: float) -> None:
        self.energy += delta
