import copy
import numpy as np

from action import Action
from agent import Agent
from dungeonstate import DungeonState
from foe import Foe
from reward import Reward


def forward_search(
    depth: int = 3,
    discount: float = 0.9,
    agent: Agent,
    foe: Foe,
    dungeonstate: DungeonState
    reward: Reward
    utility: float
    # MC_policy,
    # forward_search_weight: float = 1
    ): -> action: str, utility: float

    faux_agent = copy.deepcopy(bb_agent)
    faux_foe = copy.deepcopy(bb_foe)

    idx = dungeonstate.agent_foe_to_index(faux_agent, faux_foe) # How is this used?

    if depth <= 0:
        return ("none", utility)
    best_action = ("none", reward.get_worst_reward())

    Up = forward_search(depth-1, discount, agent, foe, dungeonstate, utility)[1]

    for action in agent.get_available_actions():
        utility = Up + __lookahead(agent, foe, action, reward, discount)
        if utility > best_action[1]:
            best_action = (action, utility)

    return best_action


def __lookahead(
    agent: Agent, # Agent and foe represent the full state
    foe: Foe,
    action: Action,
    reward: Reward,
    discount: float,
    ): -> utility: [float]

    # What is transition?
    # Wait, should we learn it with a model-based approach?
    # Transition(agent stats, foe stats [unknown -- belief])
    # Given a belief, do we know the transition matrix? Yes. But also, we can
    # skip that entirely, we think.
    # Action -> "calculate_action_expectation" which uses our brains and
    # knowledge of probability to "learn" action value [Q(a)]

    # Note - utility of action expectation is the sum of the actor and foe action utilities

    utility = reward.get_reward(agent, foe) + discount*(
        reward.get_reward(action.get_action_expectation(foe))
    )

    return utility
