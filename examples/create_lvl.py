import sys
sys.path.insert(0, '.')
from create_game import setup_json_lvls, save_mp4

import gym

def sample_rnd_action():
    rnd_pos = env.action_space.spaces['pos'].sample()
    rnd_sel = env.action_space.spaces['index'].sample()
    return [*rnd_pos, rnd_sel]

# Or whatever path to your folder of custom JSON task definitions.
json_path = osp.join(osp.dirname(osp.abspath(__file__)), 'custom_json')
setup_json_lvls(json_path)

env = gym.make('CustomPush-v0')


for iter_i in range(num_iters):
    obs = env.reset()

    done = False
    frames = []
    while not done:
        action = sample_rnd_action()
        obs, reward, done, info = env.step(action)
        frame = env.render('rgb_array_high_mega_changed_colors')
        frames.append(frame)

    # display all the frames to the screen somehow.


