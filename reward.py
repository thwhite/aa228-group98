import numpy as np

class Reward:

    def __init__(self,
    reward_for_kill: float = 1000,
    penalty_for_dying: float = -1000,
    agent_hp_bonus: float = 10,
    agent: Agent = Agent(),
    foe: Foe = Foe(),
    ):

        reward_per_agent_hp = agent_hp_bonus*np.arange(
                start=0, stop=agent.max_hp
        )
        reward_per_agent_hp[0] = penalty_for_dying

        reward_per_foe_hp = [0]*foe.max_hp
        reward_per_foe_hp[0] = reward_for_kill

        self.reward_per_agent_hp = reward_per_agent_hp
        self.reward_per_foe_hp = reward_per_foe_hp


    def get_reward(self, agent: Agent, foe: Foe) -> reward: float:

        return (
            self.reward_per_agent_hp[agent.hp]
            + self.reward_per_foe_hp[foe.hp]
        )
