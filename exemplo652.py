# exemplo 5 função ZIP

lista1 = [1,2,3,4,5]
lista2 = ["abacate","bola","cachorro","dinheiro","elefante"]
lista3 = ["R$ 2,00","RS 5,00","não tem preço", "Não tem preço","não tem preço"]


#laco for com dois valores numero e nome
#no processo zip, durante o laço for, ele faz o PRINT de cada um desses elementos

for numero, nome, valor in zip(lista1,lista2,lista3):
    print(numero,nome,valor)
print ("--------------------------------------------------------")    
#-----------------------------------------------------------------
#Exemplo 6 função MAP

def dobro(x):
    return x*2
    
valor = [1,2,3,4,5]
#print(dobro(valor))#dessa forma ele duplicara a lista

#dessa forma, ele aplica em todos os valores dentro da lista
valor_dobrado = map(dobro,valor)

#for i in valor_dobrado:#um jeito de mostrar os valores dobrados.
#    print ("usando laço for",i)

valor_dobrado = list(valor_dobrado)
print("convertendo de MAP pra LIST")
print(valor_dobrado)

#função Exemplo 7 -  LAMBDA

    
valor = [1,2,3,4,5]

valor_dobrado = map(lambda i: i*2,valor)

valor_dobrado = list(valor_dobrado)
print("convertendo de MAP pra LIST")
print(valor_dobrado)

#Testes de lição
x = [1, 2, 3]
y = [i for i in x if i% 2 ==0]
print (y)