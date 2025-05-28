import json

def create_level_presets():
    presets = {}
    
    # Level 1
    presets['Level_1_small'] = {
        'game_type': 0, 'map_size': 30, 'lines': False, 'tree_count': 6, 'trees_per_line': 1,
        'starting_firefighter_agents': 3, 'known': True,
    }
    presets['Level_1_large'] = {
        'game_type': 0, 'map_size': 60, 'lines': False, 'tree_count': 25, 'trees_per_line': 1,
        'starting_firefighter_agents': 10, 'known': True,
    }
    
    # Level 2
    presets['Level_2_small'] = {
        'game_type': 0, 'map_size': 30, 'lines': True, 'tree_count': 2, 'trees_per_line': 5,
        'starting_firefighter_agents': 2, 'starting_bulldozer_agents': 1, 'vegetation_density_offset': 30, 'known': True,
    }
    presets['Level_2_large'] = {
        'game_type': 0, 'map_size': 60, 'lines': True, 'tree_count': 5, 'trees_per_line': 7,
        'starting_firefighter_agents': 4, 'starting_bulldozer_agents': 3, 'vegetation_density_offset': 30, 'known': True,
    }
    
    # Level 3
    presets['Level_3_small'] = {
        'game_type': 1, 'map_size': 100, 'fire_spread_speed': 100,'known': False,
        'starting_drone_agents': 3
    }
    presets['Level_3_large'] = {
        'game_type': 1, 'map_size': 250, 'fire_spread_speed': 300,'known': False,
        'starting_drone_agents': 5
    }
    
    # Level 4
    presets['Level_4_small'] = {
        'game_type': 2, 'map_size': 100,
        'starting_firefighter_agents': 6, 'starting_helicopter_agents': 1, 'known': True,
    }
    presets['Level_4_large'] = {
        'game_type': 2, 'map_size': 250,
        'starting_firefighter_agents': 12, 'starting_helicopter_agents': 2, 'known': True,
    }
    
    # Level 5
    presets['Level_5_small'] = {
        'game_type': 4, 'map_size': 40, 'civilian_count': 3, 'civilian_clusters': 1, 'civilian_move_speed': 300, 'known': True,
        'starting_firefighter_agents': 3
    }
    presets['Level_5_large'] = {
        'game_type': 4, 'map_size': 80, 'civilian_count': 3, 'civilian_clusters': 3, 'civilian_move_speed': 300, 'known': True,
        'starting_firefighter_agents': 5
    }
    
    # Level 6
    presets['Level_6'] = {
        'game_type': 3, 'map_size': 60, 'water': False, 'fire_spread_speed': 500,
        'starting_firefighter_agents': 5, 'starting_bulldozer_agents': 1, 'vegetation_density_offset': 30, 'vegetation_density_offset': 30, 'known': True,
    }
    
    # Level 7
    presets['Level_7'] = {
        'game_type': 3, 'map_size': 60, 'water': True, 'fire_spread_speed': 500,'vegetation_density_offset': 30,
        'starting_firefighter_agents': 8, 'vegetation_density_offset': 30, 'known': True,
    }
    
    # Level 8
    presets['Level_8'] = {
        'game_type': 4, 'map_size': 100, 'civilian_count': 5, 'civilian_clusters': 1, 'civilian_move_speed': 300,
        'starting_firefighter_agents': 5, 'starting_drone_agents': 2, 'known': False,
    }
    
    # Level 9
    presets['Level_9'] = {
        'game_type': 3, 'map_size': 100, 'water': False, 'fire_spread_speed': 500,
        'starting_firefighter_agents': 5, 'starting_drone_agents': 2, 'starting_bulldozer_agents': 1, 'vegetation_density_offset': 30, 'vegetation_density_offset': 30, 'known': False,
    }
    
    # Level 10
    presets['Level_10'] = {
        'game_type': 3, 'map_size': 150, 'water': False, 'fire_spread_speed': 500,
        'starting_firefighter_agents': 10, 'starting_drone_agents': 2, 'starting_helicopter_agents': 2, 'vegetation_density_offset': 30, 'known': False,
    }
    
    # Level 11
    presets['Level_11'] = {
        'game_type': 4, 'map_size': 150, 'civilian_count': 5, 'civilian_clusters': 2, 'civilian_move_speed': 300, 'known': False,
        'starting_firefighter_agents': 10, 'starting_drone_agents': 2, 'starting_helicopter_agents': 2
    }
    
    # Level 12
    presets['Level_12'] = {
        'game_type': 5, 'map_size': 200, 'fire_spread_speed': 500,
        'civilian_count': 5, 'civilian_clusters': 1, 'civilian_move_speed': 300,
        'starting_firefighter_agents': 10, 'starting_bulldozer_agents': 1, 'starting_drone_agents': 2, 'starting_helicopter_agents': 2, 'vegetation_density_offset': 30, 'known': False,
    }

    return presets



def update_config(preset, seed, config, log_trajectory=False):
    # Define all possible game-related config keys
    game_config_keys = {
        'map_size', 'lines', 'tree_count', 'trees_per_line',
        'fire_spread_speed', 'water', 'civilian_count', 'civilian_clusters', 'civilian_move_speed'
    }
    
    # Define task-specific required variables
    task_variables = {
        0: {'map_size', 'lines', 'tree_count', 'trees_per_line'},
        1: {'map_size', 'fire_spread_speed'},
        2: {'map_size', },
        3: {'map_size', 'water', 'fire_spread_speed'},
        4: {'map_size', 'civilian_count', 'civilian_clusters', 'civilian_move_speed'},
        5: {'map_size', 'fire_spread_speed', 'civilian_count', 'civilian_clusters', 'civilian_move_speed'}
    }
    
    # Default adjustable parameters
    default_values = {
        'starting_firefighter_agents': 0,
        'starting_bulldozer_agents': 0,
        'starting_drone_agents': 0,
        'starting_helicopter_agents': 0,
        'steps_per_decision': 10,
        'vegetation_density_offset':20,
        'log_trajectory': log_trajectory
    }
    
    if 'game_type' not in preset:
        raise ValueError("Preset must include 'game_type' key.")
    
    game_type = preset['game_type']
    if game_type not in task_variables:
        raise ValueError(f"Invalid game type: {game_type}")
    
    # Update game-related keys
    for key in game_config_keys:
        if key in task_variables[game_type]:
            if key in preset:
                config[key] = preset[key]
            else:
                raise ValueError(f"Missing required key '{key}' for game type {game_type}.")
        else:
            config[key] = 0  # Irrelevant for this task, set to 0
    config['game_type'] = game_type

    # Always update seed and log_trajectory directly
    config['seed'] = seed
    config['log_trajectory'] = log_trajectory

    # Update adjustable agent settings from preset if given, else use default
    for key, value in default_values.items():
        config[key] = preset.get(key, value)
