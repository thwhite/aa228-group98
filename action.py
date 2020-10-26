class action:

    def __init__(self, actor: Actor, targets, dice_roll: [int], effect: str):
        self.actor
        self.targets
        self.dice_roll
        self.modifier
        self.effect

    def resolve_action(self) -> delta_states: dict:

        # what is the recipe for an action?
        #     1. roll dice, add modifiers
        #     2. compare rolls/AC/etc.
        #     3. roll damage
        #     4. calculate state updates

        delta_states = {"hp": 0}

        return delta_states
