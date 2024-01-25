# 3. Faça um programa que peça uma nota, entre zero e dez. Mostra uma mensagem casa o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

while True:
    nota = float(input("Digite uma nota entre 0 e 10: "))

    if 0 <= nota < 10:
        print(f"Você inseriu a nota {nota}.")
        break
    else:
        print(f"A nota que você inseriu é inválida. Por favor, insira uma nota entre 0 e 10")