# 0x05. N Queens
`Algorithm` `Python`

The “0x05. N queens” project is a classic problem in computer science and mathematics, known for its application of the backtracking algorithm to place N non-attacking queens on an N×N chessboard. To successfully complete this project, you will need to understand several key concepts and have access to resources that will help you grasp the necessary algorithms and techniques.

## Concepts Needed:
1. **Backtracking Algorithms:**
    * Understanding how backtracking algorithms work to explore all potential solutions to a problem and backtrack when a solution cannot be completed.
    * [Backtracking Introduction](https://www.geeksforgeeks.org/introduction-to-backtracking-2/)

2. **Recursion:**
    * Using recursive functions to implement backtracking algorithms.
    * [Recursion in Python](https://realpython.com/python-thinking-recursively/)

3. **List Manipulations in Python:**
    * Creating and manipulating lists, especially to store the positions of queens on the board.
    * [Python Lists](https://docs.python.org/3/tutorial/datastructures.html)

4. **Python Command Line Arguments:**
    * Handling command-line arguments with the `sys` module.
    * [Command Line Arguments in Python](https://docs.python.org/3.3/library/sys.html#sys.argv)

### Additional Resources
* [Queen](https://en.wikipedia.org/wiki/Queen_%28chess%29)
* [Backtracking](https://en.wikipedia.org/wiki/Backtracking)

By studying these concepts and utilizing the resources provided, you will be equipped with the knowledge required to implement an efficient solution to the N queens problem using Python. This project not only tests programming and problem-solving skills but also offers an excellent opportunity to learn about algorithmic thinking and optimization techniques.

## Explanation of the N-Queens Problem
The N-Queens problem is a challenge in which we try to place NN queens on an N×NN×N chessboard such that:
    1. No two queens can attack each other.
    2. A queen can attack another queen if they are in the same row, same column, or on the same diagonal.

Our goal is to find all the possible ways to place NN queens on this board while following these rules. If we manage to place all queens without breaking the rules, we’ve found a solution.

## Approach to Solving the Problem
The strategy we use to solve this is backtracking:
    1. Start by placing the first queen in the first row.
    2. Move to the next row and try to place the next queen in a column where it won’t be attacked.
    3. If we reach a point where there’s no valid place for a queen, we backtrack to the previous row, move the queen there to the next possible column, and try again.
    4. We continue this process until we’ve placed all queens on the board or explored all possibilities.
