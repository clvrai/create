# Chain REAction Tool Environment (CREATE)
<p align="center">
     <img src="github-assets/combo3.gif" width="400">
</p>

CREATE is a multi-step physics based puzzle reinforcement learning benchmark featuring many diverse tools. The goal of the game is to get the red ball (the target ball) to the blue ball (the goal ball). The agent must select which tool to place and where to place it. To solve the task multiple tools need to be placed. 

Features:
- **Tool usage and reasoning:** Choose which tool to select and where to place it. 
- **Multi-step:** reinforcment learning in precise **physics based environments**.
- **Task generalization:** 10 included tasks with randomized configurations of each task. 
- **Configurable:** Easily create new levels with a simple JSON interface and create new tools. 
- **Easily usable:** Environment is a standard [OpenAI Gym](https://github.com/openai/gym) environment interface. 

Try solving tasks for yourself on the [online demo](http://lim-e.usc.edu:8080/create/). Or get started with some [examples](https://github.com/gitlimlab/CREATE/tree/master/examples).

## Usage
`import create_game` to register the environments. From here, create the gym environment using the standard command: 
`gym.make('CreateLevelPush-v0')` with the name of the task you want to use. CREATE features 10 diverse default tasks which can be seen in the "Included Tasks" section. You can easily create more using the simple JSON definition system. 
Some level of stochasicity is applied in all of the default environments. If you don't want to use any stochasicity specify `Det` after the name of the level like: `gym.make('CreateLevelPushDet-v0')`. 

See [`examples/random_agent.py`](https://github.com/gitlimlab/CREATE/blob/master/examples/random_agent.py) for an example with using a random agent on the environment. This environment also works well with multi-processing, an example will be posted soon. 

## Installation
Clone this repository. `pip install -r requirements.txt` from this repo. Copy the `create_game` folder to where you want to use it. Note this project only works with Python 3.6+. 

## Multi-Task
See [`examples/multi_task.py`](https://github.com/gitlimlab/CREATE/blob/master/examples/multi_task.py) for a complete example. 

## Game Configuration
See [`create_game/settings.py`](https://github.com/gitlimlab/CREATE/blob/master/create_game/settings.py) for a list of all possible settings that can be changed about the game play, rendering, reward structure and simulation. Configure the environment as: 

## Defining Tasks
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

## Included Tasks

| Task Description  | Task Example |
| ------------- | ------------- |
| Basket (`CreateLevelBasket`)  | <img src="github-assets/basket.gif" width="400">  |
| Belt (`CreateLevelBelt`)  | <img src="github-assets/belt.gif" width="400">  |
| Buckets (`CreateLevelBuckets`)  | <img src="github-assets/buckets.gif" width="400">  |
| Cannon (`CreateLevelCannon`)  | <img src="github-assets/cannon.gif" width="400">  |
| Collide (`CreateLevelCollide`)  | <img src="github-assets/collide.gif" width="400">  |
| Ladder (`CreateLevelLadder`)  | <img src="github-assets/ladder.gif" width="400">  |
| Moving (`CreateLevelMoving`)  | <img src="github-assets/moving.gif" width="400">  |
| Navigate (`CreateLevelNavigate`)  | <img src="github-assets/navigate.gif" width="400">  |
| Obstacle (`CreateLevelObstacle`)  | <img src="github-assets/obstacle.gif" width="400">  |
| Push (`CreateLevelPush`)  | <img src="github-assets/push.gif" width="400">  |
| Seesaw (`CreateLevelSeesaw`)  | <img src="github-assets/seesaw.gif" width="400">  |
