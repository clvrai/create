from collections import namedtuple
from .create_action_set import gen_action_set, get_allowed_actions, UseSplit
import os.path as osp

params = {
        ######################
        # Reward modifiers
        ######################
        'default_reward': 0.01,
        'no_op_reward': 0.0,
        'goal_reward': 10.0,
        'dense_reward_scale': 0.0,
        'invalid_action_reward': -0.01,
        'blocked_action_reward': -0.01,
        'sec_goal_reward': 2.0,
        'sec_goal_radius': 6.0,
        'permanent_goal': True,
        # For marker ball levels
        'marker_reward': 'reg',
        'target_reward': 1.0,

        ######################
        # Render settings
        ######################
        'screen_width': 84,
        'screen_height': 84,
        'render_width': 84,
        'render_height': 84,
        'high_res_width': 1024,
        'high_res_height': 1024,
        'render_ball_traces': False,
        'evaluation_mode': False,
        'render_mega_res': False,
        'mega_res_interval': 4,

        ######################
        # Simulation settings
        ######################
        'max_num_steps': 30,
        'large_steps': 40,
        'gravity': (0.0, -2.0),
        # Minimum velocity for motion to be considered stopped
        'min_velocity': 0.05,
        'no_overlap_env': False,
        'overlap_threshold': 0.3,
        'move_thresh': 0.03,
        'use_overlap': True,

        ######################
        # Action space settings
        ######################
        'action_random_sample': True,
        'action_sample_fn': gen_action_set,
        'get_allowed_actions_fn': get_allowed_actions,
        'action_set_size': 40,
        'action_extra': {},
        'randomized_fixed_set': False,
        'split_name': 'full_clean',
        'split_type': UseSplit.TRAIN,
        'action_seg_loc': osp.join(osp.dirname(osp.abspath(__file__)), 'splits'),
        'validation_ratio': 0.5,

        ######################
        # Tool generation settings
        ######################
        'gran_factor': 1.0,
        }

params_pairs = params.items()

CreateGameSettings = namedtuple('CreateGameSettings',
        [x[0] for x in params_pairs],
        defaults=[x[1] for x in params_pairs]
        )


