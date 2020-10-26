class Foe:

    def __init__(self):
        self.hp = 127
        self.stats = [18, 19, 17, 14, 16, 15]
        self.states = {"AC", 20, "buffed", 0, "cooldown", 4}
        self.actions = {"hit_small", 1, "hit_large", 1, "buff", 1, "radiant_breath", 1}

    def act(self, input):
        action = Action()

        if self.actions["radiant_breath"]:

        elif self.actions["buff"]:



        return action

    def decrement_cooldowns(self):
        if self.states["cooldown"] >= 1:
            self.states["cooldown"] = self.states["cooldown"] - 1

