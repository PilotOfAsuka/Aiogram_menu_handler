from modules.json_config import load_json, save_in_json
from CONSTANTS import user_states_file

user_states = load_json(user_states_file)


def set_state(user_id, state):
    user_states[user_id] = state
    save_in_json(user_states, user_states_file)
    pass
