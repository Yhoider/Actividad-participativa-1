def palindromo ():
    palabra = input ("Ingresa una palabra:")
    invertido = palabra [::-1]
    if palabra == invertido:
        print (palabra, "es un palindromo")
    else:
        print (palabra, "no es un palindromo")


palindromo ()