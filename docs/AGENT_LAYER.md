# Agent Layer

## Responsibilities
- Observe the local world state
- Produce actions via policy/model
- Log behavior for analysis
- Support plug-and-play for multiple agent models

---

## Agent API (Minimal)

```python
reset() -> internal_state
step(observation, internal_state) -> (action, new_state)
```

### Responsibilities

- **reset()**: Initialize agent for a new episode.
- **step()**: Take an observation and internal state, output action and new internal state.

## Agent Mechanics

**Observation**: local voxel window, agent energy, inventory, orientation

**Actions**: MOVE_FORWARD, TURN_LEFT, TURN_RIGHT, BREAK_BLOCK, PLACE_BLOCK, IDLE

**Policy**: can be RL-based (PPO, DQN), rule-based, or evolutionary

**Reward Function**: task-specific (e.g., exploration, resource collection)

**Memory**: optional hidden state for multi-step planning

---

## Logging

- Observation at each tick
- Action taken
- Reward received
- World state delta (optional)
- Timestamp / tick
- Agent ID / version

---

## Containerization (Optional)

- Agent can run in its own container
- Communicates with world container via API or WebSocket
- Enables swapping agent versions without touching the world

---

## Future Extensions

- Multi-agent interactions
- Curriculum learning
- Competitions & leaderboards
