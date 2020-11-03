from agent import Agent
from foe import Foe
from turn import turn
import copy
from DungeonsAndDragonsMDP import DungeonState


def encounter(bb_agent, bb_foe, policy, turn, num_runs):
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
    local_foe = copy.deepcopy(bb_foe) # a 'focal', if you will
    dungeon = DungeonState(local_agent, local_foe)

    for i in range(turn, num_runs):
        idx = dungeon.state_to_index(local_agent, local_foe)
        turn(local_agent, local_foe, policy[idx], dungeon)

    return local_agent, local_foe
