from agent import Agent
from dungeonstate import *
from encounter import encounter
from foe import Foe


bad_guy = Foe()
good_guy = Agent()
dungeon_state = DungeonState(good_guy, bad_guy)

encounter(good_guy, bad_guy, 10)
