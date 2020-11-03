from action import Action

class Agent:

    def __init__(self):
        self.hp = 12
        self.stats = [14, 14, 14, 14, 14, 14, 15] # six traditional stats and AC
        self.states = {"shield": 1, "absorb": 1, "spell slots": 6}

    def get_available_actions(self):
        actions = ["hit", "toggle_shield"]
        if not self.states["shield"]:
            actions.append("harder_hit")
        # From Valerie: when I tried to run this with 'is not 0', Python said:
        # SyntaxWarning: "is not" with a literal. Did you mean "!="?
        if self.states["spell_slots"] != 0:
            actions.append(["absorb", "claws", "healing", "moonbeam"])
        return actions

# Action.__init__(self,
#     actor, # Agent or foe
#     target, # Agent or foe
#     attack_roll: int = 20, # If no roll (such as don/doff shield), pass 1
#     modifier_stat: str, # If no modifier, pass "none"
#     target_roll: int = 1, # Similar to attack roll
#     save_stat: str, # If no save, pass "none"
#     effect: str, # <-- which state(s) changes?
#     effect_roll: [int] = [1],
#     # positive -> subtract from current state (as in damage);
#     # negative -> add (as in healing)
#     effect_modifier: int = 0
#     ):


    def act(self, policy_step):

        if policy_step == "toggle_shield":
            self.states["shield"] = not self.states["shield"] # flips the bit
            action = Action(
                self, self,
                1, "none",
                1, "none",
                effect="ac",
                # -2 if shield on -> AC increases by 2; 2 if shield off
                effect_modifier = 2 - 4*self.states["shield"],
            )
        elif policy_step == "absorb":
            action = Action() # absorb
        elif policy_step == "claws":
            action = Action() # claws
        elif policy_step == "healing":
            action = Action() # healing
        elif policy_step == "moonbeam":
            action = Action() # moonbeam
        elif policy_step == "harder_hit":
            action = Action()
        elif policy_step == "hit":
            action = Action() # hit
        else:
            action = Action() # default

        return action
