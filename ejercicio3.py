numeros= [3,16,87,7,3,14,-68,16,7,4,25]

def modificar(lista):
    lisa= []
    for numero in numeros:
        if numero in numeros:
            lista.append(numero)
        else:
            break
    print(lista)
    print(sorted(lista, reverse=True)) #utilizamos reverse para que la lista se ordene de mayor a menor
