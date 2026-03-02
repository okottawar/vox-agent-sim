# world/core/action_resolver.py

from world.enums import ActionType
from world.schemas import ActionResult


class ActionResolver:
    """
    Mediates between agent actions and physics engine.
    Does NOT contain physics logic.
    """

    def __init__(self, physics_engine):
        self.physics = physics_engine

    def resolve(self, state, action: ActionType) -> ActionResult:
        """
        Resolves agent action via physics engine.
        """
        return self.physics.resolve_action(state, action)