# Global variables
boxes = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
move_count = 0

# Function to display the board
def display():
    global move_count
    for row in boxes:
        print("|", end=" ")
        for element in row:
            print(element, end=" | ")
        print("\n")

# Function to handle player moves
def player(move):
    global move_count
    if not move.isdigit() or int(move) < 1 or int(move) > 9:  # Validate move
        print("Invalid move. Please enter a number between 1 and 9.")
        return False

    move = int(move)  # Convert the move to an integer
    replaced = False
    for row in boxes:
        if str(move) in row:  # Check if the move is available in the row
            row[row.index(str(move))] = "O" if move_count % 2 == 0 else "X"
            replaced = True
            break

    if not replaced:
        print("Invalid move. Position already taken.")
        return False

    move_count += 1  # Increment the move count after a valid move
    return True

# Main game loop
while True:
    display()
    if move_count >= 9:  # End the game after 9 moves
        print("End of game")
        break

    move = input("Enter your move (1-9): ")
    if not player(move):
        continue  # Retry if the move is invalid
