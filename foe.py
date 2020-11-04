import random
from action import Action

class Foe:

    def __init__(self):
        self.hp = 127
        self.stats = {"str": 4, "dex": 4, "con": 3, "int": 2, "wis": 3, "cha": 3, "AC": 20}
        self.states = {"buffed": 0, "radiant_cooldown": 4, "hit_large_cooldown": 1}

    def get_available_actions(self):
        actions = ["hit_small"]
        if self.states["buffed"] == 0:
            actions.append("harder_hit")
        if self.states["radiant_cooldown"] == 0:
            actions.append("harder_hit")
        if self.states["hit_large_cooldown"] != 0:
            actions.append(["hit_large"])
        return actions

    def act(self):
        e = random.random()

        if not self.states["radiant_breath"] and e < 0.7:
            action = Action(self, 20, "wis", 20, "dex", "hp", 10, 1)
            self.states["radiant_cooldown"] = 4
        elif not self.states["hit_large_cooldown"] and e < 0.7:
            action = Action(self, 20, "str", 20, "dex", "hp", 6, 1)
            self.states["hit_large_cooldown"] = 1
        elif self.states["buff"] and e < 0.7:
            action = Action(self, 20, "int", 20, "none", "radiant_cooldown", 1, 1)
        else:
            action = Action(self, 20, "str", 20, "dex", "hp", 4, 1)
        return action

    def decrement_cooldowns(self):
        if self.states["radiant_cooldown"] >= 1:
            self.states["radiant_cooldown"] = self.states["radiant_cooldown"] - 1
        if self.states["hit_large_cooldown"] >= 1:
            self.states["hit_large_cooldown"] = self.states["hit_large_cooldown"] - 1

