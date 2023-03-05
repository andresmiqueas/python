lista = []

print("Cuantos elementos quiere ordenar?")


cant = int(input())

i=0
while i<cant:
    print("Ingrese el elemento ",i+1)
    nom= input()
    lista.append(nom)
    i+=1
lista.sort()
print(lista)
