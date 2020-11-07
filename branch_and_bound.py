import reward

def branch_and_bound(
    depth: int = 3,
    discount: float = 0.9,
    agent: Agent,
    foe: Foe, # Our faux Foe
    # MC_policy,
    # bb_weight: float = 1,
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



### Scratch / Notes ###

# Approach: Do forward search instead now. See if we can upgrade to b&b later.
#
# To do: Update ourselves on course content.
#
# Question: Is b&b actully helpful? Or should we just use forward search
#
# Lower bound (for value function)-> We die.
# Can we ever calculate a higher lower bound than that?
# It seems like that's what we need to make b&b helpful.
#     - Max damage we can take = max damage we've taken
#
# Upper bound (action value function) -> We kill the foe, lose no more hp.
#     - What max damage can we do? Is it greater than the foe's hp?
#
# What is our "expert knowledge" that allows us to bound?
# Are soft bounds based on beliefs okay?
