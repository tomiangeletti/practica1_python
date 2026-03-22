import random
import string

categories = {
    "programacion": ["python", "programa", "variable", "funcion", "bucle"],
    "datos": ["cadena", "entero", "lista"]
}

score = 0
valid_chars = string.ascii_letters
index = 0
     
print("¡Bienvenido al Ahorcado!")
print()
# Mostrar categorias

print("Categorias: ")
for category in categories:
        print("-", category)
category_choiced = input("Elegi una categoria (escribir nombre de la categoria):")
# Validar que la categoria sea correcta

while category_choiced not in categories:
        category_choiced = input("Categoria invalida. Por favor elija de nuevo: ")

# Crear lista con las palabras de la categoria elegida (en orden aleatorio).

words_category_choiced = categories[category_choiced]
words_random_order = random.sample(words_category_choiced, len(words_category_choiced))

# Bucle principal

while index < len(words_category_choiced):
    guessed = []
    attempts = 6
    word = words_random_order[index]
    print("prueba 1")
    while attempts > 0 and index < len(words_category_choiced):
    # Mostrar progreso: letras adivinadas y guiones para las que faltan

        progress = ""
        for letter in word:
            if letter in guessed:
                progress += letter + " "
            else:
                progress += "_ "
        print(progress)
    # Verificar si el jugador ya adivinó la palabra completa

        if "_" not in progress:
            print("¡Ganaste!")
            score = score + 6
            print(f"Felicitaciones! Tu puntaje fue de {score} puntos.")
            print()
            print()
            choice = input("Ronda finalizada! Quieres seguir jugando? (s/n): ")
            if choice == "s":
                index += 1
                guessed = []
                attempts = 6
                word = words_random_order[index]
            elif choice == "n":
                print()
                print("Bien jugado! Hasta la proxima.")
                break
        else:
            print(f"Intentos restantes: {attempts}")
            print(f"Letras usadas: {', '.join(guessed)}")
            letter = input("Ingresá una letra: ")
            if letter in valid_chars and len(letter) == 1:
                if letter in guessed:
                    print("Ya usaste esa letra.")
                elif letter in word:
                    guessed.append(letter)
                    print("¡Bien! Esa letra está en la palabra.")
                else:
                    guessed.append(letter)
                    attempts -= 1
                    print("Esa letra no está en la palabra.")
                    score = score -1
            else:
                print("Entrada no valida.")
            print()
    print(f"¡Perdiste! La palabra era: {word}")
    score = 0
    print(f"Puntaje: {score}")
    choice = input("Ronda finalizada! Quieres seguir jugando? (s/n): ")
    if choice == "s":
        index += 1
    elif choice == "n":
        print()
        print("Bien jugado! Hasta la proxima.")
        break
