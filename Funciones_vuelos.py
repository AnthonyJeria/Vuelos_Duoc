from numpy import True_
import Vuelos_Duoc as vd

def printMenu():
  print("-"*40)
  print("Vuelos Duoc")
  print("-"*40)
  print("1.   Ver asientos disponibles")
  print("2.   Comprar asiento")
  print("3.   Anular vuelo")
  print("4.   Modificar datos de pasajero")
  print("5.   Salir")
  print("-"*40)
  print("Ingrese el numero de la función que desea utilizar")

def comAsineto(numAsi, tAsi, nom, rut, tef, ban,):
  
  if tAsi == 1:
    for f in range(5):
      for c in range(6):
        if vd.asientosN[f][c] == numAsi:
          vd.asientosN[f,c] = 0

  if tAsi == 2:
    for f in range(2):
      for c in range(6):
        if vd.asientosN[f][c] == numAsi:
          vd.asientosN[f,c] = 0

  if ban == "si":
    banc = "Banco Duoc"
  else:
    banc = "No banco Duoc"

  if numAsi == 1:
    lista1 = [numAsi, rut, nom, tef, banc]

  if numAsi == 2:
    lista2 = [numAsi, rut, nom, tef, banc]

  if numAsi == 3:
    lista3 = [numAsi, rut, nom, tef, banc]

  if numAsi == 4:
    lista4 = [numAsi, rut, nom, tef, banc]

  if numAsi == 5:
    lista5 = [numAsi, rut, nom, tef, banc]
  
  if numAsi == 6:
    lista6 = [numAsi, rut, nom, tef, banc]

  if numAsi == 7:
    lista7 = [numAsi, rut, nom, tef, banc]

  if numAsi == 8:
    lista8 = [numAsi, rut, nom, tef, banc]

  if numAsi == 9:
    lista9 = [numAsi, rut, nom, tef, banc]

  if numAsi == 10:
    lista10 = [numAsi, rut, nom, tef, banc]

  if numAsi == 11:
    lista11 = [numAsi, rut, nom, tef, banc]
  
  if numAsi == 12:
    lista12 = [numAsi, rut, nom, tef, banc]

  if numAsi == 13:
    lista13 = [numAsi, rut, nom, tef, banc]

  if numAsi == 14:
    lista14 = [numAsi, rut, nom, tef, banc]

  if numAsi == 15:
    lista15 = [numAsi, rut, nom, tef, banc]

  if numAsi == 16:
    lista16 = [numAsi, rut, nom, tef, banc]

  if numAsi == 17:
    lista17 = [numAsi, rut, nom, tef, banc]
  
  if numAsi == 18:
    lista18 = [numAsi, rut, nom, tef, banc]

  if numAsi == 19:
    lista19 = [numAsi, rut, nom, tef, banc]

  if numAsi == 20:
    lista20 = [numAsi, rut, nom, tef, banc]

  if numAsi == 21:
    lista21 = [numAsi, rut, nom, tef, banc]

  if numAsi == 22:
    lista22 = [numAsi, rut, nom, tef, banc]

  if numAsi == 23:
    lista23 = [numAsi, rut, nom, tef, banc]
  
  if numAsi == 24:
    lista24 = [numAsi, rut, nom, tef, banc]

  if numAsi == 25:
    lista25 = [numAsi, rut, nom, tef, banc]

  if numAsi == 26:
    lista26 = [numAsi, rut, nom, tef, banc]

  if numAsi == 27:
    lista27 = [numAsi, rut, nom, tef, banc]

  if numAsi == 28:
    lista28 = [numAsi, rut, nom, tef, banc]

  if numAsi == 29:
    lista29 = [numAsi, rut, nom, tef, banc]
  
  if numAsi == 30:
    lista30 = [numAsi, rut, nom, tef, banc]

  if numAsi == 31:
    lista31 = [numAsi, rut, nom, tef, banc]

  if numAsi == 32:
    lista32 = [numAsi, rut, nom, tef, banc]

  if numAsi == 33:
    lista33 = [numAsi, rut, nom, tef, banc]

  if numAsi == 34:
    lista34 = [numAsi, rut, nom, tef, banc]

  if numAsi == 35:
    lista35 = [numAsi, rut, nom, tef, banc]
  
  if numAsi == 36:
    lista36 = [numAsi, rut, nom, tef, banc]

  if numAsi == 37:
    lista37 = [numAsi, rut, nom, tef, banc]

  if numAsi == 37:
    lista37 = [numAsi, rut, nom, tef, banc]

  if numAsi == 38:
    lista38 = [numAsi, rut, nom, tef, banc]

  if numAsi == 39:
    lista39 = [numAsi, rut, nom, tef, banc]

  if numAsi == 40:
    lista40 = [numAsi, rut, nom, tef, banc]
  
  if numAsi == 41:
    lista41 = [numAsi, rut, nom, tef, banc]

  if numAsi == 42:
    lista42 = [numAsi, rut, nom, tef, banc]

def printAsientos():
  print(vd.asientosN)
  print("-"*27)
  print("-"*27)
  print(vd.asientosVIP)
  con = input("Ingrese cualquier caracter para volver: ")

def anularAsi(numAsi):

  if numAsi >= 1 and numAsi <= 30:
    if numAsi >= 1 and numAsi <= 6:
      fi = 0
      co = numAsi -1

    elif numAsi >= 7 and numAsi <= 12:
      fi = 1
      co = numAsi - 7

    elif numAsi >= 13 and numAsi <= 18:
      fi = 2
      co = numAsi -13

    elif numAsi >= 19 and numAsi <= 24:
      fi = 3
      co = numAsi - 19

    elif numAsi >= 25 and numAsi <= 30:
      fi = 4
      co = numAsi -25

    vd.asientosN[fi,co] = numAsi

  if numAsi >= 31 and numAsi <= 42:
    if numAsi >= 31 and numAsi <= 36:
      fi = 0
      co = numAsi - 31
    else:
      fi = 2
      co = numAsi - 37

  vd.asientosVIP[fi,co] = numAsi

  if numAsi == 1:
    lista1 = []

  if numAsi == 2:
    lista2 = []

  if numAsi == 3:
    lista3 = []

  if numAsi == 4:
    lista4 = []

  if numAsi == 5:
    lista5 = []
  
  if numAsi == 6:
    lista6 = []

  if numAsi == 7:
    lista7 = []

  if numAsi == 8:
    lista8 = []

  if numAsi == 9:
    lista9 = []

  if numAsi == 10:
    lista10 = []

  if numAsi == 11:
    lista11 = []
  
  if numAsi == 12:
    lista12 = []

  if numAsi == 13:
    lista13 = []

  if numAsi == 14:
    lista14 = []

  if numAsi == 15:
    lista15 = []

  if numAsi == 16:
    lista16 = []

  if numAsi == 17:
    lista17 = []
  
  if numAsi == 18:
    lista18 = []

  if numAsi == 19:
    lista19 = []

  if numAsi == 20:
    lista20 = []

  if numAsi == 21:
    lista21 = []

  if numAsi == 22:
    lista22 = []

  if numAsi == 23:
    lista23 = []
  
  if numAsi == 24:
    lista24 = []

  if numAsi == 25:
    lista25 = []

  if numAsi == 26:
    lista26 = []

  if numAsi == 27:
    lista27 = []

  if numAsi == 28:
    lista28 = []

  if numAsi == 29:
    lista29 = []
  
  if numAsi == 30:
    lista30 = []

  if numAsi == 31:
    lista31 = []

  if numAsi == 32:
    lista32 = []

  if numAsi == 33:
    lista33 = []

  if numAsi == 34:
    lista34 = []

  if numAsi == 35:
    lista35 = []
  
  if numAsi == 36:
    lista36 = []

  if numAsi == 37:
    lista37 = []

  if numAsi == 37:
    lista37 = []

  if numAsi == 38:
    lista38 = []

  if numAsi == 39:
    lista39 = []

  if numAsi == 40:
    lista40 = []
  
  if numAsi == 41:
    lista41 = []

  if numAsi == 42:
    lista42 = []