import re

input_file = "day05/input.txt"
sample_file = "day05/sample.txt"


def execute_seed_mapping(data_file) -> int:
    result = 0
    data = open(data_file).read().strip().splitlines()

    seeds = re.findall(r'\d+', data[0])
    print("Total of {} seeds".format(len(seeds)))
    print("Seeds: {}".format(seeds))


    n = 1
    while n < len(data):
        if data[n].startswith("seed"):
            print("seed mapping")
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
        elif data[n] != "":
            values = re.findall(r'\d+', data[n])
            if len(values) != 3:
                raise ValueError("Too few values in mapping. Parsing error??")
            print(values)
        n += 1

    return result


if __name__ == "__main__":
    # execute_seed_mapping(sample_file)
    execute_seed_mapping(input_file)
