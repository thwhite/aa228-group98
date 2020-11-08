import copy
import numpy as np

from action import Action
from agent import Agent
from dungeonstate import DungeonState
from foe import Foe
from reward import Reward
from uncertainty import action_expectation


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
        utility = Up + __lookahead(agent, foe, action, reward, discount)
        if utility > best_action[1]:
            best_action = (action, utility)

    return best_action


def __lookahead(
    agent: Agent, # Agent and foe represent the full state
    foe: Foe, # This is a faux foe
    action: str, # @Valerie can we rename this policy for clarity, given that we also have a class called action?
    reward: Reward,
    discount: float,
    ) -> float:

    # Note - utility of action is the sum of the actor AND foe action utilities

    utility = reward.get_reward(agent, foe)

    # new_states = action_expectation(agent, foe, agent.act(action))
    new_states = agent.act(action).resolve_action(foe, "expectation")
    agent.update_states(new_states["agent"])
    foe.update_states(new_states["foe"])

    utility += discount*reward.get_reward(agent, foe)

    return utility
