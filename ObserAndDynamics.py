import numpy as np
import matplotlib.pyplot as plt
from Converter import *

def ObsCalculator(ob, k):
    observable = to_Matrix(ob)
    ket = to_Vector(k)
    ket = ket.scal_prod( Cartesian((1/ket.norm(), 0)) )
    
    expectedVal = ket.conjugate().dot_prod(observable.actOnVect(ket))
    
    #VARIANCE
    stepA = observable - (observable.identity()).scalarProd(expectedVal)
    stepB = stepA.dagger()*stepA
    variance = ket.conjugate().dot_prod(stepB.actOnVect(ket))

    print("Valor Esperado:", round(expectedVal.real, 4))
    print("Varianza:", variance.real)
    
    labels = ["Val. Esp.", "Varianza"]
    values = [expectedVal.real, variance.real]
    index = np.arange(len(labels))
    plt.bar(index, values)
    plt.xlabel("Indicador")
    plt.ylabel("Valor")
    plt.xticks(index, labels, rotation = 75)
    plt.title("Valores Obtenidos:")
    plt.show()

#########################################################################
    
ob = [[[0,0],[0,-1/2],[0,-1],[-7/2,0]],
      [[0,1/2],[0,0],[7/2,0],[0,-1]],
      [[0,1],[7/2,0],[0,0],[0,-1/2]],
      [[-7/2,0],[0,1],[0,1/2],[0,0]]
     ]

k = [[[-2, 1]],
     [[1, 0]],
     [[0,-1]],
     [[3,2]]
    ]

ObsCalculator(ob, k)
