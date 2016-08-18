# Import
import random

# Body
def get_random():
    rand_num = random.randint(1, 3)
    return rand_num

def player2(remain, player1_win_count, player2_win_count, marble_seque):
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
        player1_win_count += 1
    # if not, game continues
    marble_seque.append(str(each_move))
    return remain, player1_win_count, marble_seque

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

def current_player1_move(game_num, seque_index):
    # determine the game number, and the current move
    current_move = player1_seque_indx()[game_num - 1][seque_index]
    return current_move

def player1(remain, current_move, player1_win_count, player2_win_count, marble_seque):
    # check if the marbles left is fewer than the current number
    # if so, remove all. Once all marbles are removed, declare the winner, and start a new game
    if current_move >= remain:
        current_move = remain
        player2_win_count += 1
        remain = 0
    # if not, game continues
    else:
        remain -= current_move
    marble_seque.append(str(current_move))
    return remain, player2_win_count, marble_seque

def play_game():
    with open("i206_placein_output2_y.liu.txt", "w") as fin:
        player1_index = player1_seque_indx()
        game_num = 1
        player1_win_count = 0
        player2_win_count = 0
        total_game_num = len(player1_index)
        winner = None
        while game_num <= total_game_num:
            marble_seque = []
            fin.write("Game #{}. Play sequence: ".format(game_num))
            remain = 17
            seque_index = 0
            while remain > 0:
                current_move = current_player1_move(game_num, seque_index)
                (remain, player2_win_count, marble_seque) = player1(remain, current_move, player1_win_count, player2_win_count, marble_seque)
                seque_index += 1
                # check if player 1 removes all the marbles
                if remain != 0:
                    (remain, player1_win_count, marble_seque) = player2(remain, player1_win_count, player2_win_count, marble_seque)
            if len(marble_seque) % 2 == 0:
                # Player 1 always starts first.
                winner = "P1"
            else:
                winner = "P2"
            fin.write("Game #{}. Play sequence: {}. Winner: {}\n".format(str(game_num), "-".join(marble_seque), winner))
            game_num += 1
        fin.write("Player 1 won {} times; Player 2 won {} times.".format(str(player1_win_count), str(player2_win_count)))

def save_output():
        play_game()


def main():
    save_output()

if __name__ == "__main__":
    main()
