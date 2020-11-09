import copy
import numpy as np

from action import Action
from agent import Agent
from foe import Foe
from reward import Reward
from turn import turn


def forward_search(
    agent: Agent,
    foe: Foe,
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
        agent_copy, foe_copy, reward, utility, depth-1, discount
    )[1]

    for policy_step in agent_copy.get_available_actions():
        utility = Up + __lookahead(
            agent_copy, foe_copy, policy_step, reward, discount
        )
        if utility > best_action[1]:
            best_action = (policy_step, utility)

    return best_action


def __lookahead(
    agent: Agent, # Agent and foe represent the full state
    foe: Foe, # This is a faux foe
    policy_step: str,
    reward: Reward,
    discount: float,
    ) -> float:

    agent_copy = copy.deepcopy(agent)
    foe_copy = copy.deepcopy(foe)

    utility = reward.get_reward(agent_copy, foe_copy)
    turn(agent_copy, policy_step, foe_copy, "expectation")

    return utility + discount*reward.get_reward(agent_copy, foe_copy)
