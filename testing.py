# # Create class
# class Init:
#     def __init__(self, init_: bool):
#         self.init = init_# Create Instance of the class
#
# init_ = Init(False)
# def run():
#     print('Will Run')    if init_.init:
#         print( 'Already initiated' )
#     if not init_.init:
#         init()def init():
#     init_.init = True
#     print('Will Init')run()
# run()
# Output:Will Run
# Will Init
# Will Run
# Already initiated
#
#
# INIT = Falsedef run():
#     global INIT
#     print('Will Run')
#     if INIT:
#         print( 'Already initiated' )
#     if not INIT:
#         init()def init():
#     global INIT
#     INIT = True
#     print('Will Init')run()
# run()OUTPUT:Will Run
# Will Init
# Will Run
# Already initiated
import numpy as np

board = np.array([1,0,1,
                  1,1,0,
                  0,1,0])

def check_winner(moves):
    reshaped1 = moves.reshape((3, 3))
    x = np.sum(reshaped1, axis=0)
    y = np.sum(reshaped1, axis=1)
    diag1 = np.sum(np.diagonal(reshaped1))
    diag2 = np.sum(np.fliplr(reshaped1).diagonal())
    if np.any(x == 0) or np.any(y == 0) or diag1 == 0 or diag2 == 0:
        return 'computer'
    elif np.any(x == 3) or np.any(y == 3) or diag1 == 3 or diag2 == 3:
        return 'human'
    elif 10 not in moves:
        return 999
print(check_winner(board))