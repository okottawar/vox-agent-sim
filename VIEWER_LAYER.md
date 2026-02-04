# **Viewer Layer** (`VIEWER_LAYER.md`)  

# Web Viewer Layer

## Responsibilities
- Render the voxel world and agents in 3D
- Provide play/pause timeline functionality
- Support camera movement (orbit, pan, zoom)
- Optionally overlay:
  - Agent vision
  - Visited cells
  - Agent trails

---

## Implementation
- **Technology**: Three.js (WebGL)
- **Input**: world state snapshots or live updates from container
- **Rendering**:
  - Voxels → cubes
  - Agents → colored cubes/arrows
  - Optional overlays: heatmaps, vision cone
- **Controls**:
  - Play / Pause / Step
  - Camera controls (orbit, pan, zoom)

---

## Non-Responsibilities
- Viewer does **not** affect world state or agent actions
- Viewer does **not** compute physics
- Viewer does **not** compute agent decisions

---

## Future Extensions
- Multi-agent visualization
- Replay timeline scrubbing
- Visualization for benchmarking and experiment overlays
