#Gerdor de senhas,usuario informa se quer outra ou nao

#biblioteca interna
import secrets 
import os

#loop
while True:
    print('---------------GERADOR DE SENHAS AUTOMATICAS---------------')
    confirmar = input('\n---------------Gerar Senha (s/n)?\n').lower() #deixar caixa baixa
    os.system('cls')

    if confirmar == 's':
        print(f'SENHA GERADA: {secrets.token_urlsafe(16)}\n\n')# a numeracao é o numero de bytes da senha / nao ocnfundir com numero de caracteres
        continue
    else:
        print('\nPrograma Encerrado!')
        break

