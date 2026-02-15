# world/types.py

from dataclasses import dataclass
from typing import Tuple
import numpy as np

# Core Types
Position = Tuple[int, int, int]

# Observation Type
@dataclass
class Observation:
    local_voxels: np.ndarray  # shape: (7, 7, 7)
    energy: float
    position: Position
    orientation: int

# Action Result
@dataclass
class ActionResult:
    success: bool
    reward: float
    energy_delta: float
    done: bool

# World Snapshot
@dataclass
class WorldSnapshot:
    tick_id: int
    position: Position
    energy: float
    physics_version: str
    terrain_version: str
    world_seed: int