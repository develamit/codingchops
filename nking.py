'''
Created on Jan 14, 2014

@author: amitava bhaduri
Solving the problem found in:
http://stackoverflow.com/questions/11382189/number-of-ways-to-place-kings-on-chess-board
The input to this problem is through a text file, which has the chess board configuration details.
The input file description and constraints are given in the above link and in the README file.
'''

import numpy
validCnt = 0

def detectAttack(r, c, rp, chessBoard, N):
    if rp < 0: # going before row 0
        return 0 # 0 means no attack
    if ((c+1) < N) and (chessBoard[rp][c+1] == 1):
        return 1 # 1 means attack
    elif ((c-1) >= 0) and (chessBoard[rp][c-1] == 1):
        return 1 # 1 means attack
    else:
        return 0
    
def detectColumnCollision(c, columnTrack):
    if columnTrack[c] == 1:
        return 1
    else:
        return 0
    
    
def callSoln(item=None):
    #print 'callSoln:'
    global validCnt
    validCnt = 0
    
    N = int(item[0][0])
    K = int(item[0][1])
    if (N == K):
        #print('All rows are filled up... So done...')
        validCnt += 1
        #print 'validCnt final=', validCnt
        print(validCnt),
        print('\n'),
        return
    
    posarr=[]
    if item[1]:
        posarr = map(int, item[1])
        
    chessBoard = numpy.zeros(shape=(N,N)) # square matrix
    columnTrack = numpy.zeros(N) # array with N zeros
    for i in xrange(K):
        chessBoard[i][posarr[i]] = 1 # filling up the chessboard with the Kings given
        columnTrack[posarr[i]] = 1
    
    # Recursive Call - may not be the best. can lead to stack overflow. For now lets keep it this way  
    explore(N, K, chessBoard, columnTrack)
    #print '\n'
    #print 'ValidCnt final= ', validCnt
    print(validCnt),
    print('\n'),
    
def explore(N, K, chessBoard, columnTrack):
    rows_to_explore = N-K+1
    '''
    # can uncomment for debug
    print('\n'),
    print(chessBoard),
    print('\n'),
    print('columnTrack=', columnTrack),
    print('\n'),
    print('rows_to_explore=', rows_to_explore),
    print('\n')
    '''
    r = K
    for c in xrange(0, N):
        #detect kings attack with previous row, which has already been placed
        #print 'row=', r, 'col=', c
        retd = detectAttack(r, c, r-1, chessBoard, N)
        retc = detectColumnCollision(c, columnTrack)
        if retd == 0 and retc == 0: # good to go
            #print(r,c, ':valid rowcol', retd, retc),
            if r == N-1:
                global validCnt
                validCnt += 1 # reached the last row and found a valid cell. So increase count
                #print('ValidCnt here=', validCnt)
                #return
            else:
                chessBoard[r][c] = 1
                columnTrack[c] = 1
                
                explore(N, r+1, chessBoard, columnTrack)
                #print 'stack return: row=', r, 'col=', c
                
                chessBoard[r][c] = 0 #re-initializing
                columnTrack[c] = 0   #re-initializing
                '''
                # uncomment for debug purpose
                print('\n'),
                print('Reinstated chessboard:'),
                print('\n')
                print(chessBoard),
                print('\n')
                print('Reinstated columnTrack'),
                print('\n')
                print(columnTrack)
                '''
        #else:
            #print(r,c, ':Invalid rowcol', retd, retc),


if __name__ == '__main__':
    allTestList = []
    T = int(raw_input())
    for t in xrange(T):
        NKarr = []
        posarr = [] 
        for line_num in xrange(0,2):
            #print 'here...'
            inp = raw_input()
            if line_num == 0:
                NKarr = inp.split(' ', len(inp))
            else:
                if NKarr and int(NKarr[1]) == 0:
                    posarr = []
                    #print 'here...'
                else:
                    posarr = inp.split(' ', len(inp))
                #print('posarr length:', len(inp), 'posarr=', posarr)
        entryTuple = (NKarr, posarr)
        allTestList.append(entryTuple)
    
    for item in allTestList:
        #print('item[0]=', item[0]),
        #print('item[1]=', item[1]),
        callSoln(item)

    #for i in xrange(N):
        #print 'hello'
