import copy
import numpy as np

from action import Action
from action_expectation import action_expectation
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

    faux_agent = copy.deepcopy(agent)
    faux_foe = copy.deepcopy(foe)

    # How is this used?
    # idx = dungeonstate.agent_foe_to_index(faux_agent, faux_foe)

    if depth <= 0:
        return ("none", utility)
    best_action = ("none", reward.get_worst_reward())

    Up = forward_search(
        agent, foe, dungeonstate, reward, utility, depth-1, discount
    )[1]

    for action in agent.get_available_actions():
        utility = Up + __lookahead(agent, foe, action, reward, discount)[1]
        if utility > best_action[1]:
            best_action = (action, utility)

    return best_action


def __lookahead(
    agent: Agent, # Agent and foe represent the full state
    foe: Foe,
    action: str,
    reward: Reward,
    discount: float,
    ) -> float:

    # What is transition?
    # Wait, should we learn it with a model-based approach?
    # Transition(agent stats, foe stats [unknown -- belief])
    # Given a belief, do we know the transition matrix? Yes. But also, we can
    # skip that entirely, we think.
    # Action -> "calculate_action_expectation" which uses our brains and
    # knowledge of probability to "learn" action value [Q(a)]

    # Note - utility of action expectation is the sum of the actor and foe action utilities

    utility = reward.get_reward(agent, foe) + discount*(
        reward.get_reward( # TODO: fix
            action_expectation(agent, foe, agent.act(action))
        )
    )

    return utility
