import json
import os
import numpy as np


file_name = 'json_config.json'
print(os.path.abspath("json_config.json"))

#
# config = {
#     "genders": {
#         'm': {'p': 0.5},
#         'f': {'p': 0.5}
#     },
#     "skin_tone": {
#         'light': {'p': 0.95,
#                   'options': {
#                       'Pele muito Branca': {'p': 0.35},
#                       'Pele Branca': {'p': 0.65}}
#                   },
#         'dark': {'p': 0.05,
#                  'options': {
#                      'Pele Morena Clara': {'p': 0.40},
#                      'Pele Morena Moderada': {'p': 0.30},
#                      'Pele Morena Escura': {'p': 0.20},
#                      'Pele Negra': {'p': 0.10}
#                  }}
#     }
#
# }
#
# # An example on file write
# with open(file_name, 'w') as json_config:
#     json_config.write(json.dumps(config))


def get_ps_for_config(config, root_key: str):
    keys_list = tuple(config[root_key].keys())
    weights = [elem['p'] for elem in [config[root_key][key] for key in keys_list]]
    result = np.random.choice(keys_list, p=weights)
    if 'options' in list(config[root_key][result].keys()):
        result += f" -> {get_ps_for_config(config[root_key][result], 'options')}"
    return result


def main():
    # Read the JSON config
    with open(file_name, 'r') as json_config:
        game_config = json.load(json_config)

    print(f'{type(game_config)} {game_config}')

    for run_counter in range(1000):
        keys = ['genders', 'skin_tone']
        for key in keys:
            res = get_ps_for_config(game_config, key)
            print(f'Run {run_counter:03}: The choice for key [{key}] is: {res}')


if __name__ == '__main__':
    main()
