def exibe(L):
    L.sort()
    print(*L, sep=' ')

lista = [int(n) for n in input().split()]

comando = ['início']

while comando[0] != 'encerrar':

    comando = input().split()

    if comando[0] == 'adicionar':
        lista.append(int(comando[1]))
    
    if comando[0] == 'remover':
        try:
            lista.remove(int(comando[1]))
        except:
            print('código', comando[1], 'não encontrado')

    if comando[0] == 'exibir':
        exibe(lista)

exibe(lista)