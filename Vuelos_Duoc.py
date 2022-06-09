import numpy as np
import Funciones_vuelos as fv
sw = True
costoN = 78900
costoVip = 240000

asientosN = np.zeros([5,6])
n = 0
for f in range(5):
  for c in range(6):
    n = n + 1
    asientosN[f][c] = n

asientosVIP = np.zeros([2,6])
n = 30
for f in range(2):
  for c in range(6):
    n = n + 1
    asientosVIP[f][c] = n

while sw == True:
    fv.printMenu()
    try:
        op = int(input())
        if op > 0 and op < 6:
            if op == 5:
                sw = False

            if op == 1:
                fv.printAsientos()

            if op == 4:
                asiMod = input("Ingrese el numero de asiento que desea modificar: ")
                rutMod = input("Ingrese el numero de rut del pasajero que desea modificar")

                fv.modDatos(asiMod, rutMod)

            if op == 3:
                tt = True
                while tt == True:
                    try:
                        numAnu = input("Ingrese el numero de asiento que desea anular: ")
                        if numAnu >= 1 and numAnu <= 42:
                            tt = False
                            fv.anularAsi(numAnu)
                        else:
                            print("Asiento no existente")
                    except:
                        print("Valor no valido")

            #Compra de asientos
            if op == 2:
                bc = True
                ato = True
                nombre = input("Ingrese su nombre: ")
                rut = input("Ingrese su rut: ")
                telefono = input("ingrese su telefono: ")
                while bc == True:
                    banco = input("¿Es cliente de bancoDuoc?(ingrese si o no): ")
                    if banco == "si" or banco == "no":
                        bc = False
                    else:
                        print("Opcion no valida")

                print("¿Que tipo de asiento desea\n1.   Normal\n2.  VIP")
                while ato == True:
                    try:
                        asiento = int(input())
                        if asiento == 1 or asiento == 2:
                            ato = False

                            if asiento == 1:
                                na = True
                                
                                if banco == "si":
                                    print("El costo sera de: $"+ str(costoN - (costoN * 0.15)))
                                else:
                                    print("El costo sera de: $"+ str(costoN))

                                print(asientosN)
                                numasiento = int(input("Ingrese el numero del asiento que desea: "))
                                while na == True:
                                    try:
                                        if numasiento >= 1 and numasiento <= 30:
                                            na = False
                                            fv.comAsineto(numasiento,asiento,nombre,rut,telefono,banco)
                                        else:
                                            print("Asiento no valido")
                                    except:
                                        print("Asiento no valido")
                            else:
                                na = True

                                if banco == "si":
                                    print("El costo sera de: $"+ str(costoVip - (costoVip * 0.15)))
                                else:
                                    print("El costo sera de: $"+ str(costoVip))

                                print(asientosVIP)
                                numasiento = int(input("Ingrese el numero del asiento que desea"))
                                while na == True:
                                    try:
                                        if numasiento >= 31 and numasiento <= 42:
                                            na = False
                                            fv.comAsineto(numasiento,asiento,nombre,rut,telefono,banco)
                                        else:
                                            print("Asiento no valido")
                                    except:
                                        print("Asiento no valido")
                        else:
                            print("Opcion no valida")
                    except:
                        print("Opcion no valida")
        else:
            print("Opción no valida")
    except:
        print("Dato ingresado no es valido")