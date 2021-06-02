import numpy as np
import pandas as pd


def is_stochastic(matrix):
    x = matrix.shape
    boolean = True
    if(x[0]==x[1]):
        for i in range(x[0]):
            count = 0
            for j in range(x[0]):
                count+=matrix[j][i]
                if(j==x[0]-1):
                    if not np.isclose(count, 1):
                        boolean = False
                if(matrix[j][i]<0):
                    boolean = False
        if(boolean):
            return True
    return False
    

def adjacency(dic):
    A = np.zeros((len(dic),len(dic)))
    for x,y in dic.items():
        for i in range(len(y)):
            A[x,y[i]] = 1;
    return A

def count_shortest_paths(M, i, j):
    shape = M.shape[0]
    D = np.eye(shape, dtype=np.int64)
    while D[i][j]==0:
        D=D@M
    return D[i][j]

def leontief(file, name):
    data = pd.read_csv(file)
    shape = data.to_numpy().shape[0]
    ind = data.columns.get_loc(name)-1
    A = []
    b = []
    I = np.eye(shape-1, dtype=np.float64)
    # x = Ax + b
    # (I-A)x = b
    for i in range(shape):
        if i==shape-1:
            b = np.delete(data.to_numpy()[i], 0)
        else:
            A.append(np.delete(data.to_numpy()[i],0))
    b = np.array(b, dtype=np.float64)    
    A = np.array(A, dtype=np.float64)
    x = np.linalg.solve(I-A, b)

    return x[ind]
    

def main():
    #M = np.zeros([4,4])
    #M[0,0] = 0.99
    #M[1,0] = 0.01
    #M[1,1] = 0.79
    #M[2,1] = 0.2
    #M[3,1] = 0.01
    #M[2,2] = 1
    #M[3,3] = 1
    #print(is_stochastic(M))
    d = {0: [1], 1: [0,2], 2: [3], 3: []}
    stoch = (adjacency(d))
    print(count_shortest_paths(stoch, 0,3))
    #print(leontief("leontief.csv", "butter"))
    
main()