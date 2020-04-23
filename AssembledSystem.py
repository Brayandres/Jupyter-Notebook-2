import numpy as np
import matplotlib.pyplot as plt
from Converter import *

def sistemas_Ensamblados(ma, mb, va, vb, clicks):
    MA = to_Matrix(ma)
    MB = to_Matrix(mb)
    VA = to_Vector(va)
    VB = to_Vector(vb)
    
    MAB = MA.tensorProduct(MB)
    VAB = (Matrx([VA]).tensorProduct( Matrx([VB]) )).rows[0]
    
    for i in range(clicks):
        VAB = MAB.actOnVect(VAB)
    
    labels = []
    states = []
    count = 0
    for i in range(len(va)):
        for j in range(len(vb)):
            labels.append(str(i)+str(j))
            states.append(VAB.numbers[count].element_1)
            count += 1
    index = np.arange(len(labels))
    plt.bar(index, states)
    plt.xlabel("Estado")
    plt.ylabel("Valor")
    plt.xticks(index, labels, rotation = 75)
    plt.title("Evolución Dinámica del sistema luego de "+str(clicks)+" click(s) de tiempo:")
    plt.show()

############################################################################################

MA = [[[0,0],[0.2,0],[0.3,0],[0.5,0]],
      [[0.3,0],[0.2,0],[0.1,0],[0.4,0]],
      [[0.4,0],[0.3,0],[0.2,0],[0.1,0]],
      [[0.3,0],[0.3,0],[0.4,0],[0,0]]
     ]

MB = [[[0,0],[1/6,0],[5/6,0]], 
      [[1/3,0],[1/2,0],[1/6,0]], 
      [[2/3,0],[1/3,0],[0,0]] 
     ]

VA = [[[0.2,0]],[[0.1,0]],[[0.6,0]],[[0.1,0]]]

VB = [[[0.7,0]],[[0.15,0]],[[0.15,0]]]

C = 5

sistemas_Ensamblados(MA, MB, VA, VB, C)