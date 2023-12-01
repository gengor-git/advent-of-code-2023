import re

input_file = "day01/input.txt"
sample_file = "day01/sample.txt"
sample_file2 = "day01/sample2.txt"


def extract_words_with_digits(data_file) -> int:
    digit_sum = 0
    data = open(data_file).read().strip().splitlines()

    for entry in data:
        entry = entry.replace('one', 'o1e')
        entry = entry.replace('two', 't2o')
        entry = entry.replace('three', 't3r')
        entry = entry.replace('four', 'f4r')
        entry = entry.replace('five', 'f5e')
        entry = entry.replace('six', 's6x')
        entry = entry.replace('seven', 's7n')
        entry = entry.replace('eight', 'e8t')
        entry = entry.replace('nine', 'n9e')

        digits = re.findall(r'\d', entry)
        # print(digits)
        value = int(digits[0] + digits[-1])
        digit_sum = digit_sum + value
    return digit_sum

def extract_digits(data_file) -> int:
    digit_sum = 0
    data = open(data_file).read().strip().splitlines()
    for entry in data:
        digits = re.findall(r'\d', entry)
        value = int(digits[0] + digits[-1])
        # print(value)
        digit_sum = digit_sum + value

    return digit_sum

if __name__ == "__main__":
    # print(extract_digits(sample_file))
    # print(extract_words_with_digits(sample_file2))
    # print(extract_digits(input_file))
    print(extract_words_with_digits(input_file))
