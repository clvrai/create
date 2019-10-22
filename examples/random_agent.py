import sys
sys.path.insert(0, '.')
# import create game whatever way works best for you
import create_game

import gym

def sample_rnd_action():
    rnd_pos = env.action_space.spaces['pos'].sample()
    rnd_sel = env.action_space.spaces['index'].sample()
    return [*rnd_pos, rnd_sel]


env = gym.make('CreateLevelPush-v0')

num_iters = 10

for iter_i in range(num_iters):
    obs = env.reset()

    done = False
    while not done:
        action = sample_rnd_action()
        obs, reward, done, info = env.step(action)
        try:
            env.render('human')
        except:
            pass
