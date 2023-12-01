input_file = "day01/input.txt"
sample_file = "day01/sample.txt"

def extract_digits(data_file) -> int:
    digit_sum = 0
    data = open(data_file).read().strip().splitlines()
    for entry in data:
        print(entry)
    return digit_sum

if __name__ == "__main__":
    print(extract_digits(input_file))
    