import sys
sys.path.insert(0, '.')
sys.path.insert(0, '..')
# import create game whatever way works best for you
import create_game
from create_game import CreateGameSettings
import gym
from create_game import UseSplit
import numpy as np




def gen_action_set(settings, tool_gen, allowed_actions, rng):
    return np.random.choice(allowed_actions, settings.action_set_size, replace=False)

use_settings = CreateGameSettings(
    max_num_steps=5,
    action_random_sample=True,
    action_set_size=50,
    validation_ratio=0.5,
    split_type=UseSplit.TEST,
    action_sample_fn=gen_action_set)

eval_lvls = ['CreateLevelPush-v0', 'CreateLevelNavigate-v0', 'CreateLevelObstacle-v0']
NUM_EVAL_EPISODES = 10



for eval_lvl in eval_lvls:
    env = gym.make(eval_lvl)
    env.set_settings(use_settings)

    num_goal_hit = 0.0

    for eval_episode_i in range(NUM_EVAL_EPISODES):
        obs = env.reset()
        ep_reward = 0.0
        done = False
        while not done:
            action = env.action_space.sample()
            obs, reward, done, info = env.step(action)
            ep_reward += reward

        num_goal_hit += info['ep_goal_hit']

    avg_num_goal_hit = num_goal_hit / NUM_EVAL_EPISODES

    print('%s average goal hit (%%): %.4f%%' % (eval_lvl, avg_num_goal_hit))


