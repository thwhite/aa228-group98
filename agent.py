class Agent:

    def __init__(self):
        self.hp = 12
        self.stats = [14, 14, 14, 14, 14, 14]
        self.states = {"AC": 15, "absorb": 1, "spell slots": 6}
        self.actions = {"hit": 1, "harder_hit": 1, "don": 1, "doff": 0, "absorb": 1, "claws": 1, "healing": 1, "moonbeam": 1}

    def act(self, policy):

        # What if policy asks for an action that can't be done?
        # Non-parametric nature of the action space is actually kinda a problem.
        # A stupid approach here is to have the policy default to an

        if policy == 0 and self.actions["don"]:
            action = Action() # don
        elif policy == 1 and self.actions["doff"]:
            action = Action() # doff
        elif policy == 2 and self.actions["absorb"] and self.states["spell slots"] is not 0:
            action = Action() # absorb
        elif policy == 4 and self.actions["claws"] and self.states["spell slots"] is not 0:
            action = Action() # claws
        elif policy == 5 and self.actions["healing"] and self.states["spell slots"] is not 0:
            action = Action() # healing
        elif policy == 6 and self.actions["moonbeam"] and self.states["spell slots"] is not 0:
            action = Action() # moonbeam
        elif policy == 7 and self.actions["harder_hit"]:
            action = Action()
        else:
            action = Action() # hit

        return action
