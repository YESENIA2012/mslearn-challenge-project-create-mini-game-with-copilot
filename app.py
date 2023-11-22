#write 'hello world' to the console
print("Hello, World!")
import random

def obtener_opcion_usuario():
    while True:
        opcion = input("Elige piedra, papel o tijera: ").lower()
        if opcion in ["piedra", "papel", "tijera"]:
            return opcion
        else:
            print("Opción no válida. Por favor, elige piedra, papel o tijera.")

def obtener_opcion_computadora():
    opciones = ["piedra", "papel", "tijera"]
    return random.choice(opciones)

def determinar_ganador(opcion_usuario, opcion_computadora):
    if opcion_usuario == opcion_computadora:
        return "Empate"
    elif (
        (opcion_usuario == "piedra" and opcion_computadora == "tijera") or
        (opcion_usuario == "papel" and opcion_computadora == "piedra") or
        (opcion_usuario == "tijera" and opcion_computadora == "papel")
    ):
        return "Ganaste"
    else:
        return "Perdiste"

def jugar():
    puntaje_usuario = 0

    while True:
        opcion_usuario = obtener_opcion_usuario()
        opcion_computadora = obtener_opcion_computadora()

        print(f"Tú elegiste: {opcion_usuario}")
        print(f"La computadora eligió: {opcion_computadora}")

        resultado = determinar_ganador(opcion_usuario, opcion_computadora)
        print(f"Resultado: {resultado}")

        if resultado == "Ganaste":
            puntaje_usuario += 1
        elif resultado == "Perdiste":
            puntaje_usuario -= 1

        print(f"Puntaje actual: {puntaje_usuario}")

        jugar_nuevamente = input("¿Quieres jugar nuevamente? (s/n): ").lower()
        if jugar_nuevamente != "s":
            break

    print(f"\nPuntaje final: {puntaje_usuario}")
    print("¡Gracias por jugar!")

if __name__ == "__main__":
    jugar()