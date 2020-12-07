def escreva(txt):
    lin = len(txt) + 4
    print('~' * lin)
    print(f'  {txt.capitalize()}')
    print('~' * lin)

# main program
escreva('banana')
escreva('de pijamas')
escreva('quero trabalhar com programação!')