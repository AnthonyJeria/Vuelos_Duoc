from numpy import True_
import Vuelos_Duoc as vd

lista1 = []
lista2 = []
lista3 = []
lista4 = []
lista5 = []
lista6 = []
lista7 = []
lista8 = []
lista9 = []
lista10 = []
lista11 = []
lista12 = []
lista13 = []
lista14 = []
lista15 = []
lista16 = []
lista17 = []
lista18 = []
lista19 = []
lista20 = []
lista21 = []
lista22 = []
lista23 = []
lista24 = []
lista25 = []
lista26 = []
lista27 = []
lista28 = []
lista29 = []
lista30 = []
lista31 = []
lista32 = []
lista33 = []
lista34 = []
lista35 = []
lista36 = []
lista37 = []
lista38 = []
lista39 = []
lista40 = []
lista41 = []
lista42 = []

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

def modDatos(asiMod, rutMod):

  try:

    if asiMod == 1:
      print("-"*40)
      print(lista1)
      print("-"*40)
      
      nom = input("Ingrese nuevo nombre: ")
      tef = input("Ingrese nuevo numero telefonico: ")
      ol = True
      while ol == True:
        bank = input("Es banco duoc o es un ser inferior(si o no)")
        if bank == "si" or bank == "no":
          ol = False
        else:
          print("Respuesta no valida")
      
      if bank == "si":
        banc = "Banco Duoc"
      else:
        banc = "No banco Duoc"

      lista1 = [asiMod, rutMod, nom, tef,banc ]

    if asiMod == 2:
      print("-"*40)
      print(lista2)
      print("-"*40)
      
      nom = input("Ingrese nuevo nombre: ")
      tef = input("Ingrese nuevo numero telefonico: ")
      ol = True
      while ol == True:
        bank = input("Es banco duoc o es un ser inferior(si o no)")
        if bank == "si" or bank == "no":
          ol = False
        else:
          print("Respuesta no valida")
      
      if bank == "si":
        banc = "Banco Duoc"
      else:
        banc = "No banco Duoc"

      lista2 = [asiMod, rutMod, nom, tef,banc ]


    if asiMod == 3:
      print("-"*40)
      print(lista3)
      print("-"*40)
      
      nom = input("Ingrese nuevo nombre: ")
      tef = input("Ingrese nuevo numero telefonico: ")
      ol = True
      while ol == True:
        bank = input("Es banco duoc o es un ser inferior(si o no)")
        if bank == "si" or bank == "no":
          ol = False
        else:
          print("Respuesta no valida")
      
      if bank == "si":
        banc = "Banco Duoc"
      else:
        banc = "No banco Duoc"

      lista3 = [asiMod, rutMod, nom, tef,banc ]
      
    if asiMod == 4:
      print("-"*40)
      print(lista4)
      print("-"*40)
      
      nom = input("Ingrese nuevo nombre: ")
      tef = input("Ingrese nuevo numero telefonico: ")
      ol = True
      while ol == True:
        bank = input("Es banco duoc o es un ser inferior(si o no)")
        if bank == "si" or bank == "no":
          ol = False
        else:
          print("Respuesta no valida")
      
      if bank == "si":
        banc = "Banco Duoc"
      else:
        banc = "No banco Duoc"

      lista4 = [asiMod, rutMod, nom, tef,banc ]

    if asiMod == 5:
      print("-"*40)
      print(lista5)
      print("-"*40)
      
      nom = input("Ingrese nuevo nombre: ")
      tef = input("Ingrese nuevo numero telefonico: ")
      ol = True
      while ol == True:
        bank = input("Es banco duoc o es un ser inferior(si o no)")
        if bank == "si" or bank == "no":
          ol = False
        else:
          print("Respuesta no valida")
      
      if bank == "si":
        banc = "Banco Duoc"
      else:
        banc = "No banco Duoc"

      lista5 = [asiMod, rutMod, nom, tef,banc ]

    if asiMod == 6:
      print("-"*40)
      print(lista6)
      print("-"*40)
      
      nom = input("Ingrese nuevo nombre: ")
      tef = input("Ingrese nuevo numero telefonico: ")
      ol = True
      while ol == True:
        bank = input("Es banco duoc o es un ser inferior(si o no)")
        if bank == "si" or bank == "no":
          ol = False
        else:
          print("Respuesta no valida")
      
      if bank == "si":
        banc = "Banco Duoc"
      else:
        banc = "No banco Duoc"

      lista6 = [asiMod, rutMod, nom, tef,banc ]

    if asiMod == 7:
      print("-"*40)
      print(lista7)
      print("-"*40)
      
      nom = input("Ingrese nuevo nombre: ")
      tef = input("Ingrese nuevo numero telefonico: ")
      ol = True
      while ol == True:
        bank = input("Es banco duoc o es un ser inferior(si o no)")
        if bank == "si" or bank == "no":
          ol = False
        else:
          print("Respuesta no valida")
      
      if bank == "si":
        banc = "Banco Duoc"
      else:
        banc = "No banco Duoc"

      lista7 = [asiMod, rutMod, nom, tef,banc ]

    if asiMod == 8:
      print("-"*40)
      print(lista8)
      print("-"*40)
      
      nom = input("Ingrese nuevo nombre: ")
      tef = input("Ingrese nuevo numero telefonico: ")
      ol = True
      while ol == True:
        bank = input("Es banco duoc o es un ser inferior(si o no)")
        if bank == "si" or bank == "no":
          ol = False
        else:
          print("Respuesta no valida")
      
      if bank == "si":
        banc = "Banco Duoc"
      else:
        banc = "No banco Duoc"

      lista8 = [asiMod, rutMod, nom, tef,banc ]

    if asiMod == 9:
      print("-"*40)
      print(lista9)
      print("-"*40)
      
      nom = input("Ingrese nuevo nombre: ")
      tef = input("Ingrese nuevo numero telefonico: ")
      ol = True
      while ol == True:
        bank = input("Es banco duoc o es un ser inferior(si o no)")
        if bank == "si" or bank == "no":
          ol = False
        else:
          print("Respuesta no valida")
      
      if bank == "si":
        banc = "Banco Duoc"
      else:
        banc = "No banco Duoc"

      lista9 = [asiMod, rutMod, nom, tef,banc ]

    if asiMod == 10:
      print("-"*40)
      print(lista10)
      print("-"*40)
      
      nom = input("Ingrese nuevo nombre: ")
      tef = input("Ingrese nuevo numero telefonico: ")
      ol = True
      while ol == True:
        bank = input("Es banco duoc o es un ser inferior(si o no)")
        if bank == "si" or bank == "no":
          ol = False
        else:
          print("Respuesta no valida")
      
      if bank == "si":
        banc = "Banco Duoc"
      else:
        banc = "No banco Duoc"

      lista10 = [asiMod, rutMod, nom, tef,banc ]

    if asiMod == 11:
      print("-"*40)
      print(lista11)
      print("-"*40)
      
      nom = input("Ingrese nuevo nombre: ")
      tef = input("Ingrese nuevo numero telefonico: ")
      ol = True
      while ol == True:
        bank = input("Es banco duoc o es un ser inferior(si o no)")
        if bank == "si" or bank == "no":
          ol = False
        else:
          print("Respuesta no valida")
      
      if bank == "si":
        banc = "Banco Duoc"
      else:
        banc = "No banco Duoc"

      lista11 = [asiMod, rutMod, nom, tef,banc ]

    if asiMod == 12:
      print("-"*40)
      print(lista12)
      print("-"*40)
      
      nom = input("Ingrese nuevo nombre: ")
      tef = input("Ingrese nuevo numero telefonico: ")
      ol = True
      while ol == True:
        bank = input("Es banco duoc o es un ser inferior(si o no)")
        if bank == "si" or bank == "no":
          ol = False
        else:
          print("Respuesta no valida")
      
      if bank == "si":
        banc = "Banco Duoc"
      else:
        banc = "No banco Duoc"

      lista12 = [asiMod, rutMod, nom, tef,banc ]

    if asiMod == 13:
      print("-"*40)
      print(lista13)
      print("-"*40)
      
      nom = input("Ingrese nuevo nombre: ")
      tef = input("Ingrese nuevo numero telefonico: ")
      ol = True
      while ol == True:
        bank = input("Es banco duoc o es un ser inferior(si o no)")
        if bank == "si" or bank == "no":
          ol = False
        else:
          print("Respuesta no valida")
      
      if bank == "si":
        banc = "Banco Duoc"
      else:
        banc = "No banco Duoc"

      lista13 = [asiMod, rutMod, nom, tef,banc ]

    if asiMod == 14:
      print("-"*40)
      print(lista14)
      print("-"*40)
      
      nom = input("Ingrese nuevo nombre: ")
      tef = input("Ingrese nuevo numero telefonico: ")
      ol = True
      while ol == True:
        bank = input("Es banco duoc o es un ser inferior(si o no)")
        if bank == "si" or bank == "no":
          ol = False
        else:
          print("Respuesta no valida")
      
      if bank == "si":
        banc = "Banco Duoc"
      else:
        banc = "No banco Duoc"

      lista14 = [asiMod, rutMod, nom, tef,banc ]

    if asiMod == 15:
      print("-"*40)
      print(lista15)
      print("-"*40)
      
      nom = input("Ingrese nuevo nombre: ")
      tef = input("Ingrese nuevo numero telefonico: ")
      ol = True
      while ol == True:
        bank = input("Es banco duoc o es un ser inferior(si o no)")
        if bank == "si" or bank == "no":
          ol = False
        else:
          print("Respuesta no valida")
      
      if bank == "si":
        banc = "Banco Duoc"
      else:
        banc = "No banco Duoc"

      lista15 = [asiMod, rutMod, nom, tef,banc ]

    if asiMod == 16:
      print("-"*40)
      print(lista16)
      print("-"*40)
      
      nom = input("Ingrese nuevo nombre: ")
      tef = input("Ingrese nuevo numero telefonico: ")
      ol = True
      while ol == True:
        bank = input("Es banco duoc o es un ser inferior(si o no)")
        if bank == "si" or bank == "no":
          ol = False
        else:
          print("Respuesta no valida")
      
      if bank == "si":
        banc = "Banco Duoc"
      else:
        banc = "No banco Duoc"

      lista16 = [asiMod, rutMod, nom, tef,banc ]

    if asiMod == 17:
      print("-"*40)
      print(lista17)
      print("-"*40)
      
      nom = input("Ingrese nuevo nombre: ")
      tef = input("Ingrese nuevo numero telefonico: ")
      ol = True
      while ol == True:
        bank = input("Es banco duoc o es un ser inferior(si o no)")
        if bank == "si" or bank == "no":
          ol = False
        else:
          print("Respuesta no valida")
      
      if bank == "si":
        banc = "Banco Duoc"
      else:
        banc = "No banco Duoc"

      lista17 = [asiMod, rutMod, nom, tef,banc ]
      
    if asiMod == 18:
      print("-"*40)
      print(lista18)
      print("-"*40)
      
      nom = input("Ingrese nuevo nombre: ")
      tef = input("Ingrese nuevo numero telefonico: ")
      ol = True
      while ol == True:
        bank = input("Es banco duoc o es un ser inferior(si o no)")
        if bank == "si" or bank == "no":
          ol = False
        else:
          print("Respuesta no valida")
      
      if bank == "si":
        banc = "Banco Duoc"
      else:
        banc = "No banco Duoc"

      lista18 = [asiMod, rutMod, nom, tef,banc ]

    if asiMod == 19:
      print("-"*40)
      print(lista19)
      print("-"*40)
      
      nom = input("Ingrese nuevo nombre: ")
      tef = input("Ingrese nuevo numero telefonico: ")
      ol = True
      while ol == True:
        bank = input("Es banco duoc o es un ser inferior(si o no)")
        if bank == "si" or bank == "no":
          ol = False
        else:
          print("Respuesta no valida")
      
      if bank == "si":
        banc = "Banco Duoc"
      else:
        banc = "No banco Duoc"

      lista19 = [asiMod, rutMod, nom, tef,banc ]

    if asiMod == 20:
      print("-"*40)
      print(lista20)
      print("-"*40)
      
      nom = input("Ingrese nuevo nombre: ")
      tef = input("Ingrese nuevo numero telefonico: ")
      ol = True
      while ol == True:
        bank = input("Es banco duoc o es un ser inferior(si o no)")
        if bank == "si" or bank == "no":
          ol = False
        else:
          print("Respuesta no valida")
      
      if bank == "si":
        banc = "Banco Duoc"
      else:
        banc = "No banco Duoc"

      lista20 = [asiMod, rutMod, nom, tef,banc ]

    if asiMod == 21:
      print("-"*40)
      print(lista21)
      print("-"*40)
      
      nom = input("Ingrese nuevo nombre: ")
      tef = input("Ingrese nuevo numero telefonico: ")
      ol = True
      while ol == True:
        bank = input("Es banco duoc o es un ser inferior(si o no)")
        if bank == "si" or bank == "no":
          ol = False
        else:
          print("Respuesta no valida")
      
      if bank == "si":
        banc = "Banco Duoc"
      else:
        banc = "No banco Duoc"

      lista21 = [asiMod, rutMod, nom, tef,banc ]

    if asiMod == 22:
      print("-"*40)
      print(lista22)
      print("-"*40)
      
      nom = input("Ingrese nuevo nombre: ")
      tef = input("Ingrese nuevo numero telefonico: ")
      ol = True
      while ol == True:
        bank = input("Es banco duoc o es un ser inferior(si o no)")
        if bank == "si" or bank == "no":
          ol = False
        else:
          print("Respuesta no valida")
      
      if bank == "si":
        banc = "Banco Duoc"
      else:
        banc = "No banco Duoc"

      lista22 = [asiMod, rutMod, nom, tef,banc ]

    if asiMod == 23:
      print("-"*40)
      print(lista23)
      print("-"*40)
      
      nom = input("Ingrese nuevo nombre: ")
      tef = input("Ingrese nuevo numero telefonico: ")
      ol = True
      while ol == True:
        bank = input("Es banco duoc o es un ser inferior(si o no)")
        if bank == "si" or bank == "no":
          ol = False
        else:
          print("Respuesta no valida")
      
      if bank == "si":
        banc = "Banco Duoc"
      else:
        banc = "No banco Duoc"

      lista23 = [asiMod, rutMod, nom, tef,banc ]

    if asiMod == 24:
      print("-"*40)
      print(lista24)
      print("-"*40)
      
      nom = input("Ingrese nuevo nombre: ")
      tef = input("Ingrese nuevo numero telefonico: ")
      ol = True
      while ol == True:
        bank = input("Es banco duoc o es un ser inferior(si o no)")
        if bank == "si" or bank == "no":
          ol = False
        else:
          print("Respuesta no valida")
      
      if bank == "si":
        banc = "Banco Duoc"
      else:
        banc = "No banco Duoc"

      lista24 = [asiMod, rutMod, nom, tef,banc ]

    if asiMod == 25:
      print("-"*40)
      print(lista25)
      print("-"*40)
      
      nom = input("Ingrese nuevo nombre: ")
      tef = input("Ingrese nuevo numero telefonico: ")
      ol = True
      while ol == True:
        bank = input("Es banco duoc o es un ser inferior(si o no)")
        if bank == "si" or bank == "no":
          ol = False
        else:
          print("Respuesta no valida")
      
      if bank == "si":
        banc = "Banco Duoc"
      else:
        banc = "No banco Duoc"

      lista25 = [asiMod, rutMod, nom, tef,banc ]

    if asiMod == 26:
      print("-"*40)
      print(lista26)
      print("-"*40)
      
      nom = input("Ingrese nuevo nombre: ")
      tef = input("Ingrese nuevo numero telefonico: ")
      ol = True
      while ol == True:
        bank = input("Es banco duoc o es un ser inferior(si o no)")
        if bank == "si" or bank == "no":
          ol = False
        else:
          print("Respuesta no valida")
      
      if bank == "si":
        banc = "Banco Duoc"
      else:
        banc = "No banco Duoc"

      lista26 = [asiMod, rutMod, nom, tef,banc ]

    if asiMod == 27:
      print("-"*40)
      print(lista27)
      print("-"*40)
      
      nom = input("Ingrese nuevo nombre: ")
      tef = input("Ingrese nuevo numero telefonico: ")
      ol = True
      while ol == True:
        bank = input("Es banco duoc o es un ser inferior(si o no)")
        if bank == "si" or bank == "no":
          ol = False
        else:
          print("Respuesta no valida")
      
      if bank == "si":
        banc = "Banco Duoc"
      else:
        banc = "No banco Duoc"

      lista27 = [asiMod, rutMod, nom, tef,banc ]

    if asiMod == 28:
      print("-"*40)
      print(lista28)
      print("-"*40)
      
      nom = input("Ingrese nuevo nombre: ")
      tef = input("Ingrese nuevo numero telefonico: ")
      ol = True
      while ol == True:
        bank = input("Es banco duoc o es un ser inferior(si o no)")
        if bank == "si" or bank == "no":
          ol = False
        else:
          print("Respuesta no valida")
      
      if bank == "si":
        banc = "Banco Duoc"
      else:
        banc = "No banco Duoc"

      lista28 = [asiMod, rutMod, nom, tef,banc ]

    if asiMod == 29:
      print("-"*40)
      print(lista29)
      print("-"*40)
      
      nom = input("Ingrese nuevo nombre: ")
      tef = input("Ingrese nuevo numero telefonico: ")
      ol = True
      while ol == True:
        bank = input("Es banco duoc o es un ser inferior(si o no)")
        if bank == "si" or bank == "no":
          ol = False
        else:
          print("Respuesta no valida")
      
      if bank == "si":
        banc = "Banco Duoc"
      else:
        banc = "No banco Duoc"

      lista29 = [asiMod, rutMod, nom, tef,banc ]

    if asiMod == 30:
      print("-"*40)
      print(lista30)
      print("-"*40)
      
      nom = input("Ingrese nuevo nombre: ")
      tef = input("Ingrese nuevo numero telefonico: ")
      ol = True
      while ol == True:
        bank = input("Es banco duoc o es un ser inferior(si o no)")
        if bank == "si" or bank == "no":
          ol = False
        else:
          print("Respuesta no valida")
      
      if bank == "si":
        banc = "Banco Duoc"
      else:
        banc = "No banco Duoc"

      lista30 = [asiMod, rutMod, nom, tef,banc ]

    if asiMod == 31:
      print("-"*40)
      print(lista31)
      print("-"*40)
      
      nom = input("Ingrese nuevo nombre: ")
      tef = input("Ingrese nuevo numero telefonico: ")
      ol = True
      while ol == True:
        bank = input("Es banco duoc o es un ser inferior(si o no)")
        if bank == "si" or bank == "no":
          ol = False
        else:
          print("Respuesta no valida")
      
      if bank == "si":
        banc = "Banco Duoc"
      else:
        banc = "No banco Duoc"

      lista31 = [asiMod, rutMod, nom, tef,banc ]

    if asiMod == 32:
      print("-"*40)
      print(lista32)
      print("-"*40)
      
      nom = input("Ingrese nuevo nombre: ")
      tef = input("Ingrese nuevo numero telefonico: ")
      ol = True
      while ol == True:
        bank = input("Es banco duoc o es un ser inferior(si o no)")
        if bank == "si" or bank == "no":
          ol = False
        else:
          print("Respuesta no valida")
      
      if bank == "si":
        banc = "Banco Duoc"
      else:
        banc = "No banco Duoc"

      lista32 = [asiMod, rutMod, nom, tef,banc ]

    if asiMod == 33:
      print("-"*40)
      print(lista33)
      print("-"*40)
      
      nom = input("Ingrese nuevo nombre: ")
      tef = input("Ingrese nuevo numero telefonico: ")
      ol = True
      while ol == True:
        bank = input("Es banco duoc o es un ser inferior(si o no)")
        if bank == "si" or bank == "no":
          ol = False
        else:
          print("Respuesta no valida")
      
      if bank == "si":
        banc = "Banco Duoc"
      else:
        banc = "No banco Duoc"

      lista33 = [asiMod, rutMod, nom, tef,banc ]

    if asiMod == 34:
      print("-"*40)
      print(lista34)
      print("-"*40)
      
      nom = input("Ingrese nuevo nombre: ")
      tef = input("Ingrese nuevo numero telefonico: ")
      ol = True
      while ol == True:
        bank = input("Es banco duoc o es un ser inferior(si o no)")
        if bank == "si" or bank == "no":
          ol = False
        else:
          print("Respuesta no valida")
      
      if bank == "si":
        banc = "Banco Duoc"
      else:
        banc = "No banco Duoc"

      lista34 = [asiMod, rutMod, nom, tef,banc ]

    if asiMod == 35:
      print("-"*40)
      print(lista35)
      print("-"*40)
      
      nom = input("Ingrese nuevo nombre: ")
      tef = input("Ingrese nuevo numero telefonico: ")
      ol = True
      while ol == True:
        bank = input("Es banco duoc o es un ser inferior(si o no)")
        if bank == "si" or bank == "no":
          ol = False
        else:
          print("Respuesta no valida")
      
      if bank == "si":
        banc = "Banco Duoc"
      else:
        banc = "No banco Duoc"

      lista35 = [asiMod, rutMod, nom, tef,banc ]

    if asiMod == 36:
      print("-"*40)
      print(lista36)
      print("-"*40)
      
      nom = input("Ingrese nuevo nombre: ")
      tef = input("Ingrese nuevo numero telefonico: ")
      ol = True
      while ol == True:
        bank = input("Es banco duoc o es un ser inferior(si o no)")
        if bank == "si" or bank == "no":
          ol = False
        else:
          print("Respuesta no valida")
      
      if bank == "si":
        banc = "Banco Duoc"
      else:
        banc = "No banco Duoc"

      lista36 = [asiMod, rutMod, nom, tef,banc ]

    if asiMod == 37:
      print("-"*40)
      print(lista37)
      print("-"*40)
      
      nom = input("Ingrese nuevo nombre: ")
      tef = input("Ingrese nuevo numero telefonico: ")
      ol = True
      while ol == True:
        bank = input("Es banco duoc o es un ser inferior(si o no)")
        if bank == "si" or bank == "no":
          ol = False
        else:
          print("Respuesta no valida")
      
      if bank == "si":
        banc = "Banco Duoc"
      else:
        banc = "No banco Duoc"

      lista37 = [asiMod, rutMod, nom, tef,banc ]

    if asiMod == 38:
      print("-"*40)
      print(lista38)
      print("-"*40)
      
      nom = input("Ingrese nuevo nombre: ")
      tef = input("Ingrese nuevo numero telefonico: ")
      ol = True
      while ol == True:
        bank = input("Es banco duoc o es un ser inferior(si o no)")
        if bank == "si" or bank == "no":
          ol = False
        else:
          print("Respuesta no valida")
      
      if bank == "si":
        banc = "Banco Duoc"
      else:
        banc = "No banco Duoc"

      lista38 = [asiMod, rutMod, nom, tef,banc ]

    if asiMod == 39:
      print("-"*40)
      print(lista39)
      print("-"*40)
      
      nom = input("Ingrese nuevo nombre: ")
      tef = input("Ingrese nuevo numero telefonico: ")
      ol = True
      while ol == True:
        bank = input("Es banco duoc o es un ser inferior(si o no)")
        if bank == "si" or bank == "no":
          ol = False
        else:
          print("Respuesta no valida")
      
      if bank == "si":
        banc = "Banco Duoc"
      else:
        banc = "No banco Duoc"

      lista39 = [asiMod, rutMod, nom, tef,banc ]

    if asiMod == 40:
      print("-"*40)
      print(lista40)
      print("-"*40)
      
      nom = input("Ingrese nuevo nombre: ")
      tef = input("Ingrese nuevo numero telefonico: ")
      ol = True
      while ol == True:
        bank = input("Es banco duoc o es un ser inferior(si o no)")
        if bank == "si" or bank == "no":
          ol = False
        else:
          print("Respuesta no valida")
      
      if bank == "si":
        banc = "Banco Duoc"
      else:
        banc = "No banco Duoc"

      lista40 = [asiMod, rutMod, nom, tef,banc ]

    if asiMod == 41:
      print("-"*40)
      print(lista41)
      print("-"*40)
      
      nom = input("Ingrese nuevo nombre: ")
      tef = input("Ingrese nuevo numero telefonico: ")
      ol = True
      while ol == True:
        bank = input("Es banco duoc o es un ser inferior(si o no)")
        if bank == "si" or bank == "no":
          ol = False
        else:
          print("Respuesta no valida")
      
      if bank == "si":
        banc = "Banco Duoc"
      else:
        banc = "No banco Duoc"

      lista41 = [asiMod, rutMod, nom, tef,banc ]

    if asiMod == 42:
      print("-"*40)
      print(lista42)
      print("-"*40)
      
      nom = input("Ingrese nuevo nombre: ")
      tef = input("Ingrese nuevo numero telefonico: ")
      ol = True
      while ol == True:
        bank = input("Es banco duoc o es un ser inferior(si o no)")
        if bank == "si" or bank == "no":
          ol = False
        else:
          print("Respuesta no valida")
      
      if bank == "si":
        banc = "Banco Duoc"
      else:
        banc = "No banco Duoc"

      lista42 = [asiMod, rutMod, nom, tef,banc ]

  except:
    print("error")
  