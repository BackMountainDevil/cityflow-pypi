This is not the official CityFlow repository package. Please visit the [official CityFlow repository](https://github.com/cityflow-project/CityFlow/) and install it first.

    pip install git+https://github.com/cityflow-project/CityFlow.git

This repository is a python package based on the CityFlow simulator and provides a high-level interface for users to interact with the environment. It is just contains some datas and gym-like.

usage demo

```python
import os
import random 
import time

from cityflowenv.env import CityflowEnv

if __name__ == "__main__":
    """
    map_name: jinan-1, jinan-2, jinan-3, hangzhou-1, hangzhou-2, newyork-1, newyork-2

    log_path: the path to save the config file of cityflow, default is the current working directory. If not set, the config file will be saved in the package directory.

    options of list_state_feature: cur_phase, time_this_phase, lane_num_vehicle_in, lane_num_vehicle_out, lane_queue_vehicle_in,lane_queue_vehicle_out,  traffic_movement_pressure_queue, traffic_movement_pressure_num, pressure, adjacency_matrix

    options of dic_reward_info: queue_length, pressure. such as {"queue_length": -0.25, "pressure": -0.15},

    """
    kwargs = {
        "map_name": "jinan-2",
        "log_path": os.getcwd(),
        "thread_num": 6,
        "eight_phase": True,
        "list_state_feature": ["cur_phase", "lane_queue_vehicle_in"],
        "dic_reward_info": {"queue_length": -0.25},
        "interval": 1,
        "seed": 1,
        "yellow_time": 5,
        "lane_change": True,
        "save_replay": False,
    }
    env = CityflowEnv(**kwargs)
    print(env.get_state())
    start_time = time.time()
    done = False
    while not done:
        action_list = [random.randint(1, 7) for _ in range(env.n_agents)]
        _, done, _ = env.step(action_list)
    print(env.get_state())
    print(f"Time Usage: {time.time()-start_time}s ATT: {env.get_avg_travel_time()}")
```

# refer

https://github.com/LiangZhang1996/AttentionLight
