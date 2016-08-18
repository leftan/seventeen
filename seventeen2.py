# Import
import random

# Body
def get_random():
    rand_num = random.randint(1, 3)
    return rand_num

def player2(remain, game_num, player1_win_count, player2_win_count):
    '''player2 removes marbles randomly
    remain: the marbles left, int'''
    remain_check = None
    while True:
        each_move = get_random()
        # player2 couldn't remove marbles more than the ones left.
        # If so, get another random num.
        remain_check = remain - each_move
        if remain_check < 0:
            continue
        else:
            break
    remain = remain_check
    # check if player2 removes all the remaining marbles
    # if so, declare the winner, and start the next game.
    if remain == 0:
        print("{}. Winner: P1".format(each_move))
        player1_win_count += 1
    # if not, game continues
    else:
        print("{}-".format(each_move), end='')
    return remain, player1_win_count

def player1_seque_indx():
    '''read the input file, and store player1's sequences of moves for each game as a tuple
    game # is the list index'''
    player1_seque = []
    with open("i206_placein_input_0.txt", 'r') as fin:
        for line in fin:
            line = line.strip()
            # store sequences of moves for each game as a tuple
            game_seque = tuple([int(each) for each in line.split(",")])
            player1_seque.append(game_seque)
    return player1_seque

def player1(remain, game_num, seque_index, player1_win_count, player2_win_count):
    # determine the game number, and the current move
    current_move = player1_seque_indx()[game_num - 1][seque_index]
    # check if the marbles left is fewer than the current number
    # if so, remove all. Once all marbles are removed, declare the winner, and start a new game
    if current_move >= remain:
        print("{}. Winner: P2".format(remain))
        player2_win_count += 1
        remain = 0
    # if not, game continues
    else:
        print("{}-".format(current_move), end='')
        remain -= current_move
        seque_index += 1
    return remain, seque_index, player2_win_count

def check_game_num(player1_win_count, player2_win_count):
#     '''once the current game is over, start a new game, until there is no line in the input file'''
    print("Player 1 won {} times; Player 2 won {} times.".format(player1_win_count, player2_win_count))


def main():
    player1_index = player1_seque_indx()
    game_num = 1
    player1_win_count = 0
    player2_win_count = 0
    total_game_num = len(player1_index)
    while game_num <= total_game_num:
        print("Game #{}. Play sequence: ".format(game_num), end='')
        remain = 17
        seque_index = 0
        while remain > 0:
            (remain, seque_index, player2_win_count) = player1(remain, game_num, seque_index, player1_win_count, player2_win_count)
            # check if player 1 removes all the marbles
            if remain != 0:
                (remain, player1_win_count) = player2(remain, game_num, player1_win_count, player2_win_count)
        game_num += 1
    check_game_num(player1_win_count, player2_win_count)


if __name__ == "__main__":
    main()
