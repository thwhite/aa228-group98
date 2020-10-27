class Action:

    def __init__(self,
    actor: Agent = Agent(),
    targets: [Character] = [Foe()],
    dice_roll: [int],
    modifier: str,
    effect: str
    ):
        self.actor = actor
        self.targets = targets
        self.dice_roll = dice_roll
        self.modifier = modifier
        self.effect = effect

    def resolve_action(self) -> delta_states: dict:

    # what is the recipe for an action?
        #     1. roll dice, add modifiers
        #     2. compare rolls/AC/etc.
        #     3. roll damage
        #     4. calculate state updates

        delta_states = {"hp": 0}

        return delta_states
