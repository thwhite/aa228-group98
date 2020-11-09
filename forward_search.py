import copy
import numpy as np

from action import Action
from agent import Agent
from dungeonstate import DungeonState
from foe import Foe
from reward import Reward


def forward_search(
    agent: Agent,
    foe: Foe,
    dungeonstate: DungeonState,
    reward: Reward,
    utility: float,
    depth: int = 3,
    discount: float = 0.9,
    # MC_policy,
    # forward_search_weight: float = 1
    ) -> (str, float):

    agent_copy = copy.deepcopy(agent)
    foe_copy = copy.deepcopy(foe)

    if depth <= 0:
        return ("none", utility)
    best_action = ("none", reward.get_worst_reward())

    Up = forward_search(
        agent_copy, foe_copy, dungeonstate, reward, utility, depth-1, discount
    )[1]

    for action in agent_copy.get_available_actions():
        utility = Up + __lookahead(agent_copy, foe_copy, action, reward, discount)
        if utility > best_action[1]:
            best_action = (action, utility)

    return best_action


def __lookahead(
    agent: Agent, # Agent and foe represent the full state
    foe: Foe, # This is a faux foe
    action: str, # TODO: rename action here to a string or something
    reward: Reward,
    discount: float,
    ) -> float:

    agent_copy = copy.deepcopy(agent)
    foe_copy = copy.deepcopy(foe)

    # Note - utility of action is the sum of the actor AND foe action utilities
    utility = reward.get_reward(agent_copy, foe_copy)

    new_states = agent_copy.act(action).resolve_action(foe_copy)
    agent_copy.update_states(new_states["actor"])
    foe_copy.update_states(new_states["target"])

    utility += discount*reward.get_reward(agent_copy, foe_copy)

    return utility
