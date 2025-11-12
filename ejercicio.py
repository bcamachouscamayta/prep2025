import random

def leerItems():
    items = []
    try: 
        with open("items.txt", "r") as f:
            while True:
                nombre = f.readline().strip()
                if not nombre:
                    break
                tipo = f.readline().strip()
                cantidad = int(f.readline().strip())
                items.append([nombre, tipo, cantidad])
    except FileNotFoundError:
        print("No se encontró el archivo items.txt. No tendrás items.")
    return items
   
def usarItem(item, items, vida, fuerza, vidaMax):
    if item[1] == "Curar":
        print(f"Usaste el item {item[0]}, que cura {item[2]} puntos.")
        vida += item[2]
        if vida > vidaMax:
            vida = vidaMax
            print(f"Como superaste el  limite de vida, quedaste con {vida}")
        else:
            print(f"Quedaste con {vida}")
    elif item[1] == "Atacar":
        print(f"Usaste el item {item[0]}, que aumenta tu fuerza en {item[2]}.")
        fuerza += item[2]
    items.remove(item)
    return vida, fuerza

def leerEnemigo(archivo):
   nombre = archivo.readline().strip()
   if nombre == "":
      return None
   vida = int(archivo.readline())
   daño = int(archivo.readline())
   probAtaque = int(archivo.readline())

   return [nombre, vida , daño ,probAtaque]


def calcularAtaque(prob, fuerza, vida):

  ataque = random.randint (1, 100)
  if ataque <= prob:
      print("El ataque impactó")
      return vida-fuerza

  else:
       print("El ataque falló")
       return vida

a = open ("enemigos.txt", "r")

enemigo = leerEnemigo(a)

vida = 30
prob = 80
fuerza = 3
probPotenciada = 50
fuerzaPotenciada = 7

while enemigo != None and vida > 0:
   print(f"vida: {vida}")
   # Enemigo: Esqueleto, vida: 12
   print(f"Enemigo:{ enemigo[0] }, vida: {enemigo[1]}")


   decicion = input("que vas a hacer: 1) atacar , 2) ataque potenciado o 3) curarte?: ")
   while decicion not in ["1", "2", "3"]:
       print("selecione una opcion correcta")
       decicion = input("que vas a hacer: 1) atacar , 2) ataque potenciado o 3) cuararte")

   if decicion == "1":
       print(f"atacaste al enemigo!")
       enemigo[1] = calcularAtaque(probPotenciada, fuerzaPotenciada, enemigo[1])
      
   if decicion == "2":
    print(f"lanzaste un ataque potenciado!")
    enemigo[1] = calcularAtaque(probPotenciada, fuerzaPotenciada, enemigo[1])

   if decicion == "3":
       print(f"te curaste ahora tienes {vida + 5} de vida!")
       vida = vida + 5
      

   if enemigo[1] <= 0:
       print(f"derrotaste a {enemigo[0]}")
       enemigo = leerEnemigo(a)
       if enemigo != None:
           print(f"aparecio otro enemigo!{enemigo[0]}")
   else:
       print(f"{enemigo[0]} ataca!")
       vida = calcularAtaque(enemigo[3], enemigo[2],vida)


if vida <= 0:
  print("perdiste")
else:
  print("ganaste")

a.close()

