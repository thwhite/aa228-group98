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
    forward_search_and_reward_kwargs = {},
    ) -> pd.DataFrame:
    """
    TODO: document me!!

    :param agent:
    :param foe:
    :param max_turns:
    :param forward_search_and_reward_kwargs:
        - forward_search_kwargs:
            - depth: int = 3,
            - discount: float = 0.9
        - reward_kwargs:
            - reward_for_kill: float = 1000,
            - penalty_for_dying: float = -1000,
            - agent_hp_bonus: float = 2,
    :return:
    """

    # Handle kwargs
    forward_search_kwargs, reward_kwargs = __get_kwargs(
        forward_search_and_reward_kwargs
    )

    dungeon = DungeonState(agent, foe)
    reward = Reward(agent, foe, ** reward_kwargs)
    utility = reward.get_reward(agent, foe)

    faux_foe = Foe()  # The belief state of our foe

    # Arrays to hold encounter_stats
    agent_actions = []
    agent_healths = []
    foe_healths = []
    foe_reactions = []
    faux_foe_healths = []
    forward_search_utilities = []
    rewards = []

    for i in range(max_turns):

        agent_action, forward_search_utility = forward_search(
            agent=agent, foe=faux_foe,
            dungeonstate=dungeon,
            reward=reward,
            utility=utility,
            **forward_search_kwargs
        )

        agent, foe, foe_reaction = turn(agent, agent_action, foe)
        faux_foe = update_foe_belief(faux_foe, foe_reaction)
        turn_reward = reward.get_reward(agent, foe)
        utility += turn_reward

        # Collect turn data into encounter_stats
        agent_actions.append(agent_action)
        agent_healths.append(agent.hp)
        foe_healths.append(foe.hp)
        foe_reactions.append(foe_reaction)
        faux_foe_healths.append(faux_foe.hp)
        forward_search_utilities.append(forward_search_utility)
        rewards.append(turn_reward)

        if agent.hp <= 0 or foe.hp <= 0:
            # end encounter if either dies
            break

    encounter_stats = pd.DataFrame({
        "agent actions": agent_actions,
        "agent health": agent_healths,
        "foe health": foe_healths,
        "foe reactions": foe_reactions,
        "faux foe health": faux_foe_healths,
        "forward search utility": forward_search_utilities,
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

def __get_kwargs(forward_search_and_reward_kwargs: dict) -> (dict, dict):

    forward_search_kwargs = {}
    reward_kwargs = {}

    for key, kwargs in forward_search_and_reward_kwargs.items():
        if key == "forward_search":
            forward_search_kwargs = kwargs
        elif key == "reward":
            reward_kwargs = kwargs

    return (forward_search_kwargs, reward_kwargs)
