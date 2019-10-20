# Chain REAction Tool Environment (CREATE)

CREATE is a multi-step physics based puzzle reinforcement learning benchmark. 

## Usage
Using this environment is as easy as any other Gym environment. Simply `import create_game` where you want to use it and then `gym.make('CreateLevelPush-v0')` with the name of the task you want to use. CREATE features 10 diverse built in tasks. By default stochasicity is applied to each environment. If you don't want to use any stochasicity specify `Det` after the name of the level like: `gym.make('CreateLevelPushDet-v0')`. 

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

We define the name of the level, the location of the goal and the target, the type of reward (sparse or dense) and the objects in our escene. We also define the level of stochasicity in our environment. 
