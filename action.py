import numpy as np
import random

from dungeonstate import state_dict

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

    def resolve_action(self) -> new_states: dict:
        # What is the recipe for an action?
            #     1. Roll dice, add modifiers
            #     2. Compare
            #     3. Roll effect
            #     4. Calculate updates

        new_states = {
            'actor': {*actor.states, actor.hp},
            'target': {*target.states, target.hp}
        }

        agent_roll = random.randint(1, self.attack_roll)
        agent_roll += (self.actor.stats[self.modifier_stat]
            if self.modifier_stat is not "none" else 0
        )

        target_roll = random.randint(1, self.target_roll)
        target_roll += (self.target.stats[self.save_stat]
            if self.save_stat is not "none" else 0
        )

        # Technically in some cases it's a strict inequality, but that's too
        # subtle to model right now
        if agent_roll >= target_roll

            effect_roll = np.sum([
                random.randint(1, die)
                for die in self.effect_roll
            ]) + self.effect_modifier

            old_state = new_states['target'][effect]
            new_state = old_state - effect_roll

            # States are nonnegative
            new_states['target'][effect] = new_state if new_state >= 0 else 0

        return new_states
