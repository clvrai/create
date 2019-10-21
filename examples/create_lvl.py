import sys
sys.path.insert(0, '.')
from create_game import register_json_folder, register_json_str
import os.path as osp

import gym

def sample_rnd_action():
    rnd_pos = env.action_space.spaces['pos'].sample()
    rnd_sel = env.action_space.spaces['index'].sample()
    return [*rnd_pos, rnd_sel]

# Or whatever path to your folder of custom JSON task definitions.
#json_path = osp.join(osp.dirname(osp.abspath(__file__)), 'custom_json')
#register_json_folder(json_path)
#


# Register a string as a JSON environment
json_str = """ {
    "name": "CustomPush",
    "lvl_type": "marker",
    "target": "[0.1, -0.25 + OFFSET]",
    "goal": "[-0.7, -0.75 + OFFSET]",
    "rnd": {
        "marker_ball:0": "[uniform(-HIGH_NOISE, HIGH_NOISE), uniform(-HIGH_NOISE, HIGH_NOISE)]",
        "target,medium_floor:0": "[uniform(-HIGH_NOISE, HIGH_NOISE), uniform(-HIGH_NOISE, HIGH_NOISE)]",
        "goal,medium_floor:1": "[uniform(-HIGH_NOISE, HIGH_NOISE), uniform(-HIGH_NOISE, HIGH_NOISE)]"
    },
    "env": [
        {
            "name": "marker_ball",
            "pos": [0.6, 0.75],
            "id": 0
        },
        {
            "name": "medium_floor",
            "pos": "[0.1, -0.25]",
            "id": 0
        },
        {
            "name": "medium_floor",
            "pos": "[-0.7, -0.75]",
            "id": 1
        }
    ]
}
"""
register_json_str(json_str)



#obs = env.reset()
#
#done = False
#frames = []
#while not done:
#    action = sample_rnd_action()
#    obs, reward, done, info = env.step(action)
#    frame = env.render('rgb_array_high_mega_changed_colors')
#    frames.append(frame)
#
## display all the frames to the screen somehow.
#
#
