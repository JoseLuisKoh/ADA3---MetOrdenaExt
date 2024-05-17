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
    resultado.extend(lista1[i:])
    resultado.extend(lista2[j:])
    return resultado

def mezcla_equilibrada(lista):
    from collections import deque
    if len(lista) <= 1:
        return lista

    sublistas = deque()
    for elemento in lista:
        sublistas.append([elemento])

    while len(sublistas) > 1:
        sublista1 = sublistas.popleft()
        sublista2 = sublistas.popleft()
        sublistas.append(intercalacion(sublista1, sublista2))

    return sublistas[0]

# Interacción con el usuario
lista = list(map(int, input("Ingrese una lista de números desordenados, separados por espacios: ").split()))

resultado = mezcla_equilibrada(lista)
print("Resultado de la mezcla equilibrada:", resultado)
