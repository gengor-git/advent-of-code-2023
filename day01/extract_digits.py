import re

input_file = "day01/input.txt"
sample_file = "day01/sample.txt"
sample_file2 = "day01/sample2.txt"


def extract_words_with_digits(data_file) -> int:
    digit_sum = 0
    data = open(data_file).read().strip().splitlines()

    digi_dict = {
        '1':1,
        '2':2,
        '3':3,
        '4':4,
        '5':5,
        '6':6,
        '7':7,
        '8':8,
        '9':9,
        'one':1,
        'two':2,
        'three':3,
        'four':4,
        'five':5,
        'six':6,
        'seven':7,
        'eight':8,
        'nine':9
    }


    for entry in data:
        digits = re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine|sixteen', entry)
        print(digits)
        value = int(digi_dict[digits[0]]*10 + digi_dict[digits[-1]])
        print(value)
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
    print(extract_words_with_digits(sample_file2))
    # print(extract_digits(input_file))
    print(extract_words_with_digits(input_file))
