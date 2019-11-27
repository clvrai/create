import sys
# Path needs to include the `create_game` folder.
sys.path.insert(0, '.')
sys.path.insert(0, '..')
import create_game
from create_game import CreateGameSettings
from create_game import GET_ACTIONS

import gym


env = gym.make('CreateLevelPush-v0')
env.set_settings(CreateGameSettings(max_num_steps=5))

num_iters = 10


for iter_i in range(num_iters):
    obs = env.reset()
    done = False
    while not done:
        # Get available action set for current setting
        aval, tool_list = env.get_aval_actions()
        # The following way can be used with multiprocessing environments
        # where `get_aval_actions` is not accessible:
        # _, _, _, info = env.step(GET_ACTIONS)
        # aval, tool_list = info['aval'], info['tool_list']

        # Replace with `your_policy(obs, aval, tool_list)`
        action = env.action_space.sample()

        obs, reward, done, info = env.step(action)
        try:
            env.render('human')
        except:
            pass

    obs = env.reset()
