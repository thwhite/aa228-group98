import numpy as np

class Reward:

    def __init__(self,
    reward_for_kill: float = 1000,
    penalty_for_dying: float = -1000,
    agent_hp_bonus: float = 10,
    agents: [Agent] = [Agent()],
    foe: Foe = Foe(),
    ):
        reward_per_agent_hp = {}
        for agent in agents
            reward_per_agent_hp{agent} = agent_hp_bonus*np.arange(
                start=0, stop=agent.max_hp
            )
            reward_per_agent_hp{agent}[0] = penalty_for_dying

        reward_per_foe_hp = [0]*foe.max_hp
        reward_per_foe_hp[0] = reward_for_kill

        self.reward_per_agent_hp = reward_per_agent_hp
        self.reward_per_foe_hp = reward_per_foe_hp


    def get_reward(self, agents: [Agent], foe: Foe) -> reward: float:

        reward = sum([
            self.reward_per_agent_hp{agent}[agent.hp]
            for agent in agents
        ]) # This line might not work; we'll see

        reward = reward + self.reward_per_foe_hp[foe.hp]

        return reward
