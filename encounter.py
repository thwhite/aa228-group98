from agent import Agent
from foe import Foe
from turn import turn
from dungeonstate import DungeonState

import copy


def encounter(bb_agent, bb_foe, policy, turn_count, num_runs):
    """
    Note: encounter does NOT modify bb_agent or bb_foe. It just grabs them to make a copy.

    :param bb_agent:
    :param bb_foe:
    :param policy:
    :param turn:
    :param num_runs:
    :return:
    """

    local_agent = copy.deepcopy(bb_agent)
    local_foe = copy.deepcopy(bb_foe)  # a 'focal', if you will
    dungeon = DungeonState(local_agent, local_foe)

    for i in range(turn_count, num_runs):
        idx = dungeon.agent_foe_to_index(local_agent, local_foe)
        turn(local_agent, local_foe, policy[idx])

    return local_agent, local_foe

# @Thomas
# TODO: This is actually just the test function now
#  - Stuff reward in here
# TODO: also throw in search kwargs (depth, discount, other stuff)

# @Valerie
# Make it so encounter passes out data for metric, etc.
# And then metrics runs a ton of encounters with different agents and foes and
# other hyperparameters and then graphs the results all pretty
