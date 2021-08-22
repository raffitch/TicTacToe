import random
import numpy as np
import operator
human = 888
computer = 0
human_player = ""
game_turn = 999
empty = 10
played_moves = np.array([empty, empty, empty, empty, empty, empty, empty, empty, empty])
score_points = np.array([0, 0])


def print_grid(moves):
    moves = moves.astype('str')
    moves[moves == str(empty)] = "."
    moves[moves == '0'] = "O"
    moves[moves == '888'] = "X"
    reshaped = moves.reshape((3, 3))
    for row in reshaped:
        for item in row:
            print(item, end="\t    ")
        print("\n\n")


def score(scores):

    score_points[np.argwhere(scores == 1)] += 1
    print(f"Computer:{score_points[0]} | {human_player}:{score_points[1]}")


def player_info():
    global human_player
    print("Welcome to Tic-Tac-toe\n")
    print_grid(np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9]]))
    human_player = input("At your turn type in a cell number 1 to 9 "
                         "to play the game!\nPlease type in your name:").title()
    print(f"Hi {human_player}, you're X. Let's Start!\n")
    initiate_new_game()


def initiate_new_game():
    global game_turn
    reset()
    if game_turn == human:
        print(f"{human_player} start the game")
        play_game()
    elif game_turn == computer:
        print("Computer started the game")
        play_game()
    else:
        game_turn = random.choice([computer, human])
        initiate_new_game()


def reset():
    np.place(played_moves, played_moves < 999, empty)


def try_human_move():
    global game_turn
    try:
        played_cell_nbr = int(input("Type in the cell number and press enter:"))
        if 0 < played_cell_nbr <= 9:
            if played_moves[played_cell_nbr - 1] == empty:
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
    play_again = ''
    while check_winners(played_moves, False) is False:
        if game_turn == computer:
            bot()
        else:
            print_grid(played_moves)
            try_human_move()
    while play_again != 'y':
        play_again = input("Shall we play again? type y/n").lower()
        if play_again == 'n':
            quit()
        else:
            print("Choose between y/n!")
    print(f"Let's play again!")
    initiate_new_game()


def bot():
    global game_turn
    if np.all(played_moves == empty):
        played_moves[random.choice(np.argwhere(played_moves == empty))[0]] = computer
    else:
        played_moves[internal_game(-800, played_moves, operator.gt, computer, False)[0]] = computer
    game_turn = human
    play_game()


def internal_game(best_score, play_moves, op, player, is_max):
    output_data = []
    counter=0
    for i in range(0, play_moves.size):         # TOTAL MOVES ON BOARD - 9
        if play_moves[i] == empty:              # FOR ALL THE POSSIBLE MOVES ON THE BOARD
            play_moves[i] = player                      # PLAY THEM
            print(f"player:{player}")
            counter += 1
            ai_score = ai(play_moves, is_max)           # ASSIGN A SCORE
            print(f"counter:{counter}")
            print_grid(play_moves)
            print(f"ai score is: {ai_score}")
            print("\n")
            print("New Game")
            print("\n")
            play_moves[i] = empty                       # UNDO WHAT YOU JUST DID
            if op(ai_score, best_score):                # IF SCORE IS HIGHER OR LOWER THAN INITIAL SCORE
                best_score = ai_score                   # CHOOSE THAT SCORE
                output_data = [i, best_score]
    return output_data


def ai(ai_moves, is_maximizing):
    if check_winners(ai_moves, True) == computer:
        print("Computer Wins")
        return 1
    elif check_winners(ai_moves, True) == human:
        print("Counter Computer wins")
        return -1
    elif check_winners(ai_moves, True) == 999:
        print
        return 0

    if is_maximizing:
        return internal_game(-800, ai_moves, operator.gt, computer, False)[1]
    else:
        return internal_game(800, ai_moves, operator.lt, human, True)[1]


def check_winners(moves, is_simulation):
    global game_turn
    reshaped = moves.reshape((3, 3))
    x = np.sum(reshaped, axis=0)
    y = np.sum(reshaped, axis=1)
    diag1 = np.sum(np.diagonal(reshaped))
    diag2 = np.sum(np.fliplr(reshaped).diagonal())
    if np.any(x == 0) or np.any(y == 0) or diag1 == 0 or diag2 == 0:
        if is_simulation is False:
            print_grid(played_moves)
            print("Computer Wins!")
            score(np.array([1, 0]))
            game_turn = computer
            return True
        else:
            return computer
    elif np.any(x == human*3) or np.any(y == human*3) or diag1 == human*3 or diag2 == human*3:
        if is_simulation is False:
            print(f"{human_player} you win!")
            score(np.array([0, 1]))
            game_turn = human
            return True
        else:
            return human
    elif empty not in moves:
        if is_simulation is False:
            print("It's a Draw!")
            game_turn = 999
            return True
        else:
            return 999
    if is_simulation is False:
        return False


player_info()

