import re

input_file = "day03/input.txt"
sample_file = "day03/sample.txt"

def calculate_gears(data_file):
    result = 0
    global max_rows
    global max_cols
    global data
    global gears_adjecent
    data = open(data_file).read().strip().splitlines()
    max_rows = len(data)
    max_cols = len(data[0])
    gears_adjecent = [[[] for _ in range(max_cols)] for _ in range(max_rows)]

    for idx_row, row in enumerate(data):
        start_position = 0
        idx_col = 0
        while idx_col < max_cols:
            start_position = idx_col 
            gear_number = ""
            while idx_col < max_cols and row[idx_col].isdigit():
                gear_number += row[idx_col]
                idx_col += 1

            if gear_number == "":
                idx_col += 1
                continue

            gear_number = int(gear_number)
            
            # check surroundings
            # left and right
            is_symbol(idx_row, start_position-1, number=gear_number) or is_symbol(idx_row, idx_col, number=gear_number)

            # row above and below
            for k in range(start_position-1, idx_col+1):
                # first above then below
                is_symbol(idx_row-1, k, number=gear_number) or is_symbol(idx_row+1, k, number=gear_number)
    
    for idx_row in range(max_rows):
        for idx_col in range(max_cols):
            numbers = gears_adjecent[idx_row][idx_col]
            # check for two numbers, that where adjecent to *
            if data[idx_row][idx_col] == "*" and len(numbers) == 2:
                result += numbers[0] * numbers[1]

    return result

def calculate_parts(data_file):
    result = 0
    global max_rows
    global max_cols
    global data
    data = open(data_file).read().strip().splitlines()
    max_rows = len(data)
    max_cols = len(data[0])

    for idx_row, row in enumerate(data):
        start_position = 0
        idx_col = 0
        while idx_col < max_cols:
            start_position = idx_col 
            gear_number = ""
            while idx_col < max_cols and row[idx_col].isdigit():
                gear_number += row[idx_col]
                idx_col += 1

            if gear_number == "":
                idx_col += 1
                continue

            gear_number = int(gear_number)
            
            # check surroundings
            # left and right
            if is_symbol(idx_row, start_position-1) or is_symbol(idx_row, idx_col):
                result += gear_number
                continue
            # row above and below
            for k in range(start_position-1, idx_col+1):
                # first above then below
                if is_symbol(idx_row-1, k) or is_symbol(idx_row+1, k):
                    result += gear_number
                    break
    return result

def is_symbol(row, col, number=0):
    # failsafe if we use an index that's out of bounds
    if not (0 <=row < max_rows and 0 <= col < max_cols):
        return False

    # only in part 2 number is actually set to non-0
    if not number == 0 and data[row][col] == "*":
        global gears_adjecent
        gears_adjecent[row][col].append(number)
    
    return data[row][col] != "." and not data[row][col].isdigit()

if __name__ == "__main__":
    # print(calculate_parts(sample_file))
    # print(calculate_parts(input_file))
    # print(calculate_gears(sample_file))
    print(calculate_gears(input_file))