import sqlite3
from ex115 import bases_codes
conn = sqlite3.connect('pessoas.db')
cursor = conn.cursor()
#
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        nome TEXT NOT NULL,
        idade TEXT NOT NULL,
        sexo TEXT NOT NULL
    );
    ''')


def get_pessoa(nome):
    cursor.execute(f'''
        SELECT idade, sexo FROM users
        WHERE nome = '{nome}'
    ''')

    if cursor.rowcount == 0:
        print('Nome não cadastrado ( use "1" para cadastrar')
    else:
        for nome in cursor.fetchall():
            print(nome)


def insert_pessoa(nome, idade, sexo):
    cursor.execute(f'''
        INSERT INTO users (nome, idade, sexo)
        VALUES( '{nome}', '{idade}', '{sexo}')
    ''')
    conn.commit()


def show_nome(cursor):
    cursor.execute(f'''
        SELECT nome FROM users;
    ''')
    for nome in cursor.fetchall():
        print(nome, end='')


def show_idade(cursor):
    cursor.execute(f'''
        SELECT idade FROM users;
    ''')
    for idade in cursor.fetchall():
        print(idade, end='')


def show_sexo(cursor):
    cursor.execute(f'''
        SELECT sexo FROM users;
    ''')
    for sexo in cursor.fetchall():
        print(sexo)


while True:
    bases_codes.lin()
    print(f'{"MENU PRINCIPAL":^35}')
    bases_codes.lin()
    bases_codes.yellow('1 - ')
    bases_codes.blue('Ver pessoas cadastradas')
    bases_codes.yellow('2 - ')
    bases_codes.blue('Cadastrar nova pessoa')
    bases_codes.yellow('3 - ')
    bases_codes.blue('Sair do Sistema')
    bases_codes.lin()
    op = bases_codes.erro('\033[0;33mSua Opção: \033[m')
    if op not in (1, 2, 3):
        while True:
            if op not in (1, 2, 3):
                bases_codes.red('ERROR. Digite uma opção válida!')
                op = bases_codes.erro('\033[0;33mSua Opção: \033[m')
            else:
                break
    if op == 1:
        bases_codes.lin()
        print(f'{"PESSOAS CADASTRADAS":^35}')
        print('As pessoas cadastradas foram:')
        show_nome(cursor), show_idade(cursor), show_sexo(cursor)
        bases_codes.lin()
    elif op == 2:
        bases_codes.lin()
        print(f'{"CADASTRO":^35}')
        nome = input('Qual nome quer cadastrar? ').lower().capitalize()
        idade = int(input(f'{nome} tem quantos anos? '))
        sexo = input(f'Qual o sexo de {nome}')
        insert_pessoa(nome, idade, sexo)
        bases_codes.lin()
    elif op == 3:
        bases_codes.lin()
        print(' OPERAÇÃO FINALIZADA COM SUCESSO!')
        bases_codes.lin()
        break

conn.close()


