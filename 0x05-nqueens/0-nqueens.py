#!/usr/bin/python3
"""
This module contains a program that solves the N-Queens puzzle challenge.
"""
import sys


def nqueens(n):
    """Initiate the Nqueens puzzle solution process."""
    board = [[0 for col in range(n)] for row in range(n)]
    solve(board, 0, n)


def solve(board, col, n):
    """Solve the Nqueens puzzle using backtracking."""
    if col == n:
        print_board(board)
        return

    for row in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve(board, col + 1, n)
            board[row][col] = 0  # Backtrack


def is_safe(board, row, col, n):
    """Check if it's safe to place a queen at the given row and column."""
    # Check the same row to the left
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check the upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check the lower diagonal on the left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def print_board(board):
    """Print the board in a list of coordinates format."""
    queens = []
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 1:
                queens.append([row, col])
    print(queens)


def handle_input(args) -> int:
    """Handle command-line input validation."""
    if len(args) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        n = int(args[1])
    except ValueError:
        print("N must be a number")
        exit(1)

    if n < 4:
        print("N must be at least 4")
        exit(1)

    return n


if __name__ == "__main__":
    n = handle_input(sys.argv)
    nqueens(n)
