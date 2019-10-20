from ..levels.lvl_config import setup_json_lvls, setup_class_lvls
import os.path as osp

setup_json_lvls(osp.dirname(osp.abspath(__file__)))
#setup_class_lvls("envs.logic_game.levels.all")


