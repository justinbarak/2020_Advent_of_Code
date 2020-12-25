import regex
import copy
from functools import reduce

def load(filename: str) -> list:
    """Open a text file & return a list of lowercase strings."""
    try:
        with open(filename) as in_file:
            loaded_txt = in_file.read().strip().split("\n")
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as e:
        print("{}\nError opening {}. Terminating program.".format(e, filename))

def play_war(p1_deck: list, p2_deck: list):
    winner = 0
    p1 = copy.deepcopy(p1_deck)
    p2 = copy.deepcopy(p2_deck)
    round = 0
    while winner == 0:
        round += 1
        print(f'-- Round {round} --')
        print(f'Player 1 deck: ', ', '.join(str(x) for x in p1))
        print(f'Player 2 deck: ', ', '.join(str(y) for y in p2))
        p1_plays = p1.pop(0)
        p2_plays = p2.pop(0)
        print(f'Player 1 plays:', p1_plays)
        print(f'Player 2 plays:', p2_plays)
        if int(p1_plays) > int(p2_plays):
            print('Player 1 Wins the Round!')
            p1.append(p1_plays)
            p1.append(p2_plays)
            if len(p2) == 0:
                winner = 1
                return winner, p1
        elif int(p1_plays) < int(p2_plays):
            print('Player 2 Wins the Round!')
            p2.append(p2_plays)
            p2.append(p1_plays)
            if len(p1) == 0:
                winner = 2
                return winner, p2
        else:
            raise NotImplementedError("Cards should not be equal...")
    return None
    # winning player number, deck at end as list

def score_winning_deck(deck: list) -> int:
    point_array = list(range(1, len(deck) + 1))
    point_array.reverse()
    points = 0
    for card, point in zip(deck, point_array):
        points += int(card) * point
    return points

assert score_winning_deck([1,2]) == 4

def read_card_input(deck_input: list) -> list:
    p1 = []
    p2 = []
    i = 0
    active_p = 1
    while i < len(deck_input):
        try:
            if active_p == 1:
                p1.append(int(deck_input[i]))
            elif active_p == 2:
                p2.append(int(deck_input[i]))
            else:
                raise NotImplementedError("Only 2 Players were anticipated...")
        except:
            if deck_input[i] == '':
                active_p += 1
        i += 1
    return p1, p2

deck_input = load('Day22A-input.txt')

p1, p2 = read_card_input(deck_input)
winner, deck = play_war(p1, p2)
score = score_winning_deck(deck)
print('Winning score of: ', score)
