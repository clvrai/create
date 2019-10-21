from ..levels.lvl_config import register_json_folder, setup_class_lvls
import os.path as osp

register_json_folder(osp.dirname(osp.abspath(__file__)))
#setup_class_lvls("envs.logic_game.levels.all")


