import re

input_file = "day03/input.txt"
sample_file = "day03/sample.txt"


def calculate_gears(data_file):
    result = 0
    global max_rows
    global max_cols
    global data
    data = open(data_file).read().strip().splitlines()
    max_rows = len(data)
    max_cols = len(data[0])

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
    for i, row in enumerate(data):
        start_position = 0
        j = 0
        while j < max_cols:
            # if we move through the columns here, start is always j
            start_position = j
            gear_number = ""
            # once we find a digit, we increment j here in this while
            # and start_position remains the initial value
            while j < max_cols and row[j].isdigit():
                gear_number += row[j]
                j += 1
            # if the number remains empty, we didn't find anything in this part
            if gear_number == "":
                j += 1
                continue
            # cast the string to a real number for adding later
            gear_number = int(gear_number)
            
            # Number ended, look around for symbols
            if is_symbol(i, start_position-1) or is_symbol(i, j):
                result += gear_number
                continue
            # now look in the above row and below
            for k in range(start_position-1, j+1):
                if is_symbol(i-1, k) or is_symbol(i+1, k):
                    result += gear_number
                    break
    return result

def is_symbol(i, j):
    # failsafe if we use an index that's out of bounds
    if not (0 <=i < max_rows and 0 <= j < max_cols):
        return False
    return data[i][j] != "." and not data[i][j].isdigit()

if __name__ == "__main__":
    # print(calculate_parts(sample_file))
    print(calculate_parts(input_file))
    # print(calculate_gears(sample_file))
    # print(calculate_gears(input_file))