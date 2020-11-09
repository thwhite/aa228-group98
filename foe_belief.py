from action import Action
from foe import Foe


def update_foe_belief(faux_foe: Foe, agent_action, foe_reaction: str):

    expected_states = agent_action.action_expectation(faux_foe)
    expected_damage = faux_foe.hp - expected_states["target"]["hp"]

    print(f'E(damage): {expected_damage}')

    if "RAW" in foe_reaction:
        # @Thomas: Do we also need to update what we think the faux foe's max hp is?
        # What about AC?
        faux_foe.hp = faux_foe.max_hp*(len(foe_reaction) - 3)*0.1

    return faux_foe
