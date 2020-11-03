def monte_carlo()


def test()


def metrics()


---
# Note: commented out means done(ish)

# class Reward:
#     self.reward_for_kill: float = 1000,
#     self.penalty_for_dying: float = -1000,
#     self.agent_hp_bonus: float = 10,
#     self.agent: Agent = Agent(),
#     self.foe: Foe = Foe(),
#
#     functions:
#         - get_reward(agent: Agent = Agent(), foe: Foe = Foe()) -> reward: float


def branch_and_bound(
    bb_weight: float = 1,
    depth: int = 3,
    discount: float = 0.9,
    agent_kwargs: kwargs,
    MC_policy,
    foe_kwargs: kwargs,
    ): -> action: Action, reward: float

    subfunctions:
        - lookahead()


def encounter(bb_agent, bb_foe, policy, turn_count, num_runs

    "Copies" Agent, foe

    for i in range(turn_count, num_runs):
        turn(agent, foe, policy[idx]) # policy index comes from state
    return agent, foe


def turn(agent, foe, policy) -> ?

    # do actions
    actions.append = agent.act(policy)
    actions.append = foe.act()

    # set values of the
    new_states = action.resolve_action()
    agent.states = new states

    foe.decrement_cooldowns()


class Action:
    actor, # Agent or foe
    target, # Agent or foe
    attack_roll: int = 20, # If no roll (such as don/doff shield), pass 1
    modifier_stat: str, # If no modifier, pass "none"
    target_roll: int = 1, # Similar to attack roll
    save_stat: str, # If no save, pass "none"
    effect: str, # <-- which state(s) changes?
    effect_roll: [int] = [1],
    # positive -> subtract from current state (as in damage);
    # negative -> add (as in healing)
    effect_modifier: int = 0
    ): -> new_states: {actor: {actor.states}, target: {target.states}}

    functions:
        - resolve_action() returns delta_states
        What is the recipe for an action?
            1. roll dice, add modifiers
            2. compare rolls/AC/etc.
            3. roll damage
            4. calculate state updates


class DungeonState: # RECALL EXPONENTIAL GROWTH OF STATE-SPACE
    agent: Agent
    foe: Foe

    functions:
        - state_to_index(self)
        - index_to_state(self, index)


class Agent:
    self.name: str
    self.max_hp: int
    self.hp: int
    self.stats: [int] # length 6
    self.states: dict(AC, protections, spell_slots)
    self.actions: dict(action: availability)

    functions:
        - get_available_actions()  # tells you what actions are possible based on state info
        - act(action) returns action object


class Foe:
    self.max_hp: int
    self.hp: int
    self.stats: [int] # length 6
    self.states: dict(AC, protections, debuffs, cooldowns)

    functions:
        - get_available_actions() # tells you what actions are possible based on state info
        - act() returns action object
        - decrement_cooldowns()


--- scratch/notes ---
