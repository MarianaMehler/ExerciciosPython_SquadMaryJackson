'''
1. Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
As perguntas são:
""Telefonou para a vítima?""
""Esteve no local do crime?""
""Mora perto da vítima?""
""Devia para a vítima?""
""Já trabalhou com a vítima?""
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como ""Suspeita"", entre 3 e 4 como ""Cúmplice"" e 5 como ""Assassino"".
Caso contrário, ele será classificado como""Inocente"".
'''

question01 = str(input('Telefonou para a vítima? [S ou N]')).lower()
question02 = str(input('Esteve no local do crime? [S ou N]')).lower()
question03 = str(input('Mora perto da vítima? [S ou N]')).lower()
question04 = str(input('Devia para a vítima? [S ou N]')).lower()
question05 = str(input('Já trabalhou com a vítima? [S ou N]')).lower()

countYes = [] # Lista para armazenar as respostas positivas

def checkAnswer(questions):
    if questions == 's':
        countYes.append('s')

def sentenceCrime():
    if len(countYes) == 2:
        print('Pessoa Suspeita')
    elif len(countYes) == 3 or len(countYes) == 4:
        print('Pessoa Cúmplice')
    elif len(countYes) == 5:
        print('Pessoa Assassina')
    else:
        print('Pessoa Inocente')
  
checkAnswer(question01)
checkAnswer(question02)
checkAnswer(question03)
checkAnswer(question04)
checkAnswer(question05)
sentenceCrime()

