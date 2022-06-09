# list comprehension

x = [1, 2, 3, 4, 5]
y = [i**2 for i in x ] #pegando a lista de x e colocando em raiz quadrada
z = [i for i in x if i%2==1] #pegando os números ímpares da lista de x
'''o List Comprehension serve para descartar toda essa linha de código abaixo:
y = []
for i in x:
    y.append(i**2)

print (x)
print (y)

'''
#--------------------------------------------------------------
#exemplo 2
#função ENUMERATE
lista = ["abacate", "bola", "cachorro"]

#for i in range(len(lista)):
#    print (i, lista[i]) maneira de numerar os indices

for i, nome in enumerate(lista):
    print (i,nome)
#---------------------------------------------------------------
#exemplo 3 - Filter
def pares(i):
    if i % 2 ==0:
        return i
lista = [1,2,3,4,5,6,7,8,9,10]

lista_pares = filter(pares,lista)

print (list(lista_pares))
#---------------------------------------------------------------
#Exemplo 4 - Reduce
from functools import reduce

def soma (x,y):
    return x+y

lista = [1,3,5,10,20]

soma = reduce(soma, lista)

print(soma)



