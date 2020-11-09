import random
from action import Action
import numpy as np


class Foe:

    def __init__(self):
        self.hp = 127
        self.max_hp = 127
        self.stats = {
            "str": 5, "dex": 3, "con": 3, "int": 0, "wis": 0, "cha": 3,
            "AC": 18
        }
        self.states = {
            "radiant cooldown": 4, "hit large cooldown": 1
        }

    def get_available_actions(self):
        actions = ["hit small"]
        if self.states["radiant cooldown"] == 0:
            actions.append("harder hit")
        if self.states["hit large cooldown"] == 0:
            actions.append(["hit large"])
        return actions

    def act(self, mode):
        if mode == "random":
            e = random.random()
        else:
            e = 0

        if not self.states["radiant cooldown"] and e < 0.7:
            action = Action(
                self, "other guy", 20, "wis", 20, "dex", "hp", 10, 2
            )
            self.states["radiant cooldown"] = 4
        elif not self.states["hit large cooldown"] and e < 0.7:
            action = Action(
                self, "other guy", 20, "str", 1, "AC", "hp", 6, 2
            )
            self.states["hit large cooldown"] = 1
        elif self.states["radiant cooldown"] > 2 and e < 0.7:
            self.states["radiant cooldown"] -= 2
            action = Action(self, "self")
        else:
            action = Action(
                self, "other guy", 20, "str", 1, "AC", "hp", 4, 1
            )
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
        # health remaining, with error.

        signal = "RAW" + "R"*np.clip(
            int(14 - self.hp/10 + random.randint(-1, 1)), 0, 14
        )

        return signal
