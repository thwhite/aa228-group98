from action import Action

class Agent:

    def __init__(self):
        # Note: DungeonStates assumes that all states start at their max
        # possible value, and further that they are ints that cannot go
        # negative.
        self.hp = 120
        self.max_hp = 120
        self.stats = {
            "str": 2, "dex": 2, "con": 2, "int": 2, "wis": 2, "cha": 2,
            "AC": 15
        }  # six traditional stats and AC
        self.states = {
            "shield": 1, "absorb": 1, "spell slots": 6
        }

    def get_available_actions(self):
        actions = ["hit", "toggle shield"]
        if not self.states["shield"]:
            actions.append("harder hit")
        if self.states["spell slots"] != 0:
            actions.extend(["absorb", "claws", "moonbeam"])
        if self.states["spell slots"] != 0 and (self.max_hp - self.hp) > 6:
            actions.append("healing")
        return actions

    def act(self, policy_step):

        if policy_step == "toggle shield":
            self.states["shield"] = 1 - self.states["shield"]  # flips the bit
            if self.states["shield"]:
                self.stats["AC"] += 2
            elif not self.states['shield']:
                self.stats["AC"] -= 2
            action = Action(self)
        elif policy_step == "absorb":
            self.states["absorb"] = 1
            self.states["spell slots"] -= 1
            action = Action(self)
        elif policy_step == "claws":
            action = Action(self, 20, "wis", 20, "wis", "radiant cooldown", 4, 1)
        elif policy_step == "healing":
            action = Action(self, 20, "wis", 20, "none", "hp", 6, -1)
        elif policy_step == "moonbeam":
            action = Action(self, 20, "wis", 20, "con", "hp", 6, 1)
        elif policy_step == "harder hit":
            action = Action(self, 30, "str", 20, "con", "hp", 6, 1)
        elif policy_step == "hit":
            action = Action(self, 20, "str", 20, "con", "hp", 4, 1)
        else:
            action = Action(self)  # default, empty action

        return action

    def update_states(self, new_agent_states):

        agent_states = dict(new_agent_states)

        self.hp = agent_states.pop("hp")
        self.states = agent_states
