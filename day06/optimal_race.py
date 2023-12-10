import re

input_file = 'day06/input.txt'
input_file2 = 'day06/input2.txt'
sample_file = 'day06/sample.txt'


def calculate_winning_games(data_file):
    result = 1
    data = open(data_file).read().strip().splitlines()

    times = re.findall(r'\d+', data[0])
    times = [int(num) for num in times]
    distances = re.findall(r'\d+', data[1])
    distances = [int(num) for num in distances]

    for i in range(len(times)):
        print("Time {:3} ms for distance {:4} mm".format(times[i], distances[i]))


    for i in range(len(times)):
        race_duration = times[i]
        distance_to_beat = distances[i]
        print("Calculation for race duration of {:4}".format(race_duration))
        pressed = 0
        wins = 0
        race_results = []
        while pressed < race_duration:
            # print("Pressing for {:3}ms".format(pressed))
            # formula
            # t = race duration in ms
            # p = ms pressed
            # distance = (t-p) * p
            distance = (race_duration - pressed) * pressed
            if distance > distance_to_beat:
                print("Winning press.")
                print("\\__ Pressing {:3} leads to {:5}mm".format(pressed, distance))
                wins += 1
            pressed += 1
        result *= wins
    
    return result

def calculate_start_delays(data_file):
    result = 1
    data = open(data_file).read().strip().splitlines()

    times = re.findall(r'\d+', data[0])
    times = [int(num) for num in times]
    distances = re.findall(r'\d+', data[1])
    distances = [int(num) for num in distances]

    for i in range(len(times)):
        print("Time {:3} ms for distance {:4} mm".format(times[i], distances[i]))


    for i in range(len(times)):
        race_duration = times[i]
        distance_to_beat = distances[i]
        print("Calculation for race duration of {:4}".format(race_duration))
        pressed = 0
        wins = 0
        race_results = []
        while pressed < race_duration:
            # print("Pressing for {:3}ms".format(pressed))
            # formula
            # t = race duration in ms
            # p = ms pressed
            # distance = (t-p) * p
            distance = (race_duration - pressed) * pressed
            if distance > distance_to_beat:
                print("Winning press.")
                print("\\__ Pressing {:3} leads to {:5}mm".format(pressed, distance))
                wins += 1
            pressed += 1
        result *= wins
    
    return result


if __name__ == "__main__":
    # print(calculate_start_delays(sample_file))
    # print(calculate_start_delays(input_file))
    print(calculate_winning_games(input_file2))
