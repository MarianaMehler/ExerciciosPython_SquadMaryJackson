# 3. Escreva um script que pergunta ao usuário se ele deseja converter uma temperatura de grau Celsius para Fahrenheit ou vice-versa. Para cada opção, crie uma função.

def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("Escolha a opção de conversão:")
    print("1. Celsius para Fahrenheit")
    print("2. Fahrenheit para Celsius")

    opcao = input("Digite 1 ou 2: ")

    try:
        temperatura = float(input("Digite a temperatura: "))

        if opcao == '1':
            resultado = celsius_para_fahrenheit(temperatura)
            print(f"{temperatura} graus Celsius é igual a {resultado:.2f} graus Fahrenheit.")
        elif opcao == '2':
            resultado = fahrenheit_para_celsius(temperatura)
            print(f"{temperatura} graus Fahrenheit é igual a {resultado:.2f} graus Celsius.")
        else:
            print("Opção inválida. Por favor, escolha 1 ou 2.")
    except ValueError:
        print("Entrada inválida. Certifique-se de inserir um número válido.")

if __name__ == "__main__":
    main()
