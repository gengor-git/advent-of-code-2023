import re

input_file = "day02/input.txt"
sample_file = "day02/sample.txt"

validation = {
    'red': 12,
    'green': 13,
    'blue': 14
}

def calculate_possible_games(data_file) -> int:
    result = 0
    data = open(data_file).read().strip().splitlines()
    for entry in data:
        game = entry.split(": ")
        game[0] = game[0].split(" ")[-1]
        game_id = int(game[0])
        sessions = game[1].split("; ")
        for session in sessions:
            cubes = session.split(", ")
            for cube in cubes:
                cube = cube.split(" ")
                if validation[cube[1]] < int(cube[0]):
                    # not a valid game
                    game_id = 0
        result += game_id
    return result


if __name__ == "__main__":
    print(calculate_possible_games(sample_file))
    print(calculate_possible_games(input_file))