from action import Action
from agent import Agent
from foe import Foe

def turn(agent: Agent, agent_policy_step: str, foe: Foe, rand="random"
     ) -> (str, str):
    # Not currently very extensible. Oh well.

    agent_action = agent.act(agent_policy_step)

    new_states = (agent_action.resolve_action(foe) if rand == "random"
        else agent_action.action_expectation(foe)
    )

    if agent_action.target_id == "self":
        agent.update_states(new_states["target"])
    else:
        foe.update_states(new_states["target"])

    foe_action = foe.act(rand)

    new_states = (foe_action.resolve_action(agent) if rand == "random"
        else foe_action.action_expectation(agent)
    )


    if foe_action.target_id == "self":
        foe.update_states(new_states["target"])
    else:
        agent.update_states(new_states["target"])

    foe.decrement_cooldowns()
    foe_reaction = foe.react()

    return (agent_action, foe_reaction)
