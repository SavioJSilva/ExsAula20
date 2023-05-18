def escreva(msg):
    # tam = len(msg) + 4 / dessa forma a linha de baixo seria: print('~' * tam).
    # seria uma linha mais simples mas seria uma linha a mais.
    print('~' * (len(msg) + 3))
    print(f'  {msg}')
    print('~' * (len(msg) + 3))


# Programa Principal
escreva('Savio jeronimo')
escreva('Curso de Python ')
escreva('CeV')