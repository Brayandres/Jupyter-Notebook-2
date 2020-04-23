import numpy as np
import matplotlib.pyplot as plt
from Converter import *

def particlesInALine(n, v):
    V = to_Vector(v)
    V = V.scal_prod( Cartesian((1/V.norm(), 0)) )
    states = []
    for i in range(V.long):
        states.append((V.numbers[i].mod())**2)
    
    labels = []
    for k in range(len(states)):
        labels.append("X"+str(k))
    index = np.arange(len(labels))
    plt.bar(index, states)
    plt.xlabel("Estado")
    plt.ylabel("Valor")
    plt.xticks(index, labels, rotation = 75)
    plt.title("Distribución De Probabilidad Para Los Estados Básicos:")
    plt.show()

#######################################################################

v = [[[2, -1]],
     [[-1.5, 2.5]],
     [[-3.5, 5]],
     [[-4, 6]],
     [[-3.5, 2.5]],
     [[0, 0]],
     [[-3.5, 2.5]],
     [[6, -4]],
     [[0, 2.5]],
     [[-1, 1]]
    ]

particlesInALine(10, v)