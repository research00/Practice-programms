# simple tic tac toe game, demonstration of functions abilities
# instructions

X = "X"
O = "O"
EMPTY = " "
TIE = "Tie"
NUM_SQUARES = 9


def display_instructions():
    '''Prints out the instructions for the player'''
    print(
        '''
    
    Welcome to the tic tac toe game. To make a move, enter a number
    from 0 to 8. That way you select the square to place your figure:
    
     0 | 1 | 2
     ---------
     3 | 4 | 5
     ---------
     6 | 7 | 8
    '''
    )


def ask_yes_no(question):
    '''Asks a question that could be answered with 'yes' or 'no' '''
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response

def ask_number(question, low, high):
    """asks to enter a number within given boundaries"""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response


def pieces():
    '''defines who has the first move'''
    go_first = ask_yes_no("Wanna do the first move? (y/n): ")
    if go_first == "y":
        print("\nAlright, go ahead, you will be playing X'es")
        human = X
        computer = O
    else:
        print("That was a mistake... I'll begin.")
        human = O
        computer = X
    return computer, human


def new_board():
    '''creates a new playing board'''
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board


def display_board(board):
    '''displays a playing board'''
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\t", board[6], "|", board[7], "|", board[8], "\n")

def legal_moves(board):
    '''creates a list of possible moves'''
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves


def winner(board):
    '''defines the winner'''
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
        if EMPTY not in board:
            return TIE
    return None


def human_move(board, human):
    '''defines the human move'''
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Your turn. Pick a spot (0 - 8):", 0, NUM_SQUARES)
        if move not in legal:
            print("\nThere's no way you're making that move!\n")
    print("Ok...")
    return move


def computer_move(board, computer, human):
    board = board[:]
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print("I will choose square №", end=" ")
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        board[move] = EMPTY
    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        board[move] = EMPTY
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move


def next_turn(turn):
    '''performs the turn of the move'''
    if turn == X:
        return O
    else:
        return X


def congrat_winner(the_winner, computer, human):
    '''congratulates the winner'''
    if the_winner != TIE:
        print("Three", the_winner, "in a row!\n")
    else:
        print("\nTie!\n")
    if the_winner == computer:
        print("\nExactly as I had predicted, not surprised at all. You had no chance to win.\n")
    elif the_winner == human:
        print("\nThat can not possibly be true... How could you win? I calculated your every move upfront...")
    elif the_winner == TIE:
        print("\nBy a series of mysterious coincidences, it's a tie. Don't count on that next time!")


def main():
    display_instructions()
    print("\nHope it's clear for you now.")
    computer, human = pieces()
    turn = "X"
    board = new_board()
    display_board(board)
    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)
    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)


main()
input("\n\nPress Enter to exit")
