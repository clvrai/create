import sys
sys.path.insert(0, '.')
import envs.logic_game.defs
from envs.logic_game.settings import LogicGameSettings
import gym


env = gym.make('CreateLevelPush-v0')


obs = env.reset()

done = False
while not done:
    obs, reward, done, info = env.step([0.0,0.0,0])

