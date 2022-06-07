import numpy as np
import Funciones_vuelos as fv
sw = True
asientosN = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30])
asientosVIP = np.array([31,32,33,34,35,36,37,38,39,40,41,42])

fv.printMenu()

while sw == True:
    try:
        op = int(input())
        if op > 0 and op < 6:
            if op == 5:
                sw = False
        else:
            print("Opción no valida")
    except:
        print("Dato ingresado no es valido")