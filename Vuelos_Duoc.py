import numpy as np
import Funciones_vuelos as fv
sw = True
asientosN = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30])
asientosVIP = np.array([31,32,33,34,35,36,37,38,39,40,41,42])

while sw == True:
    fv.printMenu()
    try:
        op = int(input())
        if op > 0 and op < 6:
            if op == 5:
                sw = False
            #Compra de asientos
            if op == 2:
                bc = True
                ato = True
                nombre = input("Ingrese su nombre: ")
                rut = input("Ingrese su rut: ")
                telefono = input("ingrese su telefono: ")
                while bc == True:
                    banco = input("¿Es cliente de bancoDuoc?(ingrese si o no)")
                    if banco == "si" or banco == "no":
                        bc = False
                    else:
                        print("Opcion no valida")

                print("¿Que tipo de asiento desea\n1. Normal\n2.  VIP")
                while ato == True:
                    try:
                        asiento = int(input())
                        if asiento == 1 or asiento == 2:
                            ato = False
                            if asiento == 1:
                                print(asientosN)
                                numasiento = input("Ingrese el numero del asiento que desea")
                            if asiento == 2:
                                print(asientosVIP)
                                numasiento = input("Ingrese el numero del asiento que desea")
                        else:
                            print("Opcion no valida")
                    except:
                        print("Opcion no valida")
        else:
            print("Opción no valida")
    except:
        print("Dato ingresado no es valido")