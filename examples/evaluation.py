import sys
# Path needs to include the `create_game` folder.
sys.path.insert(0, '.')
sys.path.insert(0, '..')
from create_game import UseSplit
from create_game import CreateGameSettings
from create_game import GET_ACTIONS, GET_TOOL_LIST


import gym
import numpy as np


def gen_action_set(settings, tool_gen, allowed_actions, rng):
    # Change the sampling strategy here. Our paper had a smart sampling
    # strategy using k-means and our learned action embeddings.
    return np.random.choice(allowed_actions, settings.action_set_size, replace=False)


# Settings used in our paper across all three environments. This is evaluating
# on the test set of actions. The validation split of 0.5 uses half of the
# evaluation split for testing, which is also what was used in our paper.
use_settings = CreateGameSettings(
    max_num_steps=30,
    action_random_sample=True,
    action_set_size=50,
    validation_ratio=0.5,
    split_type=UseSplit.TEST,
    action_sample_fn=gen_action_set)

eval_lvls = ['CreateLevelPush-v0',
             'CreateLevelNavigate-v0', 'CreateLevelObstacle-v0']

# Our paper evaluated over 3200 episodes. 100 episodes across 32 parallel workers
NUM_EVAL_EPISODES = 100*32

for eval_lvl in eval_lvls:
    env = gym.make(eval_lvl)
    env.set_settings(use_settings)

    tool_list = env.get_tool_list() # Alternatively, use env.step(GET_TOOL_LIST)

    num_goal_hit = 0.0

    obs = env.reset()

    for eval_episode_i in range(NUM_EVAL_EPISODES):
        obs = env.reset()
        ep_reward = 0.0
        done = False
        while not done:
            aval = env.get_aval_actions()
            # The following way can be used with multiprocessing environments
            # where `get_aval_actions` is not accessible:
            # _, _, _, info = env.step(GET_ACTIONS)
            # aval = info['aval']

            '''
                # Get the action from your policy
                action = your_policy.get_action(obs, aval, tool_list)
            '''
            action = env.action_space.sample()
            
            obs, reward, done, info = env.step(action)
            ep_reward += reward
        obs = env.reset()

        num_goal_hit += info['ep_goal_hit']

    avg_num_goal_hit = num_goal_hit / NUM_EVAL_EPISODES

    print('%s average goal hit (%%): %.4f%%' % (eval_lvl, avg_num_goal_hit))
