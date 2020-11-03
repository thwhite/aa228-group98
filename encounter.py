from agent import Agent
from foe import Foe
from turn import turn


def encounter(agent_kwargs, foe_kwargs, policy, turn, num_runs):

    agent = Agent() # need to init with the default stats
    foe = Foe()

    for i in range(turn, num_runs):
        turn(agent, foe, policy[i])

    return agent, foe # I need to check if this is actually how we discussed this?
