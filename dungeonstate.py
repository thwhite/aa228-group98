import numpy as np

from agent import Agent
from foe import Foe


class DungeonState:
    # TODO: Better documentation
    # Do we even use state_to_idx??? I don't think so?

    def __init__(self, initial_agent: Agent, initial_foe: Foe):
        # Note: This assumes that all states start at their max possible value,
        # and further that they are ints that cannot go negative.
        max_states = {
            "agent": {**initial_agent.states, **{"hp": initial_agent.hp}},
            "foe": {**initial_foe.states, **{"hp": initial_foe.hp}},
        }

        # Index at 0 -> state dimension is 1 higher than max state
        self.available_states = {
            a: {
                state: max_state + 1
                for state, max_state in a_max_state.items()
            }
            for a, a_max_state in max_states.items()
        }

    def index_to_states(self, idx) -> dict:

        states = {}

        for a in ["agent", "foe"]:
            a_states = {}

            for state, state_dim in self.available_states[a].items():
                mod = idx % state_dim
                a_states[state] = mod
                idx //= state_dim

            states[a] = a_states

        return states

    def agent_foe_to_index(self, agent: Agent, foe: Foe) -> int:

        return self.state_to_index(state_dict(agent, foe))

    def state_to_index(self, states) -> int:

        return self.__index_from_states(
            states, self.available_states
        )

    def __index_from_states(self, states, available_states) -> int:

        state_dims = __flatten_state_dict(available_states)
        idx = 0

        # Reversing necessary to undo calculations in index_to_states()
        for a in ["foe", "agent"]:
            for state, value in reversed(states[a].items()):
                state_dim = state_dims.pop(f'{a} {state}')
                dim_factor = np.prod(
                    list(state_dims.values())
                ).astype(int)
                idx += value*dim_factor

        return idx


def state_dict(agent: Agent, foe: Foe) -> dict:
    # Combines .states with .hp

    return {
        "agent": {**agent.states, **{"hp": agent.hp}},
        "foe": {**foe.states, **{"hp": foe.hp}},
    }


def __flatten_state_dict(state_dict) -> dict:
    # Reduces 2-level dict to 1-level

    return {
        f'{a} {state}': value
        for a in ["agent", "foe"]
        for state, value in state_dict[a].items()
    }
