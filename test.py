import pandas as pd

from agent import Agent
from encounter import encounter
from foe import Foe


bad_guy = Foe()
good_guy = Agent()

# good_guy, bad_guy, encounter_stats = encounter(good_guy, bad_guy, 100)

good_guy, bad_guy, encounter_stats = encounter(good_guy, bad_guy, 100,
   forward_search_and_reward_kwargs = {
       "forward_search": {"depth": 25},
       "reward": {"penalty_for_dying": -5000},
   }
)

## Note: Valerie moved plotting to test.ipynb here because reasons
