# lista com vários tipos de dados
# lista: adicionar 2 itens e remover 1
# fazer cópia real de uma lista
# cria lista com números e multiplicar cada um por 5
# gerar uma nova lista com os valores 4 e 5: a1 = [1,2,3,4,5,6] ===> [4,5]

# --------------------------------------------------------------------------------------------------------------------
# lista = ['lista', 4, True, ['atividade', 'python']]
# print(lista)

lista = ['lista', 4, True, ['atividade', 'python']]
print(lista)
print('---------------------------------------------------------------------------------------------------------------')

lista.pop(0)
lista.pop(1)
print(lista)
print('---------------------------------------------------------------------------------------------------------------')
lista.insert(0, 'listas')
print(lista)
print('---------------------------------------------------------------------------------------------------------------')

nova_lista = lista
print(f'lista: {lista} | id: {id(lista)}')
print(f'nova lista: {nova_lista} | id: {id(nova_lista)}')
print('---------------------------------------------------------------------------------------------------------------')

a2 = [1,2,3,4,5]
list = []
for num in a2: 
    list.append(5*num)

print(list)

print('---------------------------------------------------------------------------------------------------------------')

a1 = [1,2,3,4,5,6]
a3 = a1[3:5]
print(a1)
print(a3)