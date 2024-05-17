def intercalacion(lista1, lista2):
    i, j = 0, 0
    resultado = []
    while i < len(lista1) and j < len(lista2):
        if lista1[i] < lista2[j]:
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1
    # Agregar los elementos restantes
    resultado.extend(lista1[i:])
    resultado.extend(lista2[j:])
    return resultado

# Interacción con el usuario
lista1 = list(map(int, input("Ingrese la primera lista de números ordenados, separados por espacios: ").split()))
lista2 = list(map(int, input("Ingrese la segunda lista de números ordenados, separados por espacios: ").split()))

resultado = intercalacion(lista1, lista2)
print("Resultado de la intercalación:", resultado)
