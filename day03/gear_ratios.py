input_file = "day03/input.txt"
sample_file = "day03/sample.txt"

def calculate_parts(data_file):
    result = 0
    data = open(data_file).read().strip().splitlines()
    row = 0
    for entry in data:
        column = 0
        parts = []
        for col in entry:
            # print(column)
            if col.isdigit():
                print("Parts candidate: {} on ({},{})".format(col, row, column))
            elif col == ".":
                print("Nothing aka '{}'".format(col))
            else:
                print("Symbol {} on ({},{})".format(col, row, column))
            column += 1


    return result

if __name__ == "__main__":
    print(calculate_parts(sample_file))
    # print(calculate_possible_games(input_file))
    # print(calculate_minimum_cubes(sample_file))
    # print(calculate_minimum_cubes(input_file))