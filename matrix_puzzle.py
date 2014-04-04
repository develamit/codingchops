'''
Author: Amitava Bhaduri
Date: 03/25/2014
'''

import numpy as np

class matrixPuzzle:
    def __init__(self, arr):
        self.arr = arr
        self.matrix = np.zeros(shape=(3,3))
        self.setTotal = set(x for x in arr)
        self.setA = set()
        self.setB = set()
        self.Combs = ()
        self.Perms = ()
        self.solSet = []
        
    def productValidate(self):
        prodArr = [1] * 4 # preserve the products for R0, R2, C0, C2
        setProd = set()
        for i in xrange(3):
            prodArr[0] *= self.matrix[0][i] #R0
            prodArr[1] *= self.matrix[2][i] #R2
            prodArr[2] *= self.matrix[i][0] #C0
            prodArr[3] *= self.matrix[i][2] #C2

        setProd = set(x for x in prodArr)
        if len(setProd) == 1:
            #print 'setProd=', setProd
            return 1
        else:
            return 0
        
    def sumValidate(self):
        sumArr = [0] * 4
        for i in xrange(3):
            sumArr[0] += self.matrix[0][i] #R0 (North)
            sumArr[1] += self.matrix[2][i] #R2 (South)
            sumArr[2] += self.matrix[i][0] #C0 (West)
            sumArr[3] += self.matrix[i][2] #C2 (East)
        #Condition to satisfy: W - S = 1 # S - E = 2 # E - N = 3
        if (sumArr[2] - sumArr[1] == 1) and (sumArr[1] - sumArr[3] == 2) and (sumArr[3] - sumArr[0] == 3):
            return 1
        else:
            return 0
    
    def findPerms(self, arr):
        import itertools as it
        #print('permutations')
        P = it.permutations(arr, 4)
        permPool = tuple(P)
        return permPool
        
        
    def solver(self):
        self.Perms = self.findPerms(self.arr)
        print 'len of perms:', len(self.Perms)
        for tup in self.Perms:
            #arrange the corner elements from each tuple in the Permutation
            self.matrix[0][0] = tup[0]
            self.matrix[0][2] = tup[1]
            self.matrix[2][0] = tup[2]
            self.matrix[2][2] = tup[3]
            
            # run permutations of the other remaining array elements and fill up the matrix remaining positions
            self.setA = set(x for x in tup)
            self.setB = self.setTotal - self.setA
            permPool = self.findPerms(self.setB)
            for tupP in permPool:
                self.matrix[0][1] = tupP[0]
                self.matrix[2][1] = tupP[1]
                self.matrix[1][0] = tupP[2]
                self.matrix[1][2] = tupP[3]
                #Now validate each matrix
                retProd = self.productValidate()
                if retProd == 1:
                    retSum = self.sumValidate()
                    if retSum == 1:
                        print 'product valid and sum valid:'
                        print self.matrix
                        # Capture the result which satisfies both conditions
                        self.solSet.append(self.matrix)

if __name__ == '__main__':
    arr = [1,2,3,4,5,6,10,12]
    mP = matrixPuzzle(arr)
    mP.solver()
    
