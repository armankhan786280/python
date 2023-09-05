import random

# Create a deck of cards with pairs of values
def create_deck(size):
    deck = list(range(1, size // 2 + 1)) * 2
    random.shuffle(deck)
    return deck

# Display the game board
def display_board(board):
    for row in board:
        print(" ".join(map(str, row)))

# Main game logic
def memory_game(size):
    deck = create_deck(size)
    board = [["X" for _ in range(size)] for _ in range(size)]
    matched_pairs = 0

    while matched_pairs < size // 2:
        display_board(board)

        # Get user input for the first card
        while True:
            try:
                row1 = int(input("Enter the row for the first card (0 to {}): ".format(size - 1)))
                col1 = int(input("Enter the column for the first card (0 to {}): ".format(size - 1)))
                if 0 <= row1 < size and 0 <= col1 < size and board[row1][col1] == "X":
                    break
                else:
                    print("Invalid input. Try again.")
            except ValueError:
                print("Invalid input. Try again.")

        card1 = deck[row1 * size + col1]
        board[row1][col1] = card1
        display_board(board)

        # Get user input for the second card
        while True:
            try:
                row2 = int(input("Enter the row for the second card (0 to {}): ".format(size - 1)))
                col2 = int(input("Enter the column for the second card (0 to {}): ".format(size - 1)))
                if 0 <= row2 < size and 0 <= col2 < size and board[row2][col2] == "X":
                    break
                else:
                    print("Invalid input. Try again.")
            except ValueError:
                print("Invalid input. Try again.")

        card2 = deck[row2 * size + col2]
        board[row2][col2] = card2
        display_board(board)

        if card1 == card2:
            print("Match found!")
            matched_pairs += 1
        else:
            print("No match. Try again.")
            board[row1][col1] = "X"
            board[row2][col2] = "X"

    print("Congratulations! You've found all the pairs!")

if _name_ == "_main_":
    size = int(input("Enter the size of the game board (even number): "))
    if size % 2 != 0:
        print("Please enter an even number for the board size.")
    else:
        memory_game(size)