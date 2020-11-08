import copy
import pandas as pd

from action import Action
from agent import Agent
from dungeonstate import *
from foe import Foe
from forward_search import forward_search
from reward import Reward
from uncertainty import update_foe_belief


def encounter(agent=Agent, foe=Foe, max_turns=int,
    # **forward_search_kwargs, **reward_kwargs, # TODO
    ) -> pd.DataFrame:
    """
    TODO: document me!!

    :param agent:
    :param foe:
    :param max_turns:
    :param **forward_search_kwargs:
        - depth: int = 3,
        - discount: float = 0.9
    :param **reward_kwargs:
        - reward_for_kill: float = 1000,
        - penalty_for_dying: float = -1000,
        - agent_hp_bonus: float = 10,
    :return:
    """

    dungeon = DungeonState(agent, foe)
    reward = Reward(agent, foe)
    utility = reward.get_reward(agent, foe)

    faux_foe = Foe() # The belief state of our foe

    for i in range(max_turns):

        agent_action = forward_search(
            # **forward_search_kwargs, # TODO: kwargs
            agent=agent, foe=faux_foe,
            dungeonstate=dungeon,
            reward=reward,
            utility=utility,
        )

        agent, foe, foe_reaction = turn(agent, agent_action, foe)
        faux_foe = update_foe_belief(faux_foe, foe_reaction)
        utility += reward.get_reward(agent, foe)

    encounter_stats = pd.DataFrame() # TODO @Valerie

    return agent, foe, encounter_stats


def turn(agent: Agent, agent_action: Action, foe: Foe
     ) -> (Agent, Foe, float):
     # Not currently very extensible. Oh well.

    action = agent.act(agent_action)
    __update_states(agent, foe, action.resolve_action(foe, "random"))

    action = foe.act()
    __update_states(foe, agent, action.resolve_action(agent, "random"))

    foe.decrement_cooldowns()
    foe_reaction = foe.react()

    return (agent, foe, foe_reaction)


def __update_states(actor, target, new_states: dict):

    actor.update_states(new_states["actor"])
    target.update_states(new_states["target"])
