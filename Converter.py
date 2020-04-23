from Matrx import *

def to_Vector(v):
    vector = []
    for i in range(len(v)):
        vector.append( Cartesian( tuple(v[i][0])) )
    return Vector(vector)

def to_Matrix(m):
    M = []
    for i in range(len(m)):
        temp = []
        for j in range(len(m)):
            temp.append( Cartesian(tuple(m[i][j])) )
        M.append( Vector(temp) )
    return Matrx(M)