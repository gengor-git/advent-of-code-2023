input_file = "day02/input.txt"
sample_file = "day02/sample.txt"

validation = {
    'red': 12,
    'green': 13,
    'blue': 14
}

def calculate_minimum_cubes(data_file) -> int:
    result = 0
    data = open(data_file).read().strip().splitlines()
    for entry in data:
        game = entry.split(": ")
        game[0] = game[0].split(" ")[-1]
        game_id = int(game[0])
        game_power = 0
        at_least_cubes_per_game = {
            'red': 0,
            'green': 0,
            'blue': 0
        }
        sessions = game[1].split("; ")
        for session in sessions:
            cubes = session.split(", ")
            for cube in cubes:
                cube = cube.split(" ")
                at_least_cubes_per_game[cube[1]] = max(at_least_cubes_per_game[cube[1]], int(cube[0]))
        print(at_least_cubes_per_game)
        power = at_least_cubes_per_game['red'] * at_least_cubes_per_game['green'] * at_least_cubes_per_game['blue']
        result += power
    return result

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
    # print(calculate_possible_games(sample_file))
    # print(calculate_possible_games(input_file))
    # print(calculate_minimum_cubes(sample_file))
    print(calculate_minimum_cubes(input_file))