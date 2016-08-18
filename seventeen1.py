# Import
import random

# Body
def get_random():
    rand_num = random.randint(1, 3)
    return rand_num

def computer_play(remain):
    '''the computer removes marbles randomly
    remain: the marbles left, int'''
    print("Computer's turn...")
    remain_check = None
    while True:
        computer_removed_num = get_random()
        # computer couldn't remove marbles more than the ones left.
        # If so, get another random num.
        remain_check = remain - computer_removed_num
        if remain_check < 0:
            continue
        else:
            remain = remain_check
            print("Computer removed {} marbles.".format(computer_removed_num))
            # check if the computer removes all the remaining marbles
            if remain == 0:
                print("\n" + "There are no marbles left. You win!")
                quit()
            else:
                break
    return remain

def marbles_left(remain):
    '''the prompt prints how many marbles left'''
    print("Number of marbles left in jar: {} \n".format(remain))


def human_play(remain):
    '''human go first, enter 1, 2, 3
    remain: the marbles left, int'''
    removed_num = None
    invalid = "Sorry, that is not a valid option. Try again!"
    promt = "Your turn: How many marbles will you remove (1-3)? "
    while True:
        marbles_left(remain)
        # the input from user should be an int.
        try:
            removed_num = int(input(promt))
        except ValueError:
            print(invalid)
            continue
        # user can only remove 1-3 marbles.
        # user cannot remove marbles more than the ones left.
        if removed_num > 3 or removed_num < 1 or removed_num > remain:
            print(invalid)
            continue
        else:
            remain -= removed_num
            print("You removed {} marbles.".format(removed_num))
            break
    # check if the user removes all the remaining marbles
    if remain == 0:
        print("\n" + "There are no marbles left. Computer wins!")
        quit()
    else:
        marbles_left(remain)
    return remain

def control_flow(remain):
    while True:
        remain = human_play(remain)
        remain = computer_play(remain)

def main():
    remain = 17
    print("Let's play the game of Seventeen!")
    control_flow(remain)

if __name__ == "__main__":
    main()