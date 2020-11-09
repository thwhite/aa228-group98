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

    # print(f'UTILITIES: {utilities}')

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

    turn(agent_copy, policy_step, foe_copy, "expectation")

    return utility + discount*reward.get_reward(agent_copy, foe_copy)


def test_forward_search(
    agent: Agent,
    foe: Foe,
    reward: Reward,
    utility: float,
    depth: int = 3,
    discount: float = 0.9,
    e: float = 0.15
    ) -> (str, float):

    if depth <= 0 or agent.hp <= 0: # Also stop searching if we die, bc why bother
        return ("none", utility)

    best_action = ("none", np.NINF)

    best_next_action, Up = test_forward_search(
        agent, foe, reward, utility, depth-1
    )

    utilities = dict()

    for policy_step in agent.get_available_actions():

        utilities[policy_step] = Up + __lookahead(
            agent, foe, policy_step, reward, discount
        )

    max_u_action = max(utilities, key=utilities.get)
    best_action = (max_u_action, utilities[max_u_action])

    if random.random() < e: # Toggle shield occasionally so we can see things happen?
        best_action = ("toggle shield", utilities["toggle shield"])


#    turn(agent, best_action[0], foe, "expectation")

    return best_action
