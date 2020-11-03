class DungeonState:

  def __init__(self, agent: Agent, foe: Foe):
      self.agent = agent
      self.foe = foe

#
# def state_to_index(self, state):
#     idx = 10*state.hp + 10*state.ac
#     return idx
#
# def index_to_state(self,idx):
#     hp = np.mod(idx,self.MAX_HP) #
#     ac = ....
#     return State(hp,ac)
