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


def encounter(
    agent_kwargs: kwargs,
    policy: [Action],
    foe_kwargs: kwargs,
    turn_limit: int
    ): -> agent: Agent, foe: Foe, turn_count: int

    Initiates Agent, foe
        Agent acts first? (for now)
    Calls turn(action) <- action pulled from policy
    Updates agent, foe


def turn(action: Action) -> ?

    agent_action = agent.act(action)
    foe_action = foe.act()
    for action in [actions]
        delta_states = action.resolve_action()
        update agent.states, etc.
        update foe.states, etc.
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
    ):

    functions:
        - resolve_action() returns delta_states
        What is the recipe for an action?
            1. roll dice, add modifiers
            2. compare rolls/AC/etc.
            3. roll damage
            4. calculate state updates


class Agent:
    self.name: str
    self.max_hp: int
    self.hp: int
    self.stats: [int] # length 6
    self.states: dict(AC, protections, spell_slots)
    self.actions: dict(action: availability)

    functions:
        - act(action) returns action object


class Foe:
    self.max_hp: int
    self.hp: int
    self.stats: [int] # length 6
    self.states: dict(AC, protections, debuffs, cooldowns)
    self.actions: dict(action: availability)

    functions:
        - act() returns action object
        - decrement_cooldowns()


--- scratch/notes ---

# define an array states, give each state some index, function maps state to idx and vice versa
# repeat for actions
# policy: array where index is state index, value is action index
#
#
# class DungeonsAndDragonsMDP:
#
# def DungeonState: # RECALL EXPONENTIAL GROWTH OF STATE-SPACE
#     def __init__(self,...):
#         agent_hp
#         agent_ac
#         ...
#         foe_hp
#         foe_ac
#
# def state_to_index(self, state):
#     idx = 10*state.hp + 10*state.ac
#     return idx
#
# def index_to_state(self,idx):
#     hp = np.mod(idx,self.MAX_HP) #
#     ac = ....
#     return State(hp,ac)
