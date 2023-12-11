from collections import Counter

input_file = 'day07/input.txt'
sample_file = 'day07/sample.txt'

def card_to_int(card: str) -> int:
    decimal_representations = {}
    decimal_representations['A'] = 14
    decimal_representations['K'] = 13
    decimal_representations['Q'] = 12
    decimal_representations['J'] = 11
    decimal_representations['T'] = 10
    decimal_representations['9'] = 9
    decimal_representations['8'] = 8
    decimal_representations['7'] = 7
    decimal_representations['6'] = 6
    decimal_representations['5'] = 5
    decimal_representations['4'] = 4
    decimal_representations['3'] = 3
    decimal_representations['2'] = 2
    return decimal_representations[card]

def hand_to_list(hand: str) -> list:
    hand_list = [card_to_int(x) for x in list(hand)]
    return hand_list

def calculate_winnings(data_file) -> int:
    result = 0
    data = open(data_file).read().strip().splitlines()

    cards = "AKQJT98765432"

    hands = {}
    for play in data:
        hand = play.split()[0].strip()
        hand_list = hand_to_list(hand)
        bid = int(play.split()[1].strip())
        # print("Hand {} with bid {}".format(hand, bid))

        c = Counter(hand_list)
        # Alternatives to counter:
        # (1)
        # hand_values = pd.Series(list(hand))
        # (2)
        # hand_value = {}
        # for card in cards:
        #     if hand.count(card) > 0:
        #         hand_value[card_to_int(card)] = hand.count(card)
        # sorted_hand_value = dict(sorted(hand_value.items(), key=lambda item: item[1], reverse=True))
        # print(sorted_hand_value)
        # print(c)
        # print(c.most_common(1)[0][1])
        hands[hand] = (c, bid)
    # for key in hands:
    #     print("---")
    #     print("Key most:   {}".format(key))
    #     print("Amount:     {}".format(hands[key][0].most_common(1)[0][1]))
    #     print("Card:       {}".format(hands[key][0].most_common(1)[0][0]))
    #     # print(hands[key][1])
    #     print("Key second: {}".format(key))
    #     print("Amount:     {}".format(hands[key][0].most_common(2)[1][1]))
    #     print("Card:       {}".format(hands[key][0].most_common(2)[1][0]))

    return result

if __name__ == "__main__":
    calculate_winnings(sample_file)
