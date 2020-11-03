def turn(agent, foe, policy):

    actions = []
    actions.append = agent.act(policy)
    actions.append = foe.act()

    for action in actions:
        delta_states = action.resolve_action()
        for j in delta_states:
            for k in delta_states[j]:
                agent.states[k] = delta_states[j][k]

    foe.decrement_cooldowns()
