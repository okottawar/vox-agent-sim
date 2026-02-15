# world/enums.py

from enum import IntEnum

# Voxel Types
class VoxelType(IntEnum):
    AIR = 0
    GRASS = 1
    ROCK = 2
    WATER = 3
    ENERGY = 4

# Agent Orientation
class Orientation(IntEnum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

# Agent Actions
class ActionType(IntEnum):
    MOVE_FORWARD = 0
    MOVE_BACKWARD = 1
    MOVE_LEFT = 2
    MOVE_RIGHT = 3
    BREAK = 4
    IDLE = 5
