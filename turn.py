def turn(agent, foe, policy, dungeon):

    actions = []
    actions.append = agent.act(policy)
    actions.append = foe.act()

    for action in actions:
        # Primary note: if we're going to resolve these abstractly, need a sense of the target to exit this.
        # Can delta_states be of length greater than one?
        # Strongly depends on structure of delta_states

        delta_states = action.resolve_action()
        target = delta_states.target()
        for i in len(delta_states.values):
            target.state[delta_states[i].key] = delta_states[i].value

    foe.decrement_cooldowns()




