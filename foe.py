import random

class Foe:

    def __init__(self):
        self.hp = 127
        self.stats = [18, 19, 17, 14, 16, 15]
        self.states = {"AC": 20, "buffed": 0, "radiant_cooldown": 4, "hit_large_cooldown": 1}
        self.actions = {"hit_small": 1, "hit_large": 1, "buff": 1, "radiant_breath": 1}

    def act(self):
        e = random.random()

        # Note: turns out choosing a random action is remarkably hard to do since they're all in a dict
        # and the specific details have to be specified into the action object.

        # Current implementation has random chance to taking default action even when inadviseable. This is less
        # than we were hoping but hopefully ok for MVP.

        if self.actions["radiant_breath"] and e < 0.7:
            action = Action()
            self.actions["radiant_breath"] = 0
            self.states["radiant_cooldown"] = 4
        elif self.actions["hit_large"] and e < 0.7:
            action = Action()
            self.actions["hit_large"] = 0
            self.states["hit_large_cooldown"] = 1
        elif self.actions["buff"] and e < 0.7:
            action = Action()
        else:
            action = Action()
        return action

    def decrement_cooldowns(self):
        if self.states["cooldown"] >= 1:
            self.states["cooldown"] = self.states["cooldown"] - 1
        elif not self.states["cooldown"]:
            self.actions["radiant_breath"] = 1

