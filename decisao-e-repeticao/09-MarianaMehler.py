'''
9 - O programa deve calcular e apresentar a quantidade de números pares e 
ímpares inseridos. O processo de leitura deve ser encerrado quando o usuário informar 
o valor zero. Certifique-se de incluir validações para garantir que apenas números 
positivos sejam considerados na contagem e cálculos.

'''
contador_pares = 0
contador_impares = 0

while True:
    
    try:

        num = int(input('Digite um número (digite 0 se quiser encerrar): '))
    
        if num == 0:
            break

        if num > 0:
            if num % 2 == 0:
                contador_pares += 1
            else: 
                contador_impares += 1
        else: 
            print('Digite apenas números inteiros positivos.')
    
    except ValueError:
        print('Digite um número inteiro válido.')

print(f'\nA quantidade de números pares é: ', contador_pares)
print(f'A quantidade de números ímpares é: ', contador_impares)








