from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.5)
    print()
    print('PRONTO!')


def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares sorteados, temos {soma}')


numeros= list()
sorteia(numeros)
somapar(numeros)