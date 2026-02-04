# World Simulation Layer

## Responsibilities
- Maintain authoritative voxel world state
- Apply deterministic physics rules
- Advance simulation by discrete ticks
- Store world state snapshots
- Interface with agents (via API/WebSocket)

---

## Components

### Terrain Generator
- Generates voxel-based terrain grid
- Defines resources, obstacles
- Input: seed, world config
- Output: voxel grid

### Physics Engine
- Applies laws of motion
- Resolves collisions
- Manages energy costs
- Versioned (physics:v1, physics:v2)

### Tick Manager
- Advances world state step by step
- Calls physics & agent actions
- Ensures determinism

### State Store
- Holds world state at current tick
- Optionally logs snapshots for replay

---

## World Container
- Encapsulates all components
- Headless (no rendering)
- Deterministic run with fixed seed
- Exposes API to agent container

---

## Output
- World state snapshot: voxel grid, agent positions, metadata
- Replay logs for viewer or behavior analysis

---

## Future Extensions
- Terrain versioning independent of physics
- Multi-agent support
- Procedural world generation (different biomes)
