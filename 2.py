def main():
    # String inserida a ser verificada
    texto = input("Insira um dado do tipo string para a verificação: ")

    # transorma tudo em minúsculo e faz a contagem
    verificacao = texto.lower().count('a')

    # verifica a exitência 
    if verificacao == 1:
        print(f"A letra 'a' aparece apenas uma vez na string.")
    elif verificacao > 1:
        print(f"A letra 'a' aparece {verificacao} vezes na string.")
    else:
        print("A letra 'a' não está presente na string.")

if __name__ == "__main__":
    main()
