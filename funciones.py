players = {}
#Menu interactuable
def menu():
    while True:
        print("1. Registrar puntajes torneo")
        print("2. Listar todos los puntajes")
        print("3. Imprimir por tipo")
        print("4. Salir")
        opcion = input("Ingrese una opción: ")
        if opcion == '1':
            registrar_puntos()
        elif opcion == '2':
            listar_puntajes()
        elif opcion == '3':
            imprimir_tipo()
        elif opcion == '4':
            break
        else:
            print("Ingrese una opción valida")
#Funcion para el tipo de jugador
def tipo(str):
    while True:
        tipo_jugador = input(f"Ingrese tipo de jugador para {str} (Principiante, Avanzado, Experto): ").lower()
        if tipo_jugador in ['principiante','avanzado','experto']:
            return tipo_jugador
        else:
            print("Ingrese una categoría valida.")
#Registra puntos en coleccion anidada
def registrar_puntos():
    id = input("Ingrese el id del jugador: ")
    nombre = input("Ingrese el nombre del jugador: ")
    apellido = input("Ingrese el apellido del jugador: ")
    puntajes = {}
    while True:
        juego = input("Ingresa el juego en el que participas (Valorant, Fortnite, Fifa) o ingresa 'listo' para terminar(debe ingresar al menos un juego para poder salir): ").lower()
        if juego == 'listo' and puntajes:
            break
        elif juego in ['valorant','fortnite','fifa']:
            while True:
                try:
                    puntos = int(input(f"Ingrese el puntaje en {juego}: "))
                except:
                    print("Ingrese solo numeros.")
                else:
                    break
            tipo_jugador = tipo(juego)
            #Se asigna una categoría de expertiz dependiendo del juego(ya que puedo ser principiante en uno y experto en otro)
            puntajes[juego] = {
                "puntos": puntos,
                "tipo_jugador": tipo_jugador
            }
        else:
            print("Juego no valido")
        players[id] = {
            "nombre": nombre,
            "apellido": apellido,
            "juego": puntajes
        }
    print ("Registro Exitoso")
#Lista los puntajes
def listar_puntajes():
    print(f"{'ID':<10}{'Nombre':<10}{'Apellido':<10}{'Juego':<10}{'Puntaje':<10}{'Tipo':<15}")
    for id, datos in players.items():
        for juego, detalles in datos['juego'].items():
            print(f"{id:<10}{datos['nombre']:<10}{datos['apellido']:<10}{juego:<10}{detalles['puntos']:<10}{detalles['tipo_jugador']:<15}")
#imprime en formato txt
def imprimir_tipo():
    tipo_jugador = tipo("imprimir")
    with open(f"puntos_{tipo_jugador}.txt", "w") as file:
        file.write(f"{'ID':<10}{'Nombre':<10}{'Apellido':<10}{'Juego':<10}{'Puntaje':<10}{'Tipo':<15}\n")
        for id, datos in players.items():
            for juego, detalles in datos['juego'].items():
                if detalles['tipo_jugador'] == tipo_jugador:
                    file.write(f"{id:<10}{datos['nombre']:<10}{datos['apellido']:<10}{juego:<10}{detalles['puntos']:<10}{detalles['tipo_jugador']:<15}\n")
    print(f"Archivo puntos_{tipo_jugador}.txt generado con exito")
