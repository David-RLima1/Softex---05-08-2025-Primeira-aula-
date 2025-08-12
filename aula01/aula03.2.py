'''num = int(input('Digite um número: '))

for x in range(1, 11):
    print(f'{x} x {num} = {x*num}' )
'''

soma = 0
while True:
    num = int(input('Digite um número: '))
    if num == 0:
        break
    else: 
     print(num)
     soma+=num

print(f'Soma dos números digitados: {soma}')