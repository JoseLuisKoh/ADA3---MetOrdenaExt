
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

def mezcla_directa(lista):
    if len(lista) <= 1:
        return lista
    medio = len(lista) // 2
    izquierda = mezcla_directa(lista[:medio])
    derecha = mezcla_directa(lista[medio:])
    return intercalacion(izquierda, derecha)

# Interacción con el usuario
lista = list(map(int, input("Ingrese una lista de números desordenados, separados por espacios: ").split()))

resultado = mezcla_directa(lista)
print("Resultado de la mezcla directa:", resultado)
