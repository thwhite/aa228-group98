from action import Action
from foe import Foe


def update_foe_belief(faux_foe: Foe, agent_action, foe_reaction: str):

    # expected_states = agent_action.action_expectation(faux_foe)
    # expected_damage = faux_foe.hp - expected_states

    # print(f'E(damage): {expected_damage}')

    if "RAW" in foe_reaction:
        # @Thomas: Do we also need to update what we think the faux foe's max hp is?
        # What about AC?
        print(foe_reaction)
        faux_foe.hp = (14 - (len(foe_reaction) - 3))*10

    return faux_foe
