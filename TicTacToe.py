import random
import numpy as np

human = 1
computer = 0
human_player = ""

game_turn = 10
played_moves = np.array([10, 10, 10, 10, 10, 10, 10, 10, 10])
default_cell_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def print_grid(grid):
    if type(grid) is not list:
        grid = grid.astype('str')
        grid[grid == '10'] = ""
        grid[grid == '0'] = "O"
        grid[grid == '1'] = "X"

    print("\t     |     |")
    print(f"\t  {grid[0]}  |  {grid[1]}  |  {grid[2]}")
    print('\t_____|_____|_____')
    print("\t     |     |")
    print(f"\t  {grid[3]}  |  {grid[4]}  |  {grid[5]}")
    print('\t_____|_____|_____')
    print("\t     |     |")
    print(f"\t  {grid[6]}  |  {grid[7]}  |  {grid[8]}")
    print("\t     |     |")


def score(score_x, score_o):
    score_x += score_x
    score_o += score_o
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

    print("Welcome to Tic-Tac-toe")
    print_grid(default_cell_values)
    human_player = input("At your turn type in a cell number 1 to 9 "
                         "to play the game!\nPlease type in your name:").title()
    print(f"Hi {human_player}, you're X. Let's Start!\n")
    initiate_new_game()


def initiate_new_game():
    global game_turn
    reset()
    if game_turn == computer:
        print("Computer won so it starts the game!")
        play_game()
    elif game_turn == human:
        print(f"You won, start the new game!")
        print_grid(played_moves)
        try_human_move()
    else:
        turn = random.choice([computer, human])
        if turn == computer:
            print(f"Computer starts the game")
            play_game()
        else:
            try_human_move()


def reset():
    np.place(played_moves, played_moves < 999, 10)


def try_human_move():
    try:
        played_cell_nbr = int(input("Type in the cell number and press enter:"))
        if 0 < played_cell_nbr <= 9:
            if played_moves[played_cell_nbr - 1] == 10:
                played_moves[played_cell_nbr - 1] = human
                play_game()
            else:
                print(f"{human_player} that cell is taken, please try again!")
                try_human_move()
        else:
            print(f"{human_player} that's not a valid cell number, please try again!")
            try_human_move()

    except ValueError:
        print("That's not a valid choice, please try again!")
        try_human_move()


def play_game():
    played_moves[random.choice(np.argwhere(played_moves == 10))] = computer
    print_grid(played_moves)
    while check_winners() is False:
        try_human_move()
    else:
        print(f"Let's play again! {human_player}")
        initiate_new_game()


def check_winners():
    global game_turn
    reshaped = played_moves.reshape((3, 3))
    x = np.sum(reshaped, axis=0)
    y = np.sum(reshaped, axis=1)
    diag1 = np.sum(np.diagonal(reshaped))
    diag2 = np.sum(np.fliplr(reshaped).diagonal())

    if np.any(x == 0) or np.any(y == 0) or diag1 == 0 or diag2 == 0:
        print("The computer has won!")
        score(0, 1)
        game_turn = computer
        return True
    elif np.any(x == 3) or np.any(y == 3) or diag1 == 3 or diag2 == 3:
        print(f"{human_player} has won!")
        score(1, 0)
        game_turn = human
        return True
    elif 10 not in played_moves:
        game_turn = 10
        print("It's a Draw!")
    else:
        print(f"It's your turn {human_player}")
        return False


player_info()
