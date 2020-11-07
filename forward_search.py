from reward import Reward
from action import Action
from agent import Agent
from foe import Foe
from dungeonstate import DungeonState
import numpy as np

# TODO: Move agent and foe copying into here

# Faux foe update here? @Thomas
# I changed my mind and think it should be here instead of turn bc this is where
# we hold our simulated foes/agents and turn holds our actual foe/agent.
# -- Valerie
# We need a model of reactions -> states.

def forward_search(
    depth: int = 3,
    discount: float = 0.9,
    agent: Agent,
    foe: Foe, # Faux foe?
    dungeonstate: DungeonState
    U = utility (float)
    # MC_policy,
    # forward_search_weight: float = 1
)
    idx = dungeonstate.agent_foe_to_index(agent, foe)

    if depth <= 0:
        return (Action(agent), U)

    best_action = (Action(agent), - np.inf)
    Up = forward_search(depth - 1, discount, agent, foe, dungeonstate, U)[1]
    for a in agent.get_available_actions():




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

    # Note - utility of action expectation is the sum of the actor and foe action utilities


    utility[state] = reward[state] + discount*action_expectation[state, action]

    return utility
