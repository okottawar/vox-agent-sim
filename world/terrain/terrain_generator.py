# world/terrain/terrain_generator.py

import numpy as np

from world.config import TerrainConfig
from world.enums import VoxelType
from world.state.voxel_grid import VoxelGrid


class TerrainGenerator:
    """
    Generates deterministic voxel terrain based on TerrainConfig.
    Fully compliant with system enums and versioning.
    """

    def __init__(self, config: TerrainConfig):
        self.config = config
        self.rng = np.random.default_rng(config.seed)

    # Public API
    def generate(self) -> VoxelGrid:
        grid = VoxelGrid(self.config.size)

        heightmap = self._generate_heightmap()

        size = self.config.size

        for x in range(size):
            for z in range(size):

                height = heightmap[x, z]

                # Fill rock below surface
                if height > 0:
                    grid.grid[x, 0:height, z] = VoxelType.ROCK

                # Surface grass
                if height < size:
                    grid.grid[x, height, z] = VoxelType.GRASS

        self._apply_water(grid, heightmap)
        self._scatter_energy_blocks(grid, heightmap)

        return grid

    # Heightmap Generation
    def _generate_heightmap(self) -> np.ndarray:
        """
        Generates smooth heightmap using deterministic noise.
        """

        size = self.config.size
        scale = 32.0  # Adjustable later via config if needed

        x = np.linspace(0, size / scale, size)
        z = np.linspace(0, size / scale, size)
        x_grid, z_grid = np.meshgrid(x, z, indexing="ij")

        noise = self._smooth_noise()

        normalized = (noise - noise.min()) / (noise.max() - noise.min())

        heightmap = (normalized * self.config.max_height).astype(int)

        return heightmap

    def _smooth_noise(self) -> np.ndarray:
        """
        Lightweight deterministic smooth noise.
        Replaceable with real Perlin later without breaking API.
        """

        base = self.rng.random((self.config.size, self.config.size))

        smooth = (
            base +
            np.roll(base, 1, axis=0) +
            np.roll(base, -1, axis=0) +
            np.roll(base, 1, axis=1) +
            np.roll(base, -1, axis=1)
        ) / 5.0

        return smooth


    # Water Placement
    def _apply_water(self, grid: VoxelGrid, heightmap: np.ndarray) -> None:
        water_level = self.config.water_level
        size = self.config.size

        for x in range(size):
            for z in range(size):

                height = heightmap[x, z]

                if height < water_level:
                    grid.grid[x, height + 1:water_level + 1, z] = VoxelType.WATER

    # Energy Block Placement
    def _scatter_energy_blocks(self, grid: VoxelGrid, heightmap: np.ndarray) -> None:
        size = self.config.size
        prob = self.config.energy_probability

        for x in range(size):
            for z in range(size):

                if self.rng.random() < prob:
                    height = heightmap[x, z]

                    if grid.grid[x, height, z] == VoxelType.GRASS:
                        grid.grid[x, height, z] = VoxelType.ENERGY