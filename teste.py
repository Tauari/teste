def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    return a / b

def calculadora():
    print("=== Calculadora ===")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")
    
    while True:
        opcao = input("\nEscolha uma operação (1/2/3/4/5): ")
        
        if opcao == '5':
            print("Até logo!")
            break
        
        if opcao in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                
                if opcao == '1':
                    print(f"Resultado: {num1} + {num2} = {adicao(num1, num2)}")
                elif opcao == '2':
                    print(f"Resultado: {num1} - {num2} = {subtracao(num1, num2)}")
                elif opcao == '3':
                    print(f"Resultado: {num1} × {num2} = {multiplicacao(num1, num2)}")
                elif opcao == '4':
                    print(f"Resultado: {num1} ÷ {num2} = {divisao(num1, num2)}")
            except ValueError:
                print("Erro: Digite números válidos!")
        else:
            print("Opção inválida! Escolha entre 1 e 5.")

if __name__ == "__main__":
    calculadora()
