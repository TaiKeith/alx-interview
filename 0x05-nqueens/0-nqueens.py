#!/usr/bin/python3
import sys


def print_usage_and_exit():
    """
    Prints usage instructions and exits the program with a status of 1.
    This is called when the user provides incorrect input.
    """
    print("Usage: nqueens N")
    sys.exit(1)

def validate_input():
    """
    Validates the input from the command line. Ensures that:
      - Only one argument is provided.
      - The argument is a number greater than or equal to 4.
    Returns:
      - The integer value of N if valid.
    """
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print_usage_and_exit()

    # Try to convert the argument to an integer
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is at least 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    return N

def is_safe(board, row, col):
    """
    Checks if it's safe to place a queen at the given (row, col) position.
    A queen placement is considered safe if it doesn't share the same column,
    or diagonal with any previously placed queens.
    
    Parameters:
      - board: List tracking the column position of queens in each row.
      - row: The current row where we want to place the queen.
      - col: The column where we want to place the queen.
    
    Returns:
      - True if the position is safe, False otherwise.
    """
    for i in range(row):
        # Check if another queen is in the same column or on the same diagonal
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(N):
    """
    Solves the N-Queens problem using backtracking.
    It recursively tries to place queens in each row while following the N-Queens rules.
    
    Parameters:
      - N: Size of the chessboard (N x N) and number of queens.
    
    Returns:
      - A list of solutions, where each solution is a list of (row, column) positions.
    """
    def backtrack(row):
        """
        Recursive helper function to place queens row by row.
        If a valid solution is found, it's added to the list of solutions.
        
        Parameters:
          - row: The current row where we are trying to place a queen.
        """
        # If all rows are filled, a solution is found
        if row == N:
            solutions.append([[i, board[i]] for i in range(N)])
            return

        # Try placing a queen in each column of the current row
        for col in range(N):
            if is_safe(board, row, col):
                board[row] = col  # Place the queen
                backtrack(row + 1)  # Move to the next row
                board[row] = -1  # Reset the row for backtracking

    solutions = []  # List to store all the solutions
    board = [-1] * N  # Initialize board with -1 (no queen placed)
    backtrack(0)  # Start backtracking from the first row
    return solutions

def main():
    """
    Main function to validate input, solve the N-Queens problem, and print solutions.
    """
    # Validate input and get the board size
    N = validate_input()

    # Find all solutions to the N-Queens problem
    solutions = solve_nqueens(N)

    # Print each solution
    for solution in solutions:
        print(solution)

# Run the program if this file is executed directly
if __name__ == "__main__":
    main()
