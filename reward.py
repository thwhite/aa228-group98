import numpy as np

from action import Action
from agent import Agent
from foe import Foe

class Reward:

    def __init__(self,
        agent: Agent = Agent(),
        foe: Foe = Foe(),
        reward_for_kill: float = 1000,
        penalty_for_dying: float = -1000,
        agent_hp_bonus: float = 0,
        foe_hp_bonus: float = -0.5,
        ):

        # See numpy.interp
        self.agent_xp = np.arange(start=1, stop=agent.max_hp+1)
        self.reward_per_agent_hp = agent_hp_bonus*self.agent_xp
        self.penalty_for_dying = penalty_for_dying

        self.foe_xp = np.arange(start=1, stop=foe.max_hp+1)
        self.reward_per_foe_hp = foe_hp_bonus*self.foe_xp
        self.reward_for_kill = reward_for_kill

    def get_reward(self, agent: Agent, foe: Foe) -> float:

        r = np.interp(
            x=agent.hp, xp=self.agent_xp, fp=self.reward_per_agent_hp,
            left=self.penalty_for_dying
        )

        return r + np.interp(
            x=foe.hp, xp=self.foe_xp, fp=self.reward_per_foe_hp,
            left=self.reward_for_kill
        )

    # def get_worst_reward(self) -> float:
    #
    #     return self.penalty_for_dying + self.reward_per_foe_hp[-1]
