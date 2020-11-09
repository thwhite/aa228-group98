import random
from action import Action
import numpy as np


class Foe:

    def __init__(self):
        # Note: DungeonStates assumes that all states start at their max
        # possible value, and further that they are ints that cannot go
        # negative.
        self.hp = 127
        self.max_hp = 127
        self.stats = {
            "str": 4, "dex": 4, "con": 3, "int": 2, "wis": 3, "cha": 3,
            "AC": 20
        }
        self.states = {
            "buffed": 1, "radiant cooldown": 4, "hit large cooldown": 1
        }

    def get_available_actions(self):
        actions = ["hit small"]
        if self.states["buffed"] == 0:
            actions.append("harder hit")
        if self.states["radiant cooldown"] == 0:
            actions.append("harder hit")
        if self.states["hit large cooldown"] != 0:
            actions.append(["hit large"])
        return actions

    def act(self):
        e = random.random()

        if not self.states["radiant cooldown"] and e < 0.7:
            action = Action(self, 20, "wis", 20, "dex", "hp", 10, 1)
            self.states["radiant cooldown"] = 4
        elif not self.states["hit large cooldown"] and e < 0.7:
            action = Action(self, 20, "str", 20, "dex", "hp", 6, 1)
            self.states["hit large cooldown"] = 1
        elif self.states["buffed"] and e < 0.7 and self.states["radiant cooldown"] < 2:
            self.states["radiant cooldown"] -= 2
            action = Action(self)
        else:
            action = Action(self, 20, "str", 20, "dex", "hp", 4, 1)
        return action

    def decrement_cooldowns(self):
        if self.states["radiant cooldown"] >= 1:
            self.states["radiant cooldown"] = self.states["radiant cooldown"] - 1
        if self.states["hit large cooldown"] >= 1:
            self.states["hit large cooldown"] = self.states["hit large cooldown"] - 1

    def update_states(self, new_foe_states):

        foe_states = dict(new_foe_states)
        self.hp = foe_states.pop("hp")
        self.states = foe_states

    def react(self):
        # Note to grader: this implementation is inefficient, but fun.
        # Adds a number of Rs between 0 and 10 that roughly corresponds to
        # health remaining percentage, with error.
        signal = "RAW" + "R"*np.clip(
            int(10 - 10*self.hp/self.max_hp + random.randint(-1, 1)), 0, 10
        )

        # @Thomas: different reactions for buff/debuff/etc if we ever get there?

        return signal
