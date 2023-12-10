import re
# import pandas as pd

input_file = 'day07/input.txt'
sample_file = 'day07/sample.txt'


def calculate_winnings(data_file) -> int:
    result = 0
    data = open(data_file).read().strip().splitlines()

    cards = "AKQJT98765432"

    for play in data:
        hand = play.split()[0].strip()
        bid = int(play.split()[1].strip())
        print("Hand {} with bid {}".format(hand, bid))
        # hand_values = pd.Series(list(hand))
        hand_value = {}
        for card in cards:
            if hand.count(card) > 0:
                hand_value[card] = hand.count(card)
        sorted_hand_value = dict(sorted(hand_value.items(), key=lambda item: item[1], reverse=True))
        print(sorted_hand_value)

        


    return result

if __name__ == "__main__":
    calculate_winnings(sample_file)
