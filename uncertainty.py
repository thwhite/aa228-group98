from action import Action
from agent import Agent
from foe import Foe

from dungeonstate import *

def action_expectation(actor, target, action: Action):

    # function not implemented - added the implementation to resolve_action instead. thoughts?

    expected_new_states = state_dict(actor, target)

    return expected_new_states


def update_foe_belief(faux_foe, foe_reaction):

    if foe_reaction[0:2] == "RAW":
        # @Thomas: Do we also need to update what we think the faux foe's max hp is?
        faux_foe.hp = faux_foe.max_hp*(len(foe_reaction) - 3)*0.1

    return faux_foe
