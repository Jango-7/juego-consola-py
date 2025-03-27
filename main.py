import random
from clases.enemigo import Enemigo
from clases.jugador import Jugador


def main():
    nombre_jugador = input('Comienza la aventura. Ingresa tu nombre: ')
    
    jugador = Jugador(nombre_jugador)

    enemigos = [
        Enemigo("Alien", 50, 10), 
        Enemigo("Robot", 30, 5), 
        Enemigo("Monstruo", 70, 15)
    ]

    enemigos_derrotados = []

    print('Comienza la aventura!')

    while enemigos: # Esto va a hacer que siempre entre hasta que perdamos.
        enemigo_actual = random.choice(enemigos) # Esto elige un enemigo aleatorio
        if enemigo_actual in enemigos_derrotados:
            continue

        print(f'Te encuentras con {enemigo_actual.nombre} en tu camino')

        while enemigo_actual.salud > 0:
            accion = input('Que quieres hacer? (Atacar/Huir)').lower()

            if accion == "atacar":
                danio_jugador = jugador.atacar()
                print(f'Atacaste a {enemigo_actual.nombre}. Daño: {danio_jugador}')
                enemigo_actual.recibir_danio(danio_jugador)

                if enemigo_actual.salud > 0:
                    danio_enemigo = enemigo_actual.atacar()
                    print(f'{enemigo_actual.nombre} te ha atacado! Daño recibido: {danio_enemigo}')
                    jugador.recibir_danio(danio_enemigo)
            
            elif accion == "huir":
                print('Has huido a salvo')
                break
        
        if jugador.salud <= 0:
            print('Has perdido la partida!')
            break

        if enemigo_actual.salud <= 0:
            enemigos_derrotados.append(enemigo_actual)
            enemigos.remove(enemigo_actual)

        jugador.ganar_experiencia(20)

        continuar = input('Quieres continuar explorando? (S/N): ').lower()
        if continuar != "s":
            print("Gracias por haber jugado. Hasta la proxima")
            break
    
    if not enemigos:
        print('Felicidades, has derrotado a todos los enemigos')


if __name__ == "__main__": # Variable especial de python, que al usarla, nos asegura que solo podremos ejecutar este script desde el programa principal.
    main()