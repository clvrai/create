# Chain REAction Tool Environment (CREATE)

CREATE is a multi-step physics based puzzle reinforcement learning benchmark.
CREATE features 10 challenging physical reasoning tasks where the agent must
select a tool to place from over 2,000 possible tools and choose the `x,y`
coordinates on the screen where the tool should be placed. 

This environment was created to encourage research on the following areas: 
- Multi-step reinforcment learning in precise physics based environments. All
  of the 10 levels require solving the task through different physical
  phenomina. 
- Tool usage in reinforcement learning. The environment can be configurated to
  have how ever many tools available. Agents must reason about which tool is
  appropriate for the current state and the desired usage or `x,y` position to
  place the tool at. 
- Task generalization. Generalizing between the 10 tasks provided presents a
  challenge for current RL methods. Each task can generate further
  configurations of the same randomized subtask and it is also easy to define
  your own tasks. 

Try solving tasks for yourself on the [online demo](https://www.google.com).

## Usage
This environment is just a normal Gym environment. Simply `import create_game`
to register to the environment. Then create the gym environment using the
standard command: 
`gym.make('CreateLevelPush-v0')` with the name of the task you want to use. CREATE features 10 diverse default tasks which can be seen in the "Included Tasks" section. You can easily create more using the simple JSON definition system. 
Some level of stochasicity is applied in all of the default environments. If you don't want to use any stochasicity specify `Det` after the name of the level like: `gym.make('CreateLevelPushDet-v0')`. 

See `examples/random_agent.py` for an example with using a random agent on the
environment. 


## Defining Tasks
An example JSON definition of a level is shown below: 
```
{
     name :  Navigate ,
     lvl_type :  marker ,
     target :  [0.1, -0.35 + OFFSET] ,
     goal :  [-0.65, -0.7 + OFFSET] ,
     reward :  sparse ,
     rnd : {
             _marker_ball:0 :  [uniform(-HIGH_NOISE, HIGH_NOISE), uniform(-HIGH_NOISE, HIGH_NOISE)] ,
            "target,medium_floor:0": "[uniform(-MID_NOISE, MID_NOISE), uniform(-MID_NOISE, MID_NOISE)]",
             goal,medium_floor:1 :  [uniform(-HIGH_NOISE, HIGH_NOISE), uniform(-HIGH_NOISE, HIGH_NOISE)] 
        },  
     env : [
        {   
             name :  marker_ball ,
             pos :  [-0.6, 0.75] ,
             id : 0
        },  
        {   
             name :  medium_floor ,
             pos :  [0.1, -0.35] ,
             id : 0
        },  
        {   
             name :  medium_floor ,
             pos :  [-0.65, -0.7] ,
             id : 1
        },  
        {   
             name :  floor ,
             pos :  [-0.5, 0.1] ,
             length : 40
        }   
    ]   
}
```

We define the name of the level, the location of the goal and the target, the type of reward (sparse or dense) and the objects in our escene. We also define the level of stochasticity in our environment. 

## Included Tasks
