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

def play_recursive_war(p1_deck: list, p2_deck: list, game: int = 1):
    winner = 0
    p1 = copy.deepcopy(p1_deck)
    p2 = copy.deepcopy(p2_deck)
    round = 0
    identi_order = list()
    while winner == 0:
        round += 1
        # Insta win condition
        if len(identi_order) > 0 and (tuple(p1), tuple(p2)) in identi_order:
            print('P1 is Winner through insta-win condition...')
            print(identi_order)
            return 1, p1
        identi_order.append((tuple(p1), tuple(p2)))
        # Continue normally
        print(f'-- Round {round} (Game {game}) --')
        print(f'Player 1 deck: ', ', '.join(str(x) for x in p1))
        print(f'Player 2 deck: ', ', '.join(str(y) for y in p2))
        p1_plays = p1.pop(0)
        p2_plays = p2.pop(0)
        print(f'Player 1 plays:', p1_plays)
        print(f'Player 2 plays:', p2_plays)
        # Possible recursive combat
        recurse = bool((len(p1) >= int(p1_plays)) and (len(p2) >= int(p2_plays)))
        if recurse:
            print('Playing a sub-game to determine the winner...')
            p1_for_rec = p1[:int(p1_plays)]
            p2_for_rec = p2[:int(p2_plays)]            
            sub_winner, win_deck = play_recursive_war(p1_for_rec, p2_for_rec, game + 1)
            print('Now back to game ',game)
            if sub_winner == 1:
                print(f'Player 1 Wins round {round} of game {game}!')
                p1.append(p1_plays)
                p1.append(p2_plays)
                if len(p2) == 0:
                    winner = 1
                    return winner, p1
            elif sub_winner == 2:
                print(f'Player 2 Wins round {round} of game {game}!')
                p2.append(p2_plays)
                p2.append(p1_plays)
                if len(p1) == 0:
                    winner = 2
                    return winner, p2
        # Recursive combat not needed
        else:
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
winner, deck = play_recursive_war(p1, p2)
score = score_winning_deck(deck)
print('Winning score of: ', score)
