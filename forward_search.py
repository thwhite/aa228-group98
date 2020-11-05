from reward import Reward

def forward_search(
    depth: int = 3,
    discount: float = 0.9,
    agent: Agent,
    foe: Foe, # We might end up with a belief. How do we do that?
    # MC_policy,
    # forward_search_weight: float = 1,
    ): -> action: Action, reward: float

    return Action(), reward



def __lookahead(
    agent: Agent, # Agent and foe represent the full state
    foe: Foe,
    action: Action,
    reward: Reward, # or is this a Reward object? idk
    discount: float
    ): -> utility: [float]

    # What is transition?
    # Wait, should we learn it with a model-based approach?
    # Transition(agent stats, foe stats [unknown -- belief])
    # Given a belief, do we know the transition matrix? Yes. But also, we can
    # skip that entirely, we think.
    # Action -> "calculate_action_expectation" which uses our brains and
    # knowledge of probability to "learn" action value [Q(a)]

    utility[state] = reward[state] + discount*action_expectation[state, action]

    return utility
