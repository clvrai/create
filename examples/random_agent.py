import sys
sys.path.insert(0, '.')
sys.path.insert(0, '..')
# import create game whatever way works best for you
import create_game

import gym


env = gym.make('CreateLevelPush-v0')

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
