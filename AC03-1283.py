tempo = 0
lista = []

while tempo >= 0:
    tempo = int(input())
    if tempo >= 0:
        lista.append(tempo)

media = sum(lista) / len(lista)
    
if tempo < 0:    
    print('MEDIA: %.2f' % media)

for i in lista:
    if i < media:
        print(i)