class Agent:

    def __init__(self):
        self.hp = 12
        self.stats = [14, 14, 14, 14, 14, 14]
        self.states = {"AC": 15, "absorb": 1} # Thomas I think this needs to be {"AC": 15}, etc -- Valerie
        self.actions = {"don": 1, "doff": 0, "absorb": 1, "claws": 1, "healing": 1, "moonbeam": 1, "spell slots": 6}

    def act(input, policy):
        # do I put an if/else tree here?!? Needs to be parametricized.
        action = Action(policy)

        return action
