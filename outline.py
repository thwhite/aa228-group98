def monte_carlo()


def test()


def metrics()


---

class Reward:
    self.reward_for_kill: float = 1000,
    self.penalty_for_dying: float = -1000,
    self.agent_hp_bonus: float = 10,
    self.agents: [Agent] = [Agent()],
    self.foe: Foe = Foe(),

    functions:
        - get_reward(agents: [Agent] = [Agent()], foe: Foe = Foe()) -> reward: float


def branch_and_bound(
    bb_weight: float = 1,
    depth: int = 3,
    discount: float = 0.9,
    agent_kwargs: [kwargs],
    MC_policy,
    foe_kwargs: [kwargs],
    ): -> action: Action, reward: float

    subfunctions:
        - lookahead()


def encounter(
    agents_kwargs: [kwargs],
    policies: [policy],
    foe_kwargs: [kwargs],
    turn_limit: int
    ): -> agents: [Agent], foe: Foe, turn_count: int

    Initiates [agents], foe
        Agent(s) act first? (for now)
    Calls turn(action) <- action pulled from policy
    Updates [agents], foe


def turn(action: Action) -> ?

    agent_action = agent.act(action)
    foe_action = foe.act()
    for action in [actions]
        delta_states = action.resolve_action()
        update agent.states, etc.
        update foe.states, etc.
    foe.decrement_cooldowns()


class Action:
    self.actor
    self.targets
    self.dice_roll
    self.modifier # <-- which modifier to use
    self.effect # <-- which state(s) changes?
    ... etc
    what is the recipe for an action?
        1. roll dice, add modifiers
        2. compare rolls/AC/etc.
        3. roll damage
        4. calculate state updates

    functions:
        - resolve_action() returns delta_states


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
