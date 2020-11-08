import matplotlib.pyplot as plt
import pandas as pd

from agent import Agent
from encounter import encounter
from foe import Foe


bad_guy = Foe()
good_guy = Agent()

good_guy, bad_guy, encounter_stats = encounter(good_guy, bad_guy, 100)

print(encounter_stats["agent health"])

## Note: Valerie moved to test.ipynb here because reasons
