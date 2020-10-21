def monte_carlo()


def test()


def metrics()


---
policy=list of actions ???


def reward(characters)
    - note: can use type(character) to determine positive or negative reward
    calculate the reward??

def branch_and_bound()


def encounter()


def turn(action)

    agent_action = agent.act(action)
    foe_action = foe.act()
    for action in action_objects
        delta_states = action.resolve_action()
        update agent.states, etc.
        update foe.states, etc.
    foe.decrement_cooldowns()


class action_object (todo: better name please!)
    self.dice_roll
    self... etc
    what is the recipe for an action?
        1. roll die, add modifier
        2. ...

    functions:
        - resolve_action() returns delta_states


class agent()
    self.hp = int
    self.stats = list of 6 ints
    self.states = dict(AC, protections, spell_slots)
    self.actions = dict(action: availability)

    functions:
        - act(action) returns action object


class foe()
    self.hp = int
    self.stats = 6x1 array
    self.states = dict(AC, protections, debuffs, cooldowns)
    self.actions = dict(action: availability)

    functions:
        - act() returns action object
        - decrement_cooldowns()
