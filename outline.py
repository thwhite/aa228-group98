def monte_carlo()


def test()


def metrics()


---

policy=dict(action: dict(state: value)) <-- Ask @ OH


def reward([agents], foe, turn_count)

    reward_for_dead_foe, penalty_for_dying, penalty_for_hp_loss
    if-then statements

    return reward


def branch_and_bound(bb_weight, depth=int, [agents_kwargs], [policies], foe_kwargs)
    - Am I recursive? If so, Valerie's gonna be sad [Yes]

    subfunctions:
        - lookahead

    return [policies], reward


def encounter([agents_kwargs], [policies], foe_kwargs, turn_limit)
    initiates [agents], foe
    - note: for now, agent(s) act first?

    calls turn(action) <- action pulled from policy
    update [agents], foe

    return [agents], foe, turn_count


def turn(action)

    agent_action = agent.act(action)
    foe_action = foe.act()
    for action in [actions]
        delta_states = action.resolve_action()
        update agent.states, etc.
        update foe.states, etc.
    foe.decrement_cooldowns()

    return ?


class action()
    self.actor
    self.targets
    self.dice_roll
    self.modifier <-- which
    self.effect <-- which state(s) changes?
    ... etc
    what is the recipe for an action?
        1. roll dice, add modifiers
        2. compare rolls/AC/etc.
        3. roll damage
        4. calculate state updates

    functions:
        - resolve_action() returns delta_states


class agent()
    self.max_hp = int
    self.hp = int
    self.stats = [6 ints]
    self.states = dict(AC, protections, spell_slots)
    self.actions = dict(action: availability)

    functions:
        - act(action) returns action object


class foe()
    self.max_hp = int
    self.hp = int
    self.stats = [6 ints]
    self.states = dict(AC, protections, debuffs, cooldowns)
    self.actions = dict(action: availability)

    functions:
        - act() returns action object
        - decrement_cooldowns()
