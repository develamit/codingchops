'''
Author: Amitava Bhaduri
Date: 03/25/2014
Comments: I just took a generic nxm matrix. It should work for square matrices as well... 
          You can pass the matrix as an argument to printMatrix()
'''

import numpy as npy

def printMatrix():
    m = npy.matrix('9 7 6; 5 4 3; 6 7 2; 3 4 8; 6 7 2; 3 4 8')
    (num_rows, num_cols) = m.shape
    #print m
    for c in xrange(num_cols):
        row_index = 0
        for c1 in reversed(xrange(0, c+1)):
            if row_index >= num_rows:
                continue
            print(m[row_index, c1]),
            row_index += 1
        print("\n"),
        
    for r in xrange(1, num_rows):
        col_index = num_cols - 1
        for r1 in xrange(r, num_rows):
            if col_index < 0:
                continue
            print(m[r1, col_index]),
            col_index -= 1
        print("\n"),
            
def main():
    # print matrix in a weird way :)
    printMatrix()

if __name__ == '__main__':
    main()
