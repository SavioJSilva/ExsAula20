from time import sleep


def maior(* num):
    cont = maior = 0
    print('-' * 60)
    print('Analisando os valores:', end='')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.5)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print()
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


# Programa principal
maior(2, 9, 4, 5, 7, 1)
maior(1, 7, 8, 11, 5)
maior(5, 4, 3, 2, 1)
maior(10)
maior(0)
