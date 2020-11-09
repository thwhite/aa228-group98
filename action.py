import numpy as np
from scipy.stats import randint
import random


class Action:

    def __init__(self,
        actor, # Agent or foe
        target_id: str = "other guy", # Tells us whether to target ourselves
        attack_roll: int = 1, # Default: No roll
        attack_modifier: str = "none", # Default: No modifier
        target_roll: int = 1, # Default: No roll
        save_modifier: str = "none", # Default: No save
        effect: str = "none", # Which state changes? Default: No state change
        effect_roll: int = 1, # Default: No roll
        # Positive -> Subtract from current state (as in damage);
        # Negative -> Add (as in healing)
        # Default: No modifier
        effect_modifier: int = 0
        ):

        self.actor = actor
        self.attack_roll = attack_roll
        self.attack_modifier = attack_modifier

        self.target_id = target_id

        self.target_roll = target_roll
        self.save_modifier = save_modifier
        self.effect = effect
        self.effect_roll = effect_roll
        self.effect_modifier = effect_modifier


    def resolve_action(self, other_guy) -> dict:
        # What is the recipe for an action?
            #     1. Roll dice, add modifiers (probablistic)
            #     2. Compare
            #     3. Roll effect (probablistic)
            #     4. Calculate updates

        if self.target_id == "self":
            target = self.actor
        else:
            target = other_guy

        new_states = {
            "actor": {**self.actor.states, **{"hp": self.actor.hp}},
            "target": {**target.states, **{"hp": target.hp}}
        }

        if self.effect == "none":
            return new_states

        agent_roll = random.randint(1, self.attack_roll)
        agent_roll += (self.actor.stats[self.attack_modifier]
            if self.attack_modifier != "none" else 0
        )

        target_roll = random.randint(1, self.target_roll)
        target_roll += (target.stats[self.save_modifier]
            if self.save_modifier != "none" else 0
        )

        # Technically in some cases it's a strict inequality, but that's too
        # subtle to model right now
        if agent_roll >= target_roll:
            if self.effect_modifier == 0:
                sign = 1
            else:
                sign = np.sign(self.effect_modifier)

            effect_roll = sign*random.randint(1, self.effect_roll) \
            + self.effect_modifier

            old_state = new_states["target"][self.effect]
            new_state = old_state - effect_roll

            # Cannot heal above max hp
            if self.effect == "hp":
                new_state = target.max_hp \
                    if new_state > target.max_hp else new_state

            # States are nonnegative
            new_states["target"][self.effect] = (
                new_state if new_state >= 0 else 0
            )

        return new_states

    def action_expectation(self, target) -> int:
        # What is expectation of an action? P(damage)*E(damage)

        states = {
            "actor": {**self.actor.states, **{"hp": self.actor.hp}},
            "target": {**target.states, **{"hp": target.hp}}
        }

        if self.effect != "hp":
            return states

        add_to_roll = (
            self.actor.stats[self.attack_modifier]
            if self.attack_modifier != "none" else 0
        )

        p_damage = randint(
            add_to_roll, add_to_roll + self.attack_roll
        ).sf(target.stats["AC"]) # survival function = 1 - cdf

        e_damage = randint(
            self.effect_modifier, self.effect_modifier + self.effect_roll
        ).expect()

        print(f'{self.actor} -> {target}')
        print(f'{self.effect} p: {p_damage}, e: {e_damage}')

        states["target"]["hp"] = states["target"]["hp"] - p_damage*e_damage

        return states
