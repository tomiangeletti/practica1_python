import random
import string
categories = {
    "programacion": ["python", "programa", "variable", "funcion", "bucle"],
    "datos": ["cadena", "entero", "lista"]
}
guessed = []
attempts = 6
score = 0
valid_chars = string.ascii_letters
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
word = random.choice(categories[category_choiced])
# Bucle principal
while attempts > 0:
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
        break
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
else:
    print(f"¡Perdiste! La palabra era: {word}")
    score = 0
    print(f"Puntaje: {score}")