Every program needs to change the path of file in main function


Implementation: Sudoku
For the following implementation, include your Python code in your hw2.zip file. Also include a short README file explaining how to run your code.
1. Write a program that reads in an initial setup representing a Sudoku board.  Some squares may already be filled in with a number.  Squares that are blank are represented with a “?”.  All values are comma separated.  For example
            ?,?,3,1
            2,?,?,?
            1,3,?,?
            ?,?,?,?
Represents a small Sudoku board with the bottom row with no numbers. The board sizes will be 4x4, 9x9, and 16x16. These sizes all have square blocks.
 
2.  Write a method that evaluates a given board setup and determines if it is a valid solution state.  If it is not a valid solution, the program should return the number of conflicts.
For the problems below, you can use this website to generate and solve 9x9 sudoku puzzles for testing your code: http://www.sudoku-solutions.com/. We will test your code using several sudoku puzzles with sizes 4x4, 9x9, and 16x16.
3. Write a program that uses simulated annealing to solve a Sudoku problem. Initialize the method with a random assignment. You will need to pick a temperature schedule or create your own. If you get stuck in a local minimum that doesn’t satisfy all the constraints, restart the algorithm with a different random assignment. You can also experiment with non-random or partially-random initial assignments. Time-limit your program to five minutes.  Determine how large of a puzzle you can solve in this time limit.  
 
4. Write a program that uses A* search to solve a Sudoku problem.  For this exercise, you will need a good heuristic function.  Your program should not run for more than five minutes (this “requirement” is to make your lives easier).  Determine how large of a puzzle you can solve in this time limitation.  
 
5. Implement constraint satisfaction to solve Sudoku.  You should make use of the following heuristics in your solution:
1) Minimum remaining values
2) Degree Heuristic
3) Least-constraining-value heuristic
Determine how large of a board you are capable of solving in under 5 minutes.
Write up 
1. Explain how you solved the problem using simulated annealing. Which temperature schedule did you use and why? How did you pick the initial assignment?
2. Explain how you solved the problem with A*, including which heuristic function you used.  
3. Compare the performance of Simulated Annealing, A*, and CSP in terms of number of seconds to solve a board (average across 5 puzzles).
4. Analyze A* and CSP’s performance to determine why CSP is a better solution.  What is the source of CSP’s power here?  Determine how much of the savings comes from each of the components within CSP. 
