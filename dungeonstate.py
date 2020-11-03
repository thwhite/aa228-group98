import numpy as np

class DungeonState:

    # BIG TODO: test

    def __init__(self, initial_agent: Agent, initial_foe: Foe):
        # Note: This assumes that all states start at their max possible value,
        # and further that they are ints that cannot go negative.
        # TODO: Add this note to agent/foe.py
        self.available_states = {
            'agent': {*initial_agent.states, initial_agent.hp},
            'foe': {*initial_foe.states, initial_foe.hp},
      }

    def agent_foe_to_index(self, agent: Agent, foe: Foe): -> idx: int

        return self.state_to_index(state_dict(agent, foe))


    def state_to_index(self, states): -> idx: int

        return self.__index_from_states(
            self.__align_state_and_dim_arrays(states)
        )


    def index_to_states(self, idx): -> state: dict

        states = {}

        for a in ['agent', 'foe']:
            for state, max_state in self.available_states[a]:
                a_states[state] = idx % (max_state + 1)
                idx //= (max_state + 1)
            states[a] = a_states

        return states


    def __align_state_and_dim_arrays(self, states): -> state_array, state_dims

        state_array = [
            states[a][s]
            for s in states[a].keys() & self.available_states[a].keys()
            for a in ['agent', 'foe']
        ]

        state_dims = [
            available_states[a][s]
            for s in states[a].keys() & self.available_states[a].keys()
            for a in ['agent', 'foe']
        ]

        return state_array, state_dims

    def __index_from_states(self, states, state_dims): -> idx: int

        return np.sum(
            [
                state*np.prod(
                    [dim for dim in state_dims[i+1:]]
                )
                for i, state in enumerate(states)
            ]
        )

def state_dict(agent: Agent, foe: Foe): -> states: state_dict

    return {
        'agent': {*agent.states, agent.hp},
        'foe': {*foe.states, foe.hp}
    }
