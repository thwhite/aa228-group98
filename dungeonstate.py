import numpy as np

from agent import Agent
from foe import Foe

class DungeonState:

    # BIG TODO: test

    def __init__(self, initial_agent: Agent, initial_foe: Foe):
        # Note: This assumes that all states start at their max possible value,
        # and further that they are ints that cannot go negative.
        # TODO: Add this note to agent/foe.py
        self.available_states = {
            "agent": {**initial_agent.states, **{"hp": initial_agent.hp}},
            "foe": {**initial_foe.states, **{"hp": initial_foe.hp}},
      }

    def agent_foe_to_index(self, agent: Agent, foe: Foe) -> int:

        return self.state_to_index(state_dict(agent, foe))


    def state_to_index(self, states) -> int:

        return self.__index_from_states(
            *self.__align_state_and_dim_arrays(states)
        )


    def index_to_states(self, idx) -> dict:

        states = {}

        for a in ["agent", "foe"]:
            a_states = {}
            for state, max_state in self.available_states[a].items():
                a_states[state] = idx % (max_state + 1)
                idx //= (max_state + 1)
            states[a] = a_states

        return states


    def __align_state_and_dim_arrays(self, states) -> [int]:

        state_array = [
            states[a][s]
            for a in ["agent", "foe"]
            for s in states[a].keys() & self.available_states[a].keys()
        ]

        state_dims = [
            self.available_states[a][s]
            for a in ["agent", "foe"]
            for s in states[a].keys() & self.available_states[a].keys()
        ]

        return state_array, state_dims

    def __index_from_states(self, states, state_dims) -> int:

        return np.sum(
            [
                state*np.prod(
                    [dim for dim in state_dims[i+1:]]
                )
                for i, state in enumerate(states)
            ]
        ).astype(int)

def state_dict(agent: Agent, foe: Foe) -> dict:

    return {
        "agent": {**agent.states, **{"hp": agent.hp}},
        "foe": {**foe.states, **{"hp": foe.hp}},
    }

def actor_state(actor, state_dict) -> dict:
    # Does not include hp. To get hp, use: state_dict[actor]['hp']

    return __remove_hp(state_dict[actor])

def __remove_hp(state_dict):
    dict_without_hp = dict(state_dict)
    del dict_without_hp["hp"]
    return dict_without_hp
