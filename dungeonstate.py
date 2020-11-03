import numpy as np

class DungeonState:

    # BIG TODO: test

  def __init__(self, initial_agent: Agent, initial_foe: Foe):
      # Note: This assumes that all states start at their max possible value,
      # and further that they are ints that cannot go negative.
      # TODO: Add this note to agent/foe.py
      self.available_agent_states = agent.states
      self.available_agent_hp = agent.hp
      self.available_foe_states = foe.states
      self.available_foe_hp = foe.hp

    def agent_foe_to_index(self, agent: Agent, foe: Foe): -> idx: int

        states = {
            'agent': {*agent.states, agent.hp}
            'foe': {*foe.states, foe.hp}
        }

        return self.state_to_index(states)


    def state_to_index(self, states): -> idx: int

        return self.__index_from_states(
            self.__align_state_and_dim_arrays(states)
        )


    def index_to_states(self, idx): -> state: dict

        available_states = self.available_states_dict()

        for ## Valerie, you're here


        # wrap agent.hp into agent.states
        return {agent: agent.states, foe: foe.states}


    def __align_state_and_dim_arrays(self, states):

        available_states = self.available_states_dict()

        state_array = [
            states[a][s]
            for s in states[a].keys() & available_states[a].keys()
            for a in ['agent', 'foe']
        ]

        state_dims = [
            available_states[a][s]
            for s in states[a].keys() & available_states[a].keys()
            for a in ['agent', 'foe']
        ]

        return state_array, state_dims

    def __index_from_states(self, states, state_dims):

        return np.sum(
            [
                state*np.prod(
                    [dim for dim in state_dims[i+1:]]
                )
                for i, state in enumerate(states)
            ]
        )

    def available_states_dict(self): -> dict

        return {
            'agent': self.available_agent_states,
            'foe': self.available_foe_states
        }
