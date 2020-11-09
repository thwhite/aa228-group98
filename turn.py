from action import Action
from agent import Agent
from foe import Foe

def turn(agent: Agent, agent_policy_step: str, foe: Foe
     ) -> (str, str):
    # Not currently very extensible. Oh well.

    agent_action = agent.act(agent_policy_step)
    __update_states(agent, foe, agent_action.resolve_action(foe))

    foe_action = foe.act()
    __update_states(foe, agent, foe_action.resolve_action(agent))

    foe.decrement_cooldowns()
    foe_reaction = foe.react()

    return (agent_action, foe_reaction)

def __update_states(actor, target, new_states: dict):

    actor.update_states(new_states["actor"])
    target.update_states(new_states["target"])
