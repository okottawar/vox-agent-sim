# Containerized Voxel World + Agent Simulation Roadmap

## Project Vision
Build a reproducible, containerized voxel world simulation platform with:
- Versioned physics and terrain
- Plug-and-play agent models
- Web-based visualization (play/pause/replay)
- Logging for behavior analysis
- Future: competitions for multiple agents

---

## Stages and Tasks

### Stage 0 — Project Specification
- Task 0.1: Define coordinate system
- Task 0.2: Define voxel types, terrain features
- Task 0.3: Define physics laws and tick rate
- Task 0.4: Define observation & action spaces
- Task 0.5: Define logging schema
- Task 0.6: Define container communication (API/WebSocket)
> Outcome: A 1–2 page spec freezing assumptions

---

### Stage 1 — World Generation (Containerized)
- Task 1.1: Design layer/component structure
    - Components: Terrain Generator, Physics Engine, Tick Manager, State Store
- Task 1.2: Define functionalities of each component
- Task 1.3: Technical blueprint (classes, methods, data structures)
- Task 1.4: Implement & unit-test components independently
- Task 1.5: Integrate components & perform integration testing
- Task 1.6: Containerize world & test reproducibility
- Future Task: Versioned worlds (same physics, different terrain)

**Output:** `docker run world:v1` produces deterministic world state

---

### Stage 1.5 — Web Viewer
- Task 1.5.1: Design user interface and camera controls
- Task 1.5.2: Implement interface using three.js
- Task 1.5.3: Connect viewer to backend/container (replay or live)
> Outcome: Play/pause timeline viewer showing voxel world + agent (simple cube)

---

### Stage 2 — Agent Mechanics
- Task 2.1: Define agent algorithm, behavior policy, RL mechanism, energy/reward rules
- Task 2.2: Build agent API (`reset()`, `step(obs) -> action`) and logging
- Task 2.3: Test agent on synthetic data
- Task 2.4: Integrate agent with world (small tests)
- Task 2.5: Run full simulations and refine

**Optional:** Package agent as container for modular communication with world

---

### Stage 2+ — Behavior Analysis
- Task 2+.1: Form hypotheses on agent behavior in different environments
- Task 2+.2: Run experiments & log results
- Task 2+.3: Build evaluation metrics & benchmark agents
- Task 2+.4: Create visualizations for analysis

---

## Layer Dependencies
```
World Container → Agent Container → Logging DB → Web Viewer
```
- World runs independently
- Agent reads observations & writes actions + logs
- Viewer reads world/agent state only

---

## Notes
- Separation of concerns is critical
- Unit-test each component before integration
- Logging early prevents debugging nightmares
- Version everything: physics, world, agent
