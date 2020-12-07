def leiaInt(msg):
    """
    -> The function analyzes if was typed
    numbers, letters or other things.
    numbers: print the number that was typed
    letters and other things: print an error mensage 
    and ask again.
    """
    ok = False
    while True:
        n = str(input(msg))
        if n.isnumeric():
            nu = int(n)
            ok = True
            break
        else:
            print('\033[0;31mERROR. TENTE NOVAMENTE.\033[m')
            n = str(input('Digite um numero: '))
    if ok:
        return nu
        


## MAIN PROGRAM ##

n = leiaInt('Digite um numero: ')
print(f'O numero digitado foi {n}')
help(leiaInt)