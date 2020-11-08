import copy
import pandas as pd

from action import Action
from agent import Agent
from dungeonstate import *
from foe import Foe
from forward_search import forward_search
from reward import Reward

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

    for turn in range(max_turns):

        # How's this get used again?
        idx = dungeon.agent_foe_to_index(agent, foe)

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

    actions = {
        "agent": {"actor": agent, "action": agent.act(agent_action)},
        "foe": {"actor": foe, "action": foe.act()},
    }

    for actor_name, action in actions.items():
        new_states = action["action"].resolve_action()

        actor.states = actor_state(actor_name, new_states)
        action["actor"].hp = new_states[actor_name]["hp"]

    foe.decrement_cooldowns()
    foe_reaction = foe.react()

    return (agent, foe, foe_reaction)
