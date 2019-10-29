import sys
sys.path.insert(0, '.')
sys.path.insert(0, '..')
# import create game whatever way works best for you
import create_game
from create_game import CreateGameSettings

import gym


env = gym.make('CreateLevelPush-v0')
env.set_settings(CreateGameSettings(max_num_steps=5))

# Number of tasks
n_tasks = 5

# Iterations per task
n_iters = 2

for task_i in range(n_tasks):
    env.set_task_id(task_i)
    for iter_i in range(n_iters):
        obs = env.reset()

        done = False
        while not done:
            action = env.action_space.sample()
            obs, reward, done, info = env.step(action)
            try:
                env.render('human')
            except:
                pass
