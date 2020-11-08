from agent import Agent
from dungeonstate import *
from encounter import encounter
from foe import Foe


bad_guy = Foe()
good_guy = Agent()
dungeon_state = DungeonState(good_guy, bad_guy)

encounter(good_guy, bad_guy, 10)

## -- ##
"""
print(f'Agent states: {good_guy.states}, hp: {good_guy.hp}')
print(f'Foe states: {bad_guy.states}, hp: {bad_guy.hp}')

initial_state_idx = dungeon_state.agent_foe_to_index(good_guy, bad_guy)
print(f'Initial state idx: {initial_state_idx}')
initial_states = dungeon_state.index_to_states(initial_state_idx)
print(f'Initial states: {initial_states}')

print('Lights, camera... action!!!')
doff = good_guy.act("toggle_shield")
final_states = doff.resolve_action(good_guy)
# Is this how the agent/foe get updated?
# Turns out this doesn't actually do anything right now because doff doesn't
# change the states, but it's nice to have this worked out

good_guy.states = actor_state("actor", final_states)
good_guy.hp = final_states["actor"]["hp"]

final_states = state_dict(good_guy, bad_guy)
print(f'Final states: {final_states}')

final_state_idx = dungeon_state.state_to_index(final_states)
print(f'Final state idx: {final_state_idx}')

final_states = dungeon_state.index_to_states(final_state_idx)
print(f'Final states, converted back from state idx: {final_states}')
"""
