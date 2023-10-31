from sys import argv

# Check if the correct number of command-line arguments is provided
if len(argv) is not 2:
    print('Usage: nqueens N')
    exit(1)

# Check if the provided argument is a valid integer
if not argv[1].isdigit():
    print('N must be a number')
    exit(1)

N = int(argv[1])

# Ensure N is at least 4, as the problem is not meaningful for smaller N
if N < 4:
    print('N must be at least 4')
    exit(1)

# Function to add a column of zeroes to a chessboard
def board_column_gen(board=[]):
    if len(board):
        for row in board:
            row.append(0)
    else:
        for row in range(N):
            board.append([0])
    return board

# Function to add a queen to the board
def add_queen(board, row, col):
    board[row][col] = 1

# Function to check if it's safe to place a new queen in a given position
def new_queen_safe(board, row, col):
    x = row
    y = col
    for i in range(1, N):
        if (y - i) >= 0:
            if (x - i) >= 0:
                if board[x - i][y - i]:
                    return False
            if board[x][y - i]:
                return False
            if (x + i) < N:
                if board[x + i][y - i]:
                    return False
    return True

# Function to convert chessboard with queens into coordinates
def coordinate_format(candidates):
    holberton = []
    for x, attempt in enumerate(candidates):
        holberton.append([])
        for i, row in enumerate(attempt):
            holberton[x].append([])
            for j, col in enumerate(row):
                if col:
                    holberton[x][i].append(i)
                    holberton[x][i].append(j)
    return holberton

# Initialize candidates list with the first column of 0s
candidates = []
candidates.append(board_column_gen())

# Iterate column by column to find solutions
for col in range(N):
    new_candidates = []  # Store new candidate solutions
    for matrix in candidates:  # Iterate through previous candidates
        for row in range(N):  # Try placing a queen in each row
            if new_queen_safe(matrix, row, col):  # Check if it's safe
                temp = [line[:] for line in matrix]  # Create a new candidate
                add_queen(temp, row, col)  # Place a queen
                if col < N - 1:  # Add a new column for the next round
                    board_column_gen(temp)
                new_candidates.append(temp)  # Add the new candidate
    candidates = new_candidates  # Update candidates for the next round

# Format results and print the list of queen coordinates
for item in coordinate_format(candidates):
    print(item)

