import copy
import pandas as pd

from action import Action
from agent import Agent
from foe import Foe
from forward_search import *
from reward import Reward
from foe_belief import update_foe_belief
from turn import turn




def monte_carlo_encounter(agent=Agent, foe=Foe, max_turns=int,
    forward_search_and_reward_kwargs = {},
    ) -> pd.DataFrame:


    # Handle kwargs
    forward_search_kwargs, reward_kwargs = __get_kwargs(
        forward_search_and_reward_kwargs
    )

    reward = Reward(agent, foe, **reward_kwargs)
    utility = reward.get_reward(agent, foe)

    faux_foe = Foe()  # The belief state of our foe

    # Arrays to hold encounter_stats
    agent_policies = []
    agent_spell_slots = []
    agent_shields = []
    agent_healths = []
    foe_healths = []
    foe_reactions = []
    faux_foe_healths = []
    forward_search_utilities = []
    rewards = []

    for i in range(max_turns):
        agent_policy = random.choice(agent.get_available_actions())

        agent_action, foe_reaction = turn(agent, agent_policy, foe)

        faux_foe = update_foe_belief(faux_foe, foe_reaction)
        utility += reward.get_reward(agent, foe)

        # Collect turn data into encounter_stats
        agent_policies.append(agent_policy)
        agent_spell_slots.append(agent.states["spell slots"])
        agent_shields.append(agent.states["shield"])
        agent_healths.append(agent.hp)
        foe_healths.append(foe.hp)
        foe_reactions.append(foe_reaction)
        faux_foe_healths.append(faux_foe.hp)
        # forward_search_utilities.append(forward_search_utility)
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
        "foe reactions": foe_reactions,
        "faux foe health": faux_foe_healths,
        # "forward search utility": forward_search_utilities,
        "utility": rewards,
    })

    return agent, foe, encounter_stats


def __get_kwargs(forward_search_and_reward_kwargs: dict) -> (dict, dict):

    forward_search_kwargs = {}
    reward_kwargs = {}

    for key, kwargs in forward_search_and_reward_kwargs.items():
        if key == "forward_search":
            forward_search_kwargs = kwargs
        elif key == "reward":
            reward_kwargs = kwargs

    return (forward_search_kwargs, reward_kwargs)


bad_guy = Foe()
good_guy = Agent()
num_searches = 100

best_outcome = pd.DataFrame()
max_util = 0

for i in range(num_searches):
    good_guy, bad_guy, encounter_stats = monte_carlo_encounter(good_guy, bad_guy, 100,
            forward_search_and_reward_kwargs = {
           "forward_search": {"depth": 25},
           "reward": {"penalty_for_dying": -5000},
       }
    )
    util = encounter_stats.get("utility")[int(len(encounter_stats.get("utility"))) - 1]
    if util < max_util:
        print("i replaced dataframe")
        best_outcome = encounter_stats

# print(best_outcome.info)