README for nking.py problem:
=============================
nking.py README
================

Solving the problem as found in: http://stackoverflow.com/questions/11382189/number-of-ways-to-place-kings-on-chess-board

Description of the problem:
============================
You have an N x N chessboard and you wish to place N kings on it. Each row and column should contain exactly one king, and no two kings should attack each other (two kings attack each other if they are present in squares which share a corner).

The kings in the first K rows of the board have already been placed. You are given the positions of these kings as an array pos[ ]. pos[i] is the column in which the king in the ith row has already been placed. All indices are 0-indexed. In how many ways can the remaining kings be placed?


Output:
Output the number of ways to place kings in the remaining rows satisfying the above conditions. Output all numbers modulo 1000000007.

Constraints:
1 <= T <= 20
1 <= N <= 16
0 <= K <= N
0 <= pos_i < N
The kings specified in the input will be in different columns and not attack each other.

Sample Input:
5
4 1
2
3 0

5 2
1 3
4 4
1 3 0 2
6 1
2

Sample Output:
1
0
2
1
18

Explanation: For the first example, there is a king already placed at row 0 and column 2. The king in the second row must belong to column 0. The king in the third row must belong to column 3, and the last king must beong to column 1. Thus there is only 1 valid placement.

For the second example, there is no valid placement.
