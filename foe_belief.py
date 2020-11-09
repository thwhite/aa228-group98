from action import Action
from foe import Foe


def update_foe_belief(faux_foe: Foe, foe_reaction: str):

    if "RAW" in foe_reaction:

        print(foe_reaction)
        faux_foe.hp = (14 - (len(foe_reaction) - 3))*10

    return faux_foe
