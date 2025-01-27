"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
Sempre começa no 0
"""
variavel = 'Olá mundo'
print(variavel[::-1])

print(variavel[-8:-2])
print(variavel[0:len(variavel):1])