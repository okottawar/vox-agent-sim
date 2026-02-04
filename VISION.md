# Containerized Voxel World + Agent Simulation Platform

## 1. Vision
Build a reproducible, containerized voxel world simulation platform where:
- Physics rules are stable and versioned
- Terrains/worlds can change independently
- Agents can be plugged in, evaluated, and compared
- Worlds can be visualized via a simple web viewer
- Experiments are deterministic, loggable, and replayable

Long-term goal: enable benchmarking, research, and competitive agent challenges.

---

## 2. Core Design Principles
- **Separation of concerns**
  - World simulation ≠ agent logic ≠ visualization
- **Determinism**
  - Fixed seeds, fixed physics, reproducible runs
- **Versioned physics**
  - Physics changes are explicit and never silent
- **Agents are external**
  - World does not depend on agent implementation
- **Visualization is observational**
  - Viewer never affects simulation state

---

## 3. High-Level Architecture

```
+-------------------+ +------------------+
| Agent Process | <---> | World Container |
| | | |
| - Model | | - Physics |
| - Policy | | - Terrain |
| - Training (opt) | | - State |
+-------------------+ +------------------+
|
v
+--------------+
| Logging |
+--------------+

+---------------------------------------------+
| Web Viewer |
| - Reads world state / replay logs |
| - Renders voxels + agents |
| - Play / pause / scrub |
+---------------------------------------------+
```

---

## 4. Development Stages

### Stage 0 — Specification (Required)
Define:
- Coordinate system
- Tick rate
- Block types
- Action space
- Observation space
- Physics versioning rules

_No implementation yet._

---

### Stage 1 — World Simulation (Containerized)
**Goal:** Deterministic voxel world generation and stepping.

Scope:
- Terrain generation
- Physics rules
- Tick-based state updates
- Deterministic RNG
- No agents
- No rendering

Output:
- World state snapshots
- Optional replay logs

---

### Stage 1.5 — Web Viewer (Read-Only)
**Goal:** Visualize world state for humans.

Scope:
- Web-based voxel renderer (e.g. three.js)
- Agent represented as simple geometry
- Play / pause
- Optional timeline scrubbing

Non-goals:
- No interaction with world
- No agent logic
- No editing tools

---

### Stage 2 — Agent Mechanics
**Goal:** Enable agents to act in the world.

Scope:
- Agent API (observation → action)
- Plug-and-play agent models
- Logging of behavior
- Support multiple agent implementations

Non-goals:
- No advanced UI
- No competitions yet

---

## 5. World Simulation

### Responsibilities
- Maintain authoritative world state
- Apply physics rules
- Resolve agent actions
- Advance simulation by fixed ticks

### Properties
- Deterministic given:
  - Physics version
  - World config
  - RNG seed
- Headless (no rendering)

---

## 6. Physics Versioning
- Physics changes require a new version
- Old physics versions remain immutable
- Worlds reference a specific physics version

Example:
```
physics:v1.0.0
physics:v2.0.0 (breaking change)
```

---

## 7. Agent System

### Definition
An agent is a function:
```
action = f(observation)
```

### Agent API (Minimal)

```
reset() -> internal_state
step(observation, internal_state) -> (action, new_state)
```


### Agent Characteristics
- Stateless or stateful (memory optional)
- Model-agnostic (ML, rules, evolution, etc.)
- Does not access full world state
- Does not access renderer

---

## 8. Observations
Possible observation formats:
- Local voxel window (NxNxN)
- Symbolic features (energy, inventory, orientation)
- No global map unless explicitly provided

---

## 9. Actions
Discrete action set (example):
- MOVE_FORWARD
- TURN_LEFT
- TURN_RIGHT
- BREAK_BLOCK
- PLACE_BLOCK
- IDLE

World decides validity and consequences.

---

## 10. Logging & Replay

### Logged Data
- World seed
- Physics version
- Agent version
- (observation, action, reward)
- World state deltas (optional)

### Use Cases
- Debugging
- Behavior analysis
- Replay visualization
- Benchmark comparison

---

## 11. Viewer

### Responsibilities
- Render world state
- Render agents
- Show overlays (optional):
  - Agent vision
  - Visited cells
  - Trails

### Non-Responsibilities
- No physics
- No agent decisions
- No training logic

---

## 12. Technology (Initial)
- World simulation: language-agnostic (TBD)
- Containerization: Docker
- Viewer: Web (three.js)
- Agent models: ML / rule-based / evolutionary
- Communication: API / logs / sockets (TBD)

---

## 13. Future Extensions
- Multi-agent worlds
- Agent submission system
- Hosted competitions
- Benchmark suites
- Curriculum worlds
- Leaderboards

---

## 14. Explicit Non-Goals (for now)
- AAA graphics
- Real-time human gameplay
- Complex UI/UX
- Massive open worlds
- Non-deterministic physics

---

## 15. Success Criteria
- Worlds are reproducible
- Agents are comparable
- Visualization is decoupled
- Experiments are explainable
