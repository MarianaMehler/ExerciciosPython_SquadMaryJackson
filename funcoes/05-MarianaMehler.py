'''
5 - Crie uma função chamada contar_vogais que recebe uma string como parâmetro. 
Implemente a lógica para contar o número de vogais na string e retorne o total de vogais. 
Solicite ao usuário para inserir uma frase e utilize a 
função para contar as vogais.

'''

def contar_vogais(frase):
    frase = frase.lower()
    vogais = 'aeiou'
    total_vogais = 0

    for i in vogais:
        total_vogais += frase.count(i)
    
    return total_vogais

frase_usuario = input('Digite uma frase: ')

total_vogais_frase = contar_vogais(frase_usuario)

print(f'O número total de vogais na frase é: {total_vogais_frase}')

