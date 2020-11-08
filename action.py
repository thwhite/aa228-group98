import numpy as np
import random


class Action:

    def __init__(self,
        actor, # Agent or foe
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
        self.target_roll = target_roll
        self.save_modifier = save_modifier
        self.effect = effect
        self.effect_roll = effect_roll
        self.effect_modifier = effect_modifier


    def resolve_action(self, target, rand) -> dict:
        # What is the recipe for an action?
            #     1. Roll dice, add modifiers (probablistic)
            #     2. Compare
            #     3. Roll effect (probablistic)
            #     4. Calculate updates

        new_states = {
            "actor": {**self.actor.states, **{"hp": self.actor.hp}},
            "target": {**target.states, **{"hp": target.hp}}
        }

        if self.effect == "none":
            return new_states

        agent_roll = self.roll(self.attack_roll, rand)
        agent_roll += (self.actor.stats[self.attack_modifier]
            if self.attack_modifier != "none" else 0
        )

        target_roll = self.roll(self.target_roll, rand)
        target_roll += (target.stats[self.save_modifier]
            if self.save_modifier != "none" else 0
        )

        # Technically in some cases it's a strict inequality, but that's too
        # subtle to model right now
        if agent_roll >= target_roll:
            sign = np.sign(self.effect_modifier)

            effect_roll = sign*np.sum([
                self.roll(die, rand)
                for die in self.effect_roll
            ]) + self.effect_modifier

            old_state = new_states["target"][self.effect]
            new_state = old_state - effect_roll

            # States are nonnegative
            new_states["target"][self.effect] = (
                new_state if new_state >= 0 else 0
            )

        return new_states

    def roll(self, roll, rand):
        # returns either a random die roll, or the expected value of that die roll
        if rand == "random":
            return random.randint(1, roll)
        else:
            return int(roll/2)
