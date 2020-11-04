from action import Action

class Agent:

    def __init__(self):
        self.hp = 12
        self.stats = {"str":2, "dex":2, "con":2, "int":2, "wis":2, "cha":2, "AC": 15} # six traditional stats and AC
        self.states = {"shield": 1, "absorb": 1, "spell slots": 6}

    def get_available_actions(self):
        actions = ["hit", "toggle_shield"]
        if not self.states["shield"]:
            actions.append("harder_hit")
        if self.states["spell_slots"] != 0:
            actions.append(["absorb", "claws", "healing", "moonbeam"])
        return actions

    def act(self, policy_step):

        if policy_step == "toggle_shield":
            self.states["shield"] = 1 - self.states["shield"] # flips the bit
            if self.states["shield"]:
                self.stats["wis"] += 2
            elif not self.states['shield']:
                self.stats["wis"] -= 2
            action = Action(self)
        elif policy_step == "absorb":
            self.states["absorb"] = 1
            self.states["spell_slots"] -= 1
            action = Action(self)
        elif policy_step == "claws":
            action = Action(self, 1, "wis", 1, "wis", "con", "radiant_cooldown", 1, 1)
        elif policy_step == "healing":
            action = Action() # healing
        elif policy_step == "moonbeam":
            action = Action() # moonbeam
        elif policy_step == "harder_hit":
            action = Action()
        elif policy_step == "hit":
            action = Action() # hit
        else:
            action = Action(self, self) # default

        return action
