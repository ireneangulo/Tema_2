numeros= [3,16,87,7,3,14,-68,16,7,4,25]

def modificar(lista):
    lista= []
    for numero in numeros:
        if numero in numeros:
            lista.append(numero)
        else:
            break
    print(lista)
    print(sorted(lista, reverse=True)) #utilizamos reverse para que la lista se ordene de mayor a menor

    lista_temporal= []
    for numero in lista:
        if numero%2 ==0:
            lista_temporal.append(numero)
            print(lista_temporal)
    suma_numeros= sum(lista_temporal)
    lista_temporal.insert(0, suma_numeros)
    return lista_temporal
numeros_final= modificar(numeros)
print(numeros_final)

