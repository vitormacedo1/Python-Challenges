def leiaInt(msg):
    """
    -> The function analyzes if was typed
    numbers, letters or other things.
    numbers: print the number that was typed
    letters and other things: print an error mensage 
    and ask again.
    """
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERROR. Digite um numero inteiro válido!\033[m')
            continue
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERROR. Digite um numero real válido!\033[m')
            continue
        else:
            return n
