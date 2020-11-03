import random

class Foe:

    def __init__(self):
        self.hp = 127
        self.stats = [18, 19, 17, 14, 16, 15]
        self.states = {"AC": 20, "buffed": 0, "cooldown": 4}
        self.actions = {"hit_small": 1, "hit_large": 1, "buff": 1, "radiant_breath": 1}

    def act(self):
        e = random.random()

        if e > 0.7:
            # choose a random action and do it
        else:
            if self.actions["radiant_breath"]:
                action = Action()
            elif self.actions["buff"]:
                action = Action()
            elif self.actions["hit_large"]

        if self.actions["radiant_breath"]:

        elif self.actions["buff"]:



        return action

    def decrement_cooldowns(self):
        if self.states["cooldown"] >= 1:
            self.states["cooldown"] = self.states["cooldown"] - 1
        elif not self.states["cooldown"]:
            self.actions["radiant_breath"] = 1

