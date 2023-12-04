import re

input_file = "day04/input.txt"
sample_file = "day04/sample.txt"

def calculate_scratchcard_points_pt2(data_file):
    result = 0
    data = open(data_file).read().strip().splitlines()
    max_rows = len(data)
    print("Processing {} cards in total.".format(max_rows))
    wins = {}
    for row in data:
        left = row.split("|")[0].strip().split(":")[1].strip()
        right = row.split("|")[1].strip()
        idx_card = int(row.split(":")[0].split(" ")[-1].strip())
        print("Processing ID {}".format(int(idx_card)))
        my_numbers = set(re.findall(r'\d+', left))
        winning_numbers = set(re.findall(r'\d+', right))
        matches = list(x for x in my_numbers if x in winning_numbers)
        # print("Matches: {}".format(matches))
        # print("= {} matches.".format(len(matches)))
        wins[idx_card] = len(matches)

    # now calculate the score, use incursion
    print("All matches per card: {}".format(wins))
    active_card = 1
    multiplier_for_copies = {}
    for x in range(max_rows):
        multiplier_for_copies[x+1] = 0
    while active_card < max_rows:
        print("-----")
        if wins[active_card]:
            # check if we have copies for this card
            if multiplier_for_copies[active_card] > 0:
                print("Card {} also has copies.".format(active_card))
                # once for the original card + the copies
                repeat = 1+multiplier_for_copies[active_card]
            else:
                repeat = 1
            for n in range(repeat):
                print("Card {} has {} wins".format(active_card, wins[active_card]))
                for x in range(active_card+1, active_card+1+wins[active_card]):
                    print("\_ Card {} -wins-copy-of-> {}".format(active_card, x))
                    multiplier_for_copies[x] += 1
        active_card += 1

    for x in range(max_rows):
        result += multiplier_for_copies[x+1] + 1
    print(multiplier_for_copies)

    return result

def calculate_scratchcard_points_pt1(data_file):
    result = 0
    data = open(data_file).read().strip().splitlines()

    for row in data:
        left = row.split("|")[0].strip().split(":")[1].strip()
        right = row.split("|")[1].strip()
        idx_card = row.split(":")[0].split(" ")[-1].strip()
        print("ID {}".format(int(idx_card)+1))
        print(left)
        print(right)
        my_numbers = set(re.findall(r'\d+', left))
        winning_numbers = set(re.findall(r'\d+', right))
        print(my_numbers)
        print(winning_numbers)
        matches = list(x for x in my_numbers if x in winning_numbers)
        print(matches)
        if len(matches) > 0:
            add = 2**(len(matches)-1)
            print("Add {}".format(add))
            result += add

    return result

if __name__ == "__main__":
    # print(calculate_scratchcard_points_pt1(sample_file))
    # print(calculate_scratchcard_points_pt1(input_file))
    print(calculate_scratchcard_points_pt2(sample_file))
    # print(calculate_scratchcard_points_pt2(input_file))
