# define swap function with two parameters
import time


# Classic nested loops using ij indexes
def print_matrix1(matrix):
    print("Classic nested loops using ij indexes")
    for i in range(len(matrix)):  # outer loop (i), built on length of matrix (rows)
        for j in range(len(matrix[i])):  # inner loop (j), built on length of items (columns)
            print(matrix[i][j], end=" ")  # [i][j] is 2D representation, end changes newline to space
        print()


# Enhanced nested for loops
def print_matrix2(matrix):
    print("Enhanced nested for loops")
    for row in matrix:  # short hand row iterator, index is not required
        for col in row:  # short hand column iterator
            print(col, end=" ")
        print()


# For loop with shortcut (*) row expansion (courtesy Raiden)
def print_matrix3(matrix):
    print("For loop with shortcut (*) row expansion")
    for row in matrix:
        print(*row)  # pythons has (*) that is one line expansion of row into columns


def driver():
    # setup some text matrices
    keypad = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9],
              [" ", 0, " "]]

    keyboard = [["`", 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, "-", "="],
                ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "[", "]"],
                ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";", "'"],
                ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"]]

    numbers = [[0, 1],
               [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
               [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F"]]

    # pack into a list of matrices with titles
    matrices = [["Keypad", keypad], ["Keyboard", keyboard], ["Number Systems", numbers]]

    # print each matrix using defined functions
    for title, matrix in matrices:  # unpack matrix with title
        print(title, len(matrix), "x", "~" + str(len(matrix[0])))  # formatted message with concatenation
        print_matrix1(matrix)
        print_matrix2(matrix)
        print_matrix3(matrix)
        print()


def swap():
    c = int(input('Whats your first number?:'))
    d = int(input('Whats your second number?:'))
    c,d = swap1(c,d)
    print(c,d)

def swap1(a,b):
    if a > b:
        b, a = a, b  # swap values
    else:
        a, b = a, b
    return a, b  # return 2 values


#funcy.py
# terminal print commands
ANSI_CLEAR_SCREEN = u"\u001B[2J"
ANSI_HOME_CURSOR = u"\u001B[0;0H\u001B[2"
OCEAN_COLOR = u"\u001B[44m\u001B[2D"
SHIP_COLOR = u"\u001B[32m\u001B[2D"
RESET_COLOR = u"\u001B[0m\u001B[2D"

def ocean_print():
    # print ocean
    print(ANSI_CLEAR_SCREEN, ANSI_HOME_CURSOR)
    print("\n\n\n\n")
    print(OCEAN_COLOR + "  " * 35)


# print ship with colors and leading spaces
def ship_print(position):
    print(ANSI_HOME_CURSOR)
    print(RESET_COLOR)
    sp = " " * position
    print(sp + "  (\(\   ")
    print(sp + "  ( -.-)   ")
    print(SHIP_COLOR, end="")
    print(sp + "  o_()() ")
    print(sp + " \____/  ")
    print(RESET_COLOR)


# ship function, iterface into this file
def ship():
    # only need to print ocean once
    ocean_print()

    # loop control variables
    start = 0  # start at zero
    distance = 60  # how many times to repeat
    step = 2  # count by 2

    # loop purpose is to animate ship sailing
    for position in range(start, distance, step):
        ship_print(position)  # call to function with parameter
        time.sleep(.1)




