def notas(*nota, situação=False):
    """
        ->The function analyzes how many
        grades, higher and lower notes,
        the averege and if 'situacao' was 
        True, show what is the situation.
        for 'nota': one ore more notes (accepts several).
        for 'situacao': optional value, indicating if should or not ad the situation.
        'return' dictionary with multiples informations about the class.
    """
    med = sum(nota) / len(nota)
    if situação:
        if med < 7:
            sit = 'RUIM'
        else:
            sit = 'BOA'
        ano = {'total': len(nota), 'maior': max(nota), 'menor': min(nota), 'média': sum(nota) / len(nota),
        'situação': sit}
    else:
        ano = {'total': len(nota), 'maior': max(nota), 'menor': min(nota), 'média': sum(nota) / len(nota)}
    return ano

### MAIN PROGRAM ###

resp = notas(
    8, 7, 7)
print(resp)
help(notas)
