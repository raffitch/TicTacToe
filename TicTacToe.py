import random
import numpy as np

human = 1
computer = 0
human_player = ""
score_x = 0
score_o = 0
game_turn = 10


def print_grid(values):
    if type(values) is not list:
        values = values.astype('str')
        values[values == '10'] = ""
        values[values == '0'] = "O"
        values[values == '1'] = "X"

    print("\t     |     |")
    print(f"\t  {values[0]}  |  {values[1]}  |  {values[2]}")
    print('\t_____|_____|_____')

    print("\t     |     |")
    print(f"\t  {values[3]}  |  {values[4]}  |  {values[5]}")
    print('\t_____|_____|_____')

    print("\t     |     |")

    print(f"\t  {values[6]}  |  {values[7]}  |  {values[8]}")
    print("\t     |     |")


def score():
    print("---------------------")
    print("        SCORE        ")
    print("---------------------")
    print("   ", "Computer")
    print("   ", score_o)
    print("\n")
    print("   ", human_player)
    print("   ", score_x)
    print("---------------------\n")


def player_info():
    global human_player
    default_cell_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("Welcome to Tic-Tac-toe")
    print_grid(default_cell_values)
    human_player = input("At your turn type in a cell number 1 to 9 "
                         "to play the game!\nPlease type in your name:").title()
    print(f"Hi {human_player}, you're X. Let's Start!\n")
    initiate_new_game()


def initiate_new_game():
    global game_turn
    default_moves = np.array([10, 10, 10, 10, 10, 10, 10, 10, 10])
    if game_turn == computer:
        print("Computer won so it starts the game!")
        play_game(default_moves)
    elif game_turn == human:
        print(f"{human_player}, you won, start the new game!")
        print_grid(default_moves)
        try_human_move(default_moves)
    else:
        turn = random.choice([computer, human])
        if turn == computer:
            print(f"Computer starts the game")
            play_game(default_moves)
        else:
            try_human_move(default_moves)


def try_human_move(played_moves):
    try:
        played_cell_nbr = int(input("Type in the cell number and press enter:"))
        if 0 < played_cell_nbr <= 9:
            if played_moves[played_cell_nbr - 1] == 10:
                try:
                    played_moves[played_cell_nbr - 1] = human
                except IndexError:
                    print("wtf")
                play_game(played_moves)
            else:
                print(f"{human_player} that cell is taken, please try again!")
                try_human_move(played_moves)
        else:
            print(f"{human_player} that's not a valid cell number, please try again!")
            try_human_move(played_moves)

    except ValueError:
        print("That's not a valid choice, please try again!")
        try_human_move(played_moves)


def play_game(played_moves):
    played_moves[random.choice(np.argwhere(played_moves == 10))] = computer
    print_grid(played_moves)
    while check_winners(played_moves) is False:
        try_human_move(played_moves)
    else:
        score()
        print(f"Let's play again! {human_player}")
        initiate_new_game()


def check_winners(played_moves):
    global score_x
    global score_o
    global game_turn
    reshaped = played_moves.reshape((3, 3))
    x = np.sum(reshaped, axis=0)
    y = np.sum(reshaped, axis=1)
    diag1 = np.sum(np.diagonal(reshaped))
    diag2 = np.sum(np.fliplr(reshaped).diagonal())

    if np.any(x == 0) or np.any(y == 0) or diag1 == 0 or diag2 == 0:
        print("The computer has won!")
        score_o += 1
        game_turn = computer
        return True
    elif np.any(x == 3) or np.any(y == 3) or diag1 == 3 or diag2 == 3:
        print(f"{human_player} has won!")
        score_x += 1
        game_turn = human
        return True
    elif 10 not in played_moves:
        game_turn = 10
        print("It's a Draw!")
    else:
        print(f"It's your turn {human_player}")
        return False


player_info()
