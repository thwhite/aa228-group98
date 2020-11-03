import random

class Foe:

    def __init__(self):
        self.hp = 127
        self.stats = [18, 19, 17, 14, 16, 15, 20] # six normal states and AC
        self.states = { "buffed": 0, "radiant_cooldown": 4, "hit_large_cooldown": 1}

    def get_available_actions(self):
        actions = ["hit_small", "buff"]
        if self.states["radiant_cooldown"] is 0:
            actions.append("harder_hit")
        if self.states["hit_large_cooldown"] is not 0:
            actions.append(["hit_large"])
        return actions

    def act(self):
        e = random.random()

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

