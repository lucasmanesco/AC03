inicio = int(input())
fim = int(input())

if inicio > fim:
    print('Nenhuma tabuada no intervalo!')

for x in range(inicio, fim+1):
    for i in range(1, 10+1):
        print(x, 'x', i, '=', x * i)
    print('----------')