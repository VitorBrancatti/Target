def main():
    # Número inserido a ser verificado
    numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))

    valor1 = 0
    valor2 = 1

    # Verifica se o número pertence à sequência
    pertence = (numero == valor1 or numero == valor2)

    while valor2 <= numero:
        soma = valor1 + valor2
        valor1 = valor2
        valor2 = soma

        if valor1 == numero:
            pertence = True
            break

    # Resultado
    if pertence:
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} não pertence à sequência de Fibonacci.")

if __name__ == "__main__":
    main()
