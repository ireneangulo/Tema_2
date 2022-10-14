numeros=[3,16,87,7,3,14,-68,1,54,16,7,4,25]
def modificar(lista):
    lista= list(set(lista))
    lista.sort(reverse=True) #Ordena los numeros que hay en la lista llamada numeros
    #print(lista)
    lista_temporal=[]

