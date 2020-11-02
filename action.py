
import random

class Action:

    def __init__(self,
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

        self.actor = actor
        self.target = target
        self.attack_roll = attack_roll
        self.modifier_stat = modifier_stat
        self.target_roll = target_roll
        self.save_stat = save_stat
        self.effect = effect
        self.effect_roll = effect_roll
        self.effect_modifier = effect_modifier

    def resolve_action(self) -> delta_states: dict:
        # what is the recipe for an action?
            #     1. Roll dice, add modifiers
            #     2. Compare
            #     3. Roll effect
            #     4. Calculate updates

        agent_roll = random.randint(1, self.attack_roll)
        agent_roll += (self.actor.stats[self.modifier_stat]
            if self.modifier_stat is not "none" else 0
        )

        target_roll = random.randint(1, self.target_roll)
        target_roll += (self.target.stats[self.save_stat]
            if self.save_stat is not "none" else 0
        )

        # attack = random.randint(1, self.attack_roll)
        # if attack >= self.target.states["AC"]:
        #     defend = self.target.stats["save_stat"] # This format is wrong right now, will figure later
        #     if random.randint(1, defend) <= save_stat:
        #         # how to handle actions. is it true that every action increments or decrements a stat of some form?


        delta_states = {"hp": 0}

        return delta_states
