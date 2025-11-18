import random

def leerItems():

    items = []
    try:
        f = open("items.txt", "r", encoding = "utf-8")
    except FileNotFoundError:
        print("Advertencia: No se encontró 'items.txt'. Jugarás sin items.")
        return []
    while True:
        nombre = f.readline().strip()
        if nombre == "":
            break
        curacion = int(f.readline().strip())
        items.append([nombre, curacion])
    f.close()
    print(f"Items cargados: {[item[0] for item in items]}")
    return items


def usarItem(item, items, vida):
   
    nombre_item = item[0] #nombre pocision 0
    curacion_item = item[1] #curacion pocision 1

    print(f"Usaste {nombre_item}, que cura {curacion_item} puntos de vida")
    vida += curacion_item
   
    print(f"Quedaste con {vida} HP.")
       
    items.remove(item) # usamos el item
    return vida


def leerEnemigo(archivo):

   nombre = archivo.readline().strip()
   if not nombre :
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
items = leerItems()

vida = 30
prob = 80
fuerza = 3
probPotenciada = 50
fuerzaPotenciada = 7


while enemigo != None and vida > 0:
    print(f"vida: {vida}")
    # Enemigo: Esqueleto, vida: 12
    print(f"Enemigo:{ enemigo[0] }, vida: {enemigo[1]}")


    decicion = input("que vas a hacer: 1) atacar ,2) ataque potenciado ,3) curarte? o 4)usar un item : ")
    while decicion not in ["1", "2", "3", "4"]:
        print("selecione una opcion correcta")
        decicion = input("que vas a hacer: 1) atacar , 2) ataque potenciado ,3) cuararte o 4)usar un item : ")

    turno_cancelado = False
    if decicion == "1":
        print(f"atacaste al enemigo!")
        enemigo[1] = calcularAtaque(prob, fuerza, enemigo[1])
       
    elif decicion == "2":
            print(f"lanzaste un ataque potenciado!")
            enemigo[1] = calcularAtaque(probPotenciada, fuerzaPotenciada, enemigo[1])

    elif decicion == "3":
            print(f"te curaste ahora tienes {vida + 5} de vida!")
            vida = vida + 5
       
    elif decicion == "4":
        turno_cancelado = True
       
        if not items:
             print("¡No tienes items para usar!")
        else:
             print("Elige un item (0 para cancelar):")
             for i, item in enumerate(items):
                 print(f" {i+1}) {item[0]}")
           
             while True: # Bucle para elegir el item
                 try:
                     item_elegido = int(input("Tu elección: "))
                     if 0 < item_elegido <= len(items):
                        # Elige un item válido
                         item_a_usar = items[item_elegido - 1]
                         vida = usarItem(item_a_usar, items, vida)
                         break # Rompe el bucle de elegir item
                     elif item_elegido == 0:
                        # Cancela la selección de item
                         print("Cancelaste el uso de items.")
                         turno_cancelado = True
                         break # Rompe el bucle de elegir item
                     else:
                         print(f"Error: Elige un número entre 0 y {len(items)}")
                 except ValueError:
                     print("Error: Ingresa solo números.")

    if not turno_cancelado:
        if enemigo[1] <= 0:
            print(f"derrotaste a {enemigo[0]}")
            enemigo = leerEnemigo(a)
            if enemigo != None:
                print(f"aparecio otro enemigo!{enemigo[0]}")
        else:
            print(f"{enemigo[0]} ataca!")
            vida = calcularAtaque(enemigo[3], enemigo[2],vida)
            
if vida <= 0:
    print("_ perdiste _")
elif enemigo == None:
    print("* ¡ganaste! *")

a.close()