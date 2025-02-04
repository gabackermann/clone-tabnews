"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
num = input('digite um numero inteiro: ')

try:
    num_int = int(num) 
    if num_int % 2 == 0 :
        print(f'Seu número é {num_int} e ele é par')
    else:   
        print(f'Seu número é {num_int} e ele é impar')
except:
        print('Você não digitou um número inteiro')    
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
horas = input('Por favor, digite somente a Hora: ')


try:
    horas_int = int(horas)
    if 0 <= horas_int <= 23:  
        if horas_int <= 11:
            print(f'Bom dia, são {horas_int} horas.')
        elif horas_int <= 17:
            print(f'Boa tarde, são {horas_int} horas.')
        else:
            print(f'Boa noite, são {horas_int} horas.')
    else:
        print('Por favor, digite uma hora válida (entre 0 e 23).')
except ValueError:
        print('Você não digitou uma hora válida.')   
    
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Qual o seu nome?')
nome_len = len(nome)

if nome_len > 1:
    if nome_len <= 4:
        print("Seu nome é curto")
    elif nome_len <= 6:
        print("Seu nome é normal")
    else:
        print("Seu nome é muito grande")        
else:
    print('Digite mais que uma letra')     