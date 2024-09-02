end = 0
calc_type = 0

while True:
    print("\nOlá bem vindo a Calculadora, oque deseja fazer? \n")
    print("1-Calcular")
    print("2-Sair")
    end = (int(input()))
    
    if end == 2:
        break

    if end == 1:
        n1 = (int(input("Qual o primeiro número do cálculo?")))
        print("Qual opereção deseja fazer?\n")

        print("\n1-Adicão")
        print("2-Subtração")
        print("3-Multiplicação")
        print("4-Divisão")
        print("5-Potenciação")
        calc_type = (int(input()))

        if calc_type == 1:
            n2 = (int(input("Qual o segundo número do cálculo")))
            soma = n1 + n2
            print(n1, "+" ,n2, "=", soma)
        
     
    
