import re

input_file = "day05/input.txt"
sample_file = "day05/sample.txt"


def add_to_map(source:int, dest:int, length:int, datamap:set) -> set:

    i = 0
    while i < length:
        datamap[source+i] = dest+i
        i += 1

    return datamap


def execute_seed_mapping(data_file) -> int:
    result = 0
    data = open(data_file).read().strip().splitlines()

    seeds = re.findall(r'\d+', data[0])
    print("Total of {} seeds".format(len(seeds)))
    print("Seeds: {}".format(seeds))


    # 'seed', 'soil', 'fertilizer', 'water', 'light', 'temperature', 'humidity'

    n = 1
    all_numbers = []
    category = "none"
    mapping_seed_to_soil = {}
    mapping_soil_to_fertilizer = {}
    mapping_fertilizer_to_water = {}
    mapping_water_to_light = {}
    mapping_light_to_temperature = {}
    mapping_temperature_to_humidity = {}
    mapping_humidity_to_location = {}
    while n < len(data):
        if data[n].startswith("seed"):
            print("Seed mapping")

            n += 1
            while data[n] != "":
                print(data[n])
                print(".")
                values = re.findall(r'\d+', data[n])
                if len(values) != 3:
                    raise ValueError("Too few values in mapping. Parsing error??")
                mapping_seed_to_soil = add_to_map(int(values[1]), int( values[0] ), int( values[2] ), mapping_seed_to_soil)
                print(".")
                n += 1

        elif data[n].startswith("soil"):
            print("soil mapping")
        elif data[n].startswith("fertilizer"):
            print("fertilizer mapping")
        elif data[n].startswith("water"):
            print("water mapping")
        elif data[n].startswith("light"):
            print("light mapping")
        elif data[n].startswith("temperature"):
            print("temperature mapping")
        elif data[n].startswith("humidity"):
            print("humidity mapping")
        else:
            pass
        n += 1
        print("Seed to soil: {}".format(mapping_seed_to_soil))
    return result



if __name__ == "__main__":
    # execute_seed_mapping(sample_file)
    print(execute_seed_mapping(input_file))
