def monte_carlo()


def test()


def metrics()


---
policy=list of actions ???
where are agent(s), foe(s) initiated? MC/Test?


def reward([characters])
    - note: can use type(character) to determine positive or negative reward
    calculate the reward??

def branch_and_bound(depth=int, [agents], foe)
    - Am I recursive? If so, Valerie's gonna be sad

    subfunctions:
        - lookahead

    return policy?



def encounter([agents], foe)

    return ?


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
    self.agent
    self.foe
    self.dice_roll
    self.modifier
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
    self.hp = int
    self.stats = [6 ints]
    self.states = dict(AC, protections, spell_slots)
    self.actions = dict(action: availability)

    functions:
        - act(action) returns action object


class foe()
    self.hp = int
    self.stats = [6 ints]
    self.states = dict(AC, protections, debuffs, cooldowns)
    self.actions = dict(action: availability)

    functions:
        - act() returns action object
        - decrement_cooldowns()
