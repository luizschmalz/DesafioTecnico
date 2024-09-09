entrada = 'aAAbbb'
contador = 0

for i in range(0, len(entrada)):
    if entrada[i] == 'a' or entrada[i] == 'A':
        contador += 1
    
if contador == 0:
    print('Não há letras a na entrada')
else:
    print(f'Há {contador} letras a/A na entrada')