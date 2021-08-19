import random
import numpy as np

human = 1
computer = 0
human_player = ""
game_turn = 999
played_moves = np.array([10, 10, 10, 10, 10, 10, 10, 10, 10])
default_cell_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
score_points = np.array([0, 0])


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


def score(scores):

    score_points[np.argwhere(scores == 1)] += 1
    print("---------------------")
    print("        SCORE        ")
    print("---------------------")
    print("   ", "Computer")
    print("   ", score_points[0])
    print("\n")
    print("   ", human_player)
    print("   ", score_points[1])
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
    if game_turn == human:
        print(f"{human_player} starts the game")
        play_game()
    elif game_turn == computer:
        print("Computer started the game")
        play_game()
    else:
        game_turn = random.choice([computer, human])
        initiate_new_game()


def reset():
    np.place(played_moves, played_moves < 999, 10)


def try_human_move():
    global game_turn
    try:
        played_cell_nbr = int(input("Type in the cell number and press enter:"))
        if 0 < played_cell_nbr <= 9:
            if played_moves[played_cell_nbr - 1] == 10:
                played_moves[played_cell_nbr - 1] = human
                game_turn = computer
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
    while check_winners() is False:
        if game_turn == computer:
            bot()
        else:
            print_grid(played_moves)
            try_human_move()
    print(f"Let's play again!")
    initiate_new_game()


# def bot():
#     global game_turn
#     played_moves[random.choice(np.argwhere(played_moves == 10))[0]] = computer
#     game_turn = human
#     play_game()

def bot():
    global game_turn
    best_score = -800
    best_move = 0
    for i in range(0, played_moves.size):
        if played_moves[i] == 10:
            played_moves[i] = computer
            ai_score = minimax(played_moves, 0, False)
            played_moves[i] = 10
            if ai_score > best_score:
                best_score = ai_score
                best_move = i

    played_moves[best_move] = computer
    game_turn = human
    play_game()



def minimax(played_moves, depth, is_maximizing):
    if check_winner(played_moves) == computer:
        return 1
    elif check_winner(played_moves) == human:
        return -1
    elif check_winner(played_moves) == 999:
        return 0

    if is_maximizing:
        best_score = -800
        for i in range(0, played_moves.size):
            if played_moves[i] == 10:
                played_moves[i] = computer
                ai_score = minimax(played_moves, depth + 1, False)
                played_moves[i] = 10
                if ai_score > best_score:
                    best_score = ai_score
        return best_score
    else:
        best_score = 800
        for i in range(0, played_moves.size):
            if played_moves[i] == 10:
                played_moves[i] = human
                ai_score = minimax(played_moves, depth + 1, True)
                played_moves[i] = 10
                if ai_score < best_score:
                    best_score = ai_score
        return best_score


def check_winners():
    global game_turn
    reshaped = played_moves.reshape((3, 3))
    x = np.sum(reshaped, axis=0)
    y = np.sum(reshaped, axis=1)
    diag1 = np.sum(np.diagonal(reshaped))
    diag2 = np.sum(np.fliplr(reshaped).diagonal())
    if np.any(x == 0) or np.any(y == 0) or diag1 == 0 or diag2 == 0:
        print("The computer has won!")
        score(np.array([1, 0]))
        game_turn = computer
        return True
    elif np.any(x == 3) or np.any(y == 3) or diag1 == 3 or diag2 == 3:
        print(f"{human_player} has won!")
        score(np.array([0, 1]))
        game_turn = human
        return True
    elif 10 not in played_moves:
        print("It's a Draw!")
        game_turn = 999
        return True
    else:
        return False


def check_winner(moves):
    reshaped1 = moves.reshape((3, 3))
    x = np.sum(reshaped1, axis=0)
    y = np.sum(reshaped1, axis=1)
    diag1 = np.sum(np.diagonal(reshaped1))
    diag2 = np.sum(np.fliplr(reshaped1).diagonal())
    if np.any(x == 0) or np.any(y == 0) or diag1 == 0 or diag2 == 0:
        return computer
    elif np.any(x == 3) or np.any(y == 3) or diag1 == 3 or diag2 == 3:
        return human
    elif 10 not in moves:
        return 999


player_info()
