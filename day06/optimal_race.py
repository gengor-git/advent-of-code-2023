import re

input_file = 'day06/input.txt'
sample_file = 'day06/sample.txt'

def calculate_start_delays(data_file):
    result = 0
    data = open(data_file).read().strip().splitlines()

    times = re.findall(r'\d+', data[0])
    distances = re.findall(r'\d+', data[1])

    for i in range(len(times)):
        print("Time {:3} ms for distance {:4} mm".format(int(times[i]), int(distances[i])))

    race_duration = 7


     
    return result


if __name__ == "__main__":
    # print(calculate_start_delays(sample_file))
    print(calculate_start_delays(input_file))
