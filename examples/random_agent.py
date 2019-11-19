import sys
# Path needs to include the `create_game` folder.
sys.path.insert(0, '.')
sys.path.insert(0, '..')
import create_game
from create_game import CreateGameSettings

import gym


env = gym.make('CreateLevelPush-v0')
env.set_settings(CreateGameSettings(max_num_steps=5))

num_iters = 10

for iter_i in range(num_iters):
    obs = env.reset()

    done = False
    while not done:
        action = env.action_space.sample()
        obs, reward, done, info = env.step(action)
        try:
            env.render('human')
        except:
            pass
