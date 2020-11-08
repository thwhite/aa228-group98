from action import Action
from agent import Agent
from foe import Foe

from dungeonstate import *

def action_expectation(actor, target, action: Action) -> dict:

      expected_new_states = state_dict(actor, target)

      return expected_new_states # Todo
