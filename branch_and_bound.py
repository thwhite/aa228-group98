import reward

def branch_and_bound(
    bb_weight: float = 1,
    depth: int = 3,
    discount: float = 0.9,
    agent: Agent,
    # MC_policy,
    foe: Foe,
    ): -> action: Action, reward: float

    return Action(), reward



def __lookahead(
    hp: Agent.hp,
    state: Agent.states,
    action: Action,
    # utility: float, # so I think because U(s), from just the state we should
    # be able to calculate this, and we don't need to pass it
    reward: float, # or is this a Reward object? idk
    discount: float
    ): -> utility: float

    utility = reward + discount*sum(transition*utility)
    # Okay, so these need to be defined better
    return utility
