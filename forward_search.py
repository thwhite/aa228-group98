import copy
import numpy as np
import random

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
    discount: float = 0.9
    ) -> (str, float):

    if depth <= 0:
        return ("none", utility)

    best_action = ("none", np.NINF)

    best_next_action, Up = forward_search(
        agent, foe, reward, utility, depth-1
    )

    utilities = {}

    for policy_step in agent.get_available_actions():

        utilities[policy_step] = Up + __lookahead(
            agent, foe, policy_step, reward, discount
        )

    print(f'UTILITIES: {utilities}')

    max_u_action = max(utilities, key=utilities.get)
    best_action = (max_u_action, Up)

    turn(agent, best_action[0], foe, "expectation")

    return best_action


def __lookahead(
    agent: Agent, # Agent and foe represent the full state
    foe: Foe,
    policy_step: str,
    reward: Reward,
    discount: float
    ) -> float:

    agent_copy = copy.deepcopy(agent)
    foe_copy = copy.deepcopy(foe)

    utility = reward.get_reward(agent_copy, foe_copy)
    # print(f'a states before: {agent_copy.states}')
    # print(f'f states before: {foe_copy.states}')
    # print(f'utility before lookahead turn: {utility}')

    turn(agent_copy, policy_step, foe_copy, "expectation")

    # print(f'a states after: {agent_copy.states}')
    # print(f'f states after: {foe_copy.states}')
    # print(f'utility after lookahead turn: {reward.get_reward(agent_copy, foe_copy)}')

    return utility + discount*reward.get_reward(agent_copy, foe_copy)
