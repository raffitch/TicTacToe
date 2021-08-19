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
computer = True
human= False
draw= True
checkvalue = 0
def test(value, value2):

    global checkvalue
    if value:
        return 1
    elif value == 2:
        return -1
    elif value == 3:
        return 0

    if value2:
        best_score = 800
        checkvalue = best_score
        return best_score
    else:
        best_score = -800
        checkvalue = best_score
        return best_score

print(test(True,True))
print(checkvalue)
