def es_palindromo(palabra):
    # Convierte la palabra a minúsculas para ignorar las diferencias entre mayúsculas y minúsculas
    palabra = palabra.lower()
    # Elimina los espacios en blanco de la palabra
    palabra = palabra.replace(" ", "")
    # Verifica si la palabra es igual a su inversa
    return palabra == palabra[::-1]

def main():
    palabra = input("Ingresa una palabra: ")
    if es_palindromo(palabra):
        print("¡La palabra ingresada es un palíndromo!")
    else:
        print("La palabra ingresada NO es un palíndromo.")

if __name__ == "__main__":
    main()
