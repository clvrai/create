# Chain REAction Tool Environment (CREATE)
[Ayush Jain](http://www-scf.usc.edu/~ayushj/)\*, [Andrew Szot](https://www.andrewszot.com)\*, [Joseph J. Lim](https://clvrai.com) at [USC CLVR lab](https://clvrai.com)  
[[Environment website](https://www.clvrai.com/create)]   [[Paper](https://www.clvrai.com)]

<p align="center">
     <kbd>
          <img src="github-assets/combo3.gif" width="400">
     </kbd>
</p>

**CREATE** is a multi-step physics-based puzzle reinforcement learning benchmark featuring many diverse tools and tasks. The objective is to sequentially select and position tools from an available set, to make the red ball (target) reach the goal (green) in various environment configurations.

Try solving tasks for yourself on the [online demo](https://clvrai.com/create/). Or get started with some [examples](https://github.com/gitlimlab/CREATE/tree/master/examples).

### Features
- **Multi-step environment**: Agent places a tool after every few iterations of simulation acting on *image* observations. 
- **Easily usable**: Environment is a standard [OpenAI Gym](https://github.com/openai/gym) environment interface. 
- **Diverse Tasks**: 12 complex tasks with stochastic variations and an easy <a href="https://github.com/clvrai/CREATE#   defining-tasks">interface</a> to create many more tasks. Suitable for meta reinforcement learning. 
- **Variety of Tools**: 12 base tool types, with many more variations of sizes, angles, friction parameters. 
- **Simple and Fast**: Runs headless and supports flexible resolutions for rendering. 
- **Configurable**: Easily create new levels with a simple JSON interface and create new tools. 

### Relevant Research Areas
- **Reinforcement Learning for Physical Reasoning**: Long-horizon Physics puzzles with diverse interactions. 
- **Generalization to Unseen Actions**: Large and diverse action space to test generalization. 
- **Multi-task Learning**: Diverse task distribution suitable for meta learning. 
- **Predictive Modeling and Model-based RL**: Consistent environment and tool dynamics for learning models. 
- **Tool functionality and usage**: Discrete (selection) + Continuous (placement) action space for tools.


## (1) Usage
`import create_game` to register the environments. From here, create the gym environment using the standard command: 
`gym.make('CreateLevelPush-v0')` with the name of the task you want to use. CREATE comes with [12 diverse tasks](#6-included-tasks) and you can easily create more using the simple JSON definition system. 
Some level of stochasicity is applied in all of the default environments. If you want to use deterministic configurations, specify `Det` after the name of the level like: `gym.make('CreateLevelPushDet-v0')`. 

See [`examples/random_agent.py`](https://github.com/clvrai/CREATE/blob/master/examples/random_agent.py) for an example with using a random agent on the environment. This environment also works well with multi-processing, and the simulation is optimized for high training speeds.

For a performance comparison to the method from our paper, use the evaluation script at [`examples/evaluation.py`](https://github.com/clvrai/CREATE/blob/master/examples/evaluation.py). Change the evaluation script to include your models to assess their performance on the test set of tools.
<br>

## (2) Installation
Clone this repository. `pip install -r requirements.txt` from this repo. Copy the `create_game` folder to where you want to use it. Note this project only works with Python 3.6+. 

<br>

## (3) Multi-Task
See [`examples/multi_task.py`](https://github.com/gitlimlab/CREATE/blob/master/examples/multi_task.py) for a complete example. 

<br>

## (4) Game Configuration
See [`create_game/settings.py`](https://github.com/gitlimlab/CREATE/blob/master/create_game/settings.py) for a list of all possible settings that can be changed about the game play, rendering, reward structure and simulation. Configure the environment as: 

<br>

## (5) Defining Tasks
See [`examples/create_task.ipynb`](https://github.com/gitlimlab/CREATE/blob/master/examples/create_task.ipynb) for an example on how to define custom tasks. 

You can also create custom tasks in CREATE with ease. Simply define the level in JSON and you are good to go. 
An example JSON definition of a task is shown below: 
```
{
     'name' :  'Moving' ,
     'target' :  '[0.6, 0.75]',
     'goal' :  '[-0.7, 0.0]',
     'moving_goal' : true,
     'rnd' : {
         'target' :  '[uniform(-0.2, 0.2), uniform(-0.2, 0.2)]',
         'goal' :  '[0., uniform(-0.5, 0.5)]' 
    },
    'env' : [
        {
             'name' :  'trampoline',
             'pos' :  '[-0.7, -0.75]' ,
             'id' : '1',
             'elasticity' : '1.0'
        }
    ]
}
```

You can register this JSON file as a gym environment by calling `register_json_folder` passing the name of the folder the JSON files are in. You can also call `register_json_str` to register just one task defined as a string. 

We start by defining the name of the level ('Moving') specify the initial position of the target ball and goal location. The 'rnd' section defines the stochasicity of the starting position for both the target and goal in the scene. In the 'env' section we define all the objects that are in the scene. We would load the level by specifying `gym.create('CreateLevelMoving')` Here are a complete list of options we can specify for the top level fields:
- `name`: name of the task. This will determine the load name of the task as well. 
- `target`: position of the target ball.
- `goal`: position of the goal ball.
- `moving_goal`: `true` if the goal should act as a ball with mass and be able to be moved. If false, the goal does not interact with anything. 
- `rnd`: The stochasicities for the each object in the level. Note that stochasicity can be applied to multiple objects in the scene at the same time through specifying two names in the field as: 
  ```
  'goal,medium_floor:1' :  '[uniform(-0.2, 0.2), uniform(-0.2, 0.2)]'
   ```
   This stochasicity is then applied the same to the env object with name 'medium_floor' with ID 1 and the goal object. This is useful if you have a platform below a object you want to be randomly initialized and you want to move them together.  
- `env`: Where all of the environment objects are defined. See [this location in the code](https://github.com/gitlimlab/CREATE/blob/2b68ffcdcc6d03fa0cfcae97963f2576d233c9ff/create_game/tools/tool_factory.py#L37) for the complete list of possible objects. You can also specify parameters to this object such as 'elasticity', 'length' or 'angle'. You can also specify an ID to reference in the rnd noise. 


```
from create_game import CreateGameSettings
import gym

env = gym.create('CreateLevelPush-v0')
env.set_settings(CreateGameSettings(max_num_steps=5, action_set_size=10))
```

<br>

## (6) Included Tasks

| Task Description  | Task Example | Task Description  | Task Example |
| ------------- | ------------- | ------------- | ------------- |
| Basket (`CreateLevelBasket`)  | <img src="github-assets/basket.gif" width="400">  | Belt (`CreateLevelBelt`)  | <img src="github-assets/belt.gif" width="400">  |
| Buckets (`CreateLevelBuckets`)  | <img src="github-assets/buckets.gif" width="400">  | Cannon (`CreateLevelCannon`)  | <img src="github-assets/cannon.gif" width="400">  |
| Collide (`CreateLevelCollide`)  | <img src="github-assets/collide.gif" width="400">  | Ladder (`CreateLevelLadder`)  | <img src="github-assets/ladder.gif" width="400">  |
| Moving (`CreateLevelMoving`)  | <img src="github-assets/moving.gif" width="400">  | Navigate (`CreateLevelNavigate`)  | <img src="github-assets/navigate.gif" width="400">  |
| Obstacle (`CreateLevelObstacle`)  | <img src="github-assets/obstacle.gif" width="400">  | Push (`CreateLevelPush`)  | <img src="github-assets/push.gif" width="400">  |
| Seesaw (`CreateLevelSeesaw`)  | <img src="github-assets/seesaw.gif" width="400">  | Funnel (`CreateLevelFunnel`) | <img src="github-assets/funnel.gif" width="400">  |

<br>

## (7) References
Our environment is based on Pygame and Pymunk libraries:
- Pygame: https://www.pygame.org/docs/
- Pymunk: http://www.pymunk.org/

<br>

## (8) Citation
```
@inproceedings{
}
```
