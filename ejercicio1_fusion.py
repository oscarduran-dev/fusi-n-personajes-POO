# Clase que representa un personaje con nombre, fuerza y velocidad
class Personaje:
    def __init__(self, nombre, fuerza, velocidad):
        self.nombre = nombre                # Nombre del personaje
        self.fuerza = fuerza                # Nivel de fuerza (entero)
        self.velocidad = velocidad          # Nivel de velocidad (entero)
        
    def __repr__(self):
        # Representación legible del personaje al imprimirlo
        return f"{self.nombre}(Fuerza: {self.fuerza}, Velocidad: {self.velocidad})"
    
    def __add__(self, otro):
        # Sobrecarga del operador + para fusionar personajes
        nuevo_nombre = self.nombre + "-" + otro.nombre
        # La fuerza y velocidad fusionadas se calculan como el cuadrado del promedio
        nueva_fuerza = round(((self.fuerza + otro.fuerza) / 2) ** 2, 2)
        nueva_velocidad = round(((self.velocidad + otro.velocidad) / 2) ** 2, 2)
        return Personaje(nuevo_nombre, nueva_fuerza, nueva_velocidad)

# Lista donde se almacenan todos los personajes creados
personajes = []

# Bucle principal del programa
while True:     
    print("""Selecciona una opcion.
      1. Crear personaje
      2. Fusionar personajes
      3. Salir
      """)     
    
    try:   
        opcion = int(input("seleccione una opcion: "))  # Pedir opción al usuario
    except ValueError:
        print("Ingrese una opción válida:")             # Si no es número, mostrar error
        continue                                         # Volver a mostrar el menú

    # Opción 1: Crear personaje
    if opcion == 1:
        nombre = input("Ingresa el nombre de tu personaje: ")
        try:
            fuerza = int(input("Ingresa el nivel de fuerza de tu personaje: "))
            velocidad = int(input("Ingresa la velocidad de tu personaje(m/s):"))
            personaje = Personaje(nombre, fuerza, velocidad)  # Crear objeto
            personajes.append(personaje)                      # Agregar a la lista
            print(f"Personaje creado: {personaje}")
        except ValueError:
            print("Debes ingresar solo valores numericos para fuerza y velocidad.")

    # Opción 2: Fusionar personajes existentes
    elif opcion == 2:
        if len(personajes) < 2:
            print("Debes crear al menos otro personaje para poder fusionarlos...")
        else:
            print("Personajes disponibles:")
            for i, p in enumerate(personajes):
                print(f"{i+1}: {p}")  # Mostrar personajes con índice desde 1

            try:
                i1 = int(input("Selecciona tu primer personaje: ")) - 1        
                i2 = int(input("Selecciona tu segundo personaje: ")) - 1   

                if i1 == i2:
                    print("No puedes fusionar al mismo personaje. ") 
                else: 
                    # Usar la sobrecarga de + para fusionar
                    nuevo_personaje = personajes[i1] + personajes[i2]
                    personajes.append(nuevo_personaje)
                    print(f"Personaje fusionado: {nuevo_personaje}")
            except (ValueError, IndexError):
                # Error si se ingresa texto o un número fuera del rango
                print("Ingrese un número válido: ")     

    # Opción 3: Salir del programa
    elif opcion == 3:
        print("Hasta luego, gracias por jugar.")
        break

    # Si la opción no es válida
    else:
        print("Seleccione una opción válida.")    
    
    # Mostrar la lista actual de personajes después de cada acción
    if personajes:
        print("\n Lista de personajes actuales:")   
        for p in personajes:
            print(f"-{p}") 
