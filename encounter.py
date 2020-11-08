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

    faux_foe = Foe()  # The belief state of our foe

    # Arrays to hold encounter_stats
    agent_actions = []
    agent_healths = []
    foe_healths = []
    faux_foe_healths = []
    forward_search_utilities = []
    rewards = []

    # TODO: foe reactions and faux foe belief state @Valerie

    for i in range(max_turns):

        agent_action, forward_search_utility = forward_search(
            # **forward_search_kwargs, # TODO: kwargs
            agent=agent, foe=faux_foe,
            dungeonstate=dungeon,
            reward=reward,
            utility=utility,
        )

        agent, foe, foe_reaction = turn(agent, agent_action, foe)
        faux_foe = update_foe_belief(faux_foe, foe_reaction)
        turn_reward = reward.get_reward(agent, foe)
        utility += turn_reward

        # Collect turn data into encounter_stats
        agent_actions.append(agent_action)
        agent_healths.append(agent.hp)
        foe_healths.append(foe.hp)
        faux_foe_healths.append(faux_foe.hp)
        forward_search_utilities.append(forward_search_utility)
        rewards.append(turn_reward)

    encounter_stats = pd.DataFrame({
        "agent actions": agent_actions,
        "agent health": agent_healths,
        "foe health": foe_healths,
        "faux foe health": faux_foe_healths,
        "forward search utilities": forward_search_utilities,
        "reward": rewards,
    })

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
