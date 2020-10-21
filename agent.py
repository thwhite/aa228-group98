class Agent:

    def __init__(self):
        self.hp = 12
        self.stats = [12, 12, 12, 12, 12, 12] # Intialize stats

    # Question: should each kind of attack be a function? Or are we going to have a list of functions?

    def act(self, action):
        if action == 1:
            # do stuff
        elif action == 2:
            # do more stuff
        else:
            # raise exception

