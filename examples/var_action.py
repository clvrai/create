import sys
# Path needs to include the `create_game` folder.
sys.path.insert(0, '.')
sys.path.insert(0, '..')
import create_game
from create_game import CreateGameSettings
from create_game import GET_AVAL_ACTIONS

import gym


env = gym.make('CreateLevelPush-v0')
env.set_settings(CreateGameSettings(max_num_steps=5))

num_iters = 10


for iter_i in range(num_iters):
    obs = env.reset()
    done = False
    while not done:

        aval = env.get_aval_actions()
        # This would also work.
        # _, _, _, info = env.step(GET_AVAL_ACTIONS)
        # aval = info['aval']
        # and could be used for multiprocessing environments
        # where `get_aval_actions` is not accessible.

        action = env.action_space.sample()
        obs, reward, done, info = env.step(action)
        try:
            env.render('human')
        except:
            pass

    # The available actions for the next episode are already in `info`.
    obs = env.reset()
