import random

from action import Action

class Agent:

    def __init__(self):
        self.hp = 64
        self.max_hp = 64
        self.stats = {
            "str": 2, "dex": 2, "con": 2, "int": 2, "wis": 2, "cha": 2,
            "AC": 13
        }  # six traditional stats and AC
        self.states = {
            "shield": 0, "absorb": 0, "spell slots": 6
        }

    def get_available_actions(self):
        actions = ["hit", "toggle shield"]
        if self.states["shield"] == 0:
            actions.append("harder hit")
            if self.states["spell slots"] > 0:
                actions.append("cool breath")
                if (self.max_hp - self.hp) > 6:
                    actions.append("heal")
                if self.states["absorb"]:
                    actions.append("moonbeam")
                else:
                    actions.append("absorb")

        return actions

    def act(self, policy_step):

        if policy_step == "toggle shield":
            self.states["shield"] = 2 - self.states["shield"]  # flips the bit
            if self.states["shield"]:
                self.stats["AC"] += 2
                action = Action(self, target_id="self")
            elif not self.states['shield']:
                self.stats["AC"] -= 1
                action = Action(self, target_id="self")
        elif policy_step == "absorb":
            self.states["absorb"] = 1
            self.states["spell slots"] -= 1
            action = Action(self, target_id="self")
        elif policy_step == "cool breath":
            self.states["spell slots"] -= 1
            action = Action(
                self, attack_roll=20, attack_modifier="wis",
                target_roll=20, save_modifier="wis",
                effect="radiant cooldown", effect_roll=4, effect_modifier=-1
            )
        elif policy_step == "heal":
            self.states["spell slots"] -= 1
            action = Action(
                self, target_id="self", effect="hp", effect_roll=18, effect_modifier=-1
            )
        elif policy_step == "moonbeam":
            self.states["spell slots"] -= 1
            action = Action(
                self, attack_roll=20, attack_modifier="wis",
                target_roll=20, save_modifier="con",
                effect="hp", effect_roll=12, effect_modifier=2
            )
        elif policy_step == "harder hit":
            action = Action(
                self, attack_roll=20, attack_modifier="str",
                target_roll=1, save_modifier="AC",
                effect="hp", effect_roll=8, effect_modifier=2
            )
        elif policy_step == "hit":
            action = Action(
                self, attack_roll=20, attack_modifier="str",
                target_roll=1, save_modifier="AC",
                effect="hp", effect_roll=4, effect_modifier=0
            )
        else:
            action = Action(self, target_id="self")  # default, empty action

        return action

    def random_action(self):

        return random.choice(self.get_available_actions())

    def update_states(self, new_agent_states):

        agent_states = dict(new_agent_states)

        self.hp = agent_states.pop("hp")
        self.states = agent_states
