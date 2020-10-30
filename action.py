
import random

class Action:

    def __init__(self, *kwargs):
        self.actor = kwargs["Actor"]
        self.target = kwargs["Target"]
        self.attack_roll = kwargs["attack_roll"]
        self.save_stat = kwargs["save_stat"]




    def resolve_action(self):
        attack = random.randint(1, self.attack_roll)
        if attack >= self.target.states["AC"]:
            defend = self.target.stats["save_stat"] #This format is wrong rihgt now, will figure later
            if random.randint(1, defend) <= save_stat:
                # how to handle actions. is it true that every action increments or decremets a stat of some form?




self.agent
    self.foe
    self.dice_roll
    self.modifier
    self.effect <-- which state(s) changes?
    ... etc
    what is the recipe for an action?
        1. roll dice, add modifiers
        2. compare rolls/AC/etc.
        3. roll damage
        4. calculate state updates

    functions:
        - resolve_action() returns delta_states

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

