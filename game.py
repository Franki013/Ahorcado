import random
from os import system

system('clear')


def read():
    global palabra
    palabra = []
    with open ("/home/franki/Documents/Code/Cursos/Python/hangman_game/data/data.txt", "r", encoding="utf-8") as f:
        for line in f:
            palabra.append(str.strip(line))

def write():
    palabras = [input(str("Agrega una palabra: "))]
    with open("/home/franki/Documents/Code/Cursos/Python/hangman_game/data/data.txt", "a", encoding="utf-8") as f:
        for palabra_agregada in palabras:
            f.write("\n")
            f.write(palabra_agregada)

def randomize():
    global palabra_random
    palabra_random = random.choice(palabra)

def game():
    global errores
    errores = 0
    progreso = []
    for i in range(len(palabra_random)):
        progreso.append("_ ")
    
    palabras_con_espacio = []
    for char in palabra_random:
        palabras_con_espacio.append(char + ' ')

    letras_usadas = []

    while errores < 7:
        if errores == 0:
            print('  ________ ')
            print('  |      | ')
            print('  |        ')
            print('  |        ')
            print('  |        ')
            print('  |        ')
            print('-----')
        elif errores == 1:
            print('  ________  ')
            print('  |      |  ')
            print('  |      o  ')
            print('  |         ')
            print('  |         ')
            print('  |         ')
            print('-----')
        elif errores == 2:
            print('  ________  ')
            print('  |      |  ')
            print('  |      o  ')
            print('  |      |  ')
            print('  |         ')
            print('  |         ')
            print('-----')
        elif errores == 3:
            print('  ________  ')
            print('  |      |  ')
            print('  |      o  ')
            print('  |      |  ')
            print('  |     / \ ')
            print('  |         ')
            print('-----')
        elif errores == 4:
            print('  ________  ')
            print('  |      |  ')
            print('  |      o  ')
            print('  |      |  ')
            print('  |     / \ ')
            print('  |         ')
            print('-----')
        elif errores == 5:
            print('  ________  ')
            print('  |      |  ')
            print('  |      o  ')
            print('  |     /|  ')
            print('  |     / \ ')
            print('  |         ')
            print('-----')
        elif errores == 6 :
            print('  ________  ')
            print('  |      |  ')
            print('  |      o  ')
            print('  |     /|\ ')
            print('  |     / \ ')
            print('  |         ')
            print('-----')     
            print('Perdiste!')
            break
               

        print(''.join(progreso))
        print("Letras usadas: ", letras_usadas)
        print('Elegi una letra:')
        letra = input()
        if letra in letras_usadas:
            print('Ya usaste esta letra...')
        else:
            letras_usadas.append(letra)
        

            error_letra = True
            for i in range(len(palabra_random)):
                if letra == palabra_random[i]:
                    progreso[i] = letra + ' '
                    error_letra = False

            if error_letra:
                errores += 1
        
            if palabras_con_espacio == progreso:
                print(''.join(progreso))
                print('Ganaste!')
                break
     
    while True:
        reset = int(input("\n \n Volver a Jugar? [1] Si / [2] No: "))
        if reset == 2:
            system("clear")
            break
        else:
            system("clear")
            run()

def run():
    while True:
        bienvenidos = int(input('''\n  Bienvenido al ahorcado, usted desea
                    \n \t [1] Jugar
                    \n \t [2] Agregar palabra
                    \n \t [3] Salir
                    \n Elegí la opción que quieras. '''))

        if bienvenidos == 1:
            read()
            randomize()
            game()

        elif bienvenidos == 2:
            write()
        elif bienvenidos == 3:
            break
        else:
            print("Elije una opcion valida")


if __name__ == '__main__':
    run()