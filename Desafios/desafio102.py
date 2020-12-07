def fatorial(num, show=False):
    """
    -> Calculates the factorial of the
    values 'num', using 'show=True'
    to show the all multiplication
    """
    from time import sleep
    fac = 1
    for c in range(num, 0, -1):
        fac *= c
        if show==True:
            if c == 1:
                print(f'1 = {fac}')
            else:
                print(f'{c} x ', end='')
                sleep(0.3)
    if show==False:
        print(f'{fac}')


### MAIN PROGRAM ###
print('-' * 27)
help(fatorial)
