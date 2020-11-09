import pandas as pd

from action import Action
from agent import Agent
from foe import Foe
from reward import Reward
from turn import turn

def random_encounter(agent=Agent, foe=Foe, max_turns=int,
    ) -> pd.DataFrame:
    """
    :param agent:
    :param foe:
    :param max_turns:
    :return:
    """

    reward = Reward(agent, foe)
    utility = reward.get_reward(agent, foe)

    # Arrays to hold encounter_stats
    agent_policies = []
    agent_spell_slots = []
    agent_shields = []
    agent_healths = []
    foe_healths = []
    rewards = []

    for i in range(max_turns):

        agent_policy = agent.random_action()

        agent_action, __ = turn(agent, agent_policy, foe)

        utility = reward.get_reward(agent, foe)

        # Collect turn data into encounter_stats
        agent_policies.append(agent_policy)
        agent_spell_slots.append(agent.states["spell slots"])
        agent_shields.append(agent.states["shield"])
        agent_healths.append(agent.hp)
        foe_healths.append(foe.hp)
        rewards.append(utility)

        if agent.hp <= 0 or foe.hp <= 0:
            # end encounter if either dies
            break

    encounter_stats = pd.DataFrame({
        "agent actions": agent_policies,
        "agent spell slots": agent_spell_slots,
        "agent shield": agent_shields,
        "agent health": agent_healths,
        "foe health": foe_healths,
        "reward": rewards,
    })

    return agent, foe, encounter_stats
