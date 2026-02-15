# world/state/voxel_grid.py

import numpy as np


class VoxelGrid:
    """
    Dense 3D voxel grid.

    Stores voxel IDs as uint8 in a fixed-size cube.
    Responsible ONLY for data storage and retrieval.
    No physics or game logic.
    """

    def __init__(self, size: int = 256):
        self.size = size
        self.grid = np.zeros((size, size, size), dtype=np.uint8)


    # Basic Access
    def in_bounds(self, x: int, y: int, z: int) -> bool:
        return (
            0 <= x < self.size and
            0 <= y < self.size and
            0 <= z < self.size
        )

    def get(self, x: int, y: int, z: int) -> int:
        if not self.in_bounds(x, y, z):
            raise IndexError("VoxelGrid access out of bounds")
        return int(self.grid[x, y, z])

    def set(self, x: int, y: int, z: int, value: int) -> None:
        if not self.in_bounds(x, y, z):
            raise IndexError("VoxelGrid write out of bounds")
        self.grid[x, y, z] = np.uint8(value)

    # Observation Support
    def get_local_window(self, center: tuple[int, int, int], radius: int = 3) -> np.ndarray:
        """
        Returns a (2r+1, 2r+1, 2r+1) window.
        Clips automatically at boundaries.
        """
        x, y, z = center
        r = radius

        x_min = max(0, x - r)
        x_max = min(self.size, x + r + 1)

        y_min = max(0, y - r)
        y_max = min(self.size, y + r + 1)

        z_min = max(0, z - r)
        z_max = min(self.size, z + r + 1)

        return self.grid[x_min:x_max, y_min:y_max, z_min:z_max].copy()


    # Utility
    def snapshot(self) -> np.ndarray:
        """
        Returns a copy of the full voxel grid.
        Used for logging or replay.
        """
        return self.grid.copy()
