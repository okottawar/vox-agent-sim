# world/config.py

from dataclasses import dataclass

# World 
@dataclass(frozen=True)
class WorldConfig:
    size: int = 256
    seed: int = 42

    physics_version: str = "v1.0.0"
    terrain_version: str = "v1.0.0"
    observation_version: str = "v1.0.0"
    logging_version: str = "v1.0.0"

# Terrain 
@dataclass(frozen=True)
class TerrainConfig:
    size: int = 256
    seed: int = 42

    max_height: int = 64
    water_level: int = 32
    energy_probability: float = 0.005

# Physics
@dataclass(frozen=True)
class PhysicsConfig:
    gravity_enabled: bool = True

    energy_cost_grass: float = 0.1
    energy_cost_rock: float = 0.2
    energy_cost_water: float = 0.4

# Observation
@dataclass(frozen=True)
class ObservationConfig:
    window_radius: int = 3
