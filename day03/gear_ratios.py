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

    for i, row in enumerate(data):
        start_position = 0
        j = 0
        while j < max_cols:
            start_position = j 
            gear_number = ""
            while j < max_cols and row[j].isdigit():
                gear_number += row[j]
                j += 1

            if gear_number == "":
                j += 1
                continue

            gear_number = int(gear_number)
            
            # check surroundings
            # left and right
            is_symbol(i, start_position-1, number=gear_number) or is_symbol(i, j, number=gear_number)

            # row above and below
            for k in range(start_position-1, j+1):
                # first above then below
                is_symbol(i-1, k, number=gear_number) or is_symbol(i+1, k, number=gear_number)
    
    for i in range(max_rows):
        for j in range(max_cols):
            numbers = gears_adjecent[i][j]
            # check for two numbers, that where adjecent to *
            if data[i][j] == "*" and len(numbers) == 2:
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

    for i, row in enumerate(data):
        start_position = 0
        j = 0
        while j < max_cols:
            start_position = j 
            gear_number = ""
            while j < max_cols and row[j].isdigit():
                gear_number += row[j]
                j += 1

            if gear_number == "":
                j += 1
                continue

            gear_number = int(gear_number)
            
            # check surroundings
            # left and right
            if is_symbol(i, start_position-1) or is_symbol(i, j):
                result += gear_number
                continue
            # row above and below
            for k in range(start_position-1, j+1):
                # first above then below
                if is_symbol(i-1, k) or is_symbol(i+1, k):
                    result += gear_number
                    break
    return result

def is_symbol(i, j, number=0):
    # failsafe if we use an index that's out of bounds
    if not (0 <=i < max_rows and 0 <= j < max_cols):
        return False
        
    if not number == 0 and data[i][j] == "*":
        global gears_adjecent
        gears_adjecent[i][j].append(number)
    
    return data[i][j] != "." and not data[i][j].isdigit()

if __name__ == "__main__":
    # print(calculate_parts(sample_file))
    # print(calculate_parts(input_file))
    # print(calculate_gears(sample_file))
    print(calculate_gears(input_file))