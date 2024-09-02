end = 0 
veri = 0
area_veri = 0


while True: 
    print("O que voçê deseja fazer? \n")
    print("1-Calcular")
    print("2-Sair")
    veri = (int(input()))
    
    if veri == 2:
        break
    
    if veri == 1:
        print("Qual aréa voçê deseja trabalhar \n")
        
        print("1-Geometria")
        print("2-Física")
        
        if area_veri == 2:
            print("Qual figura você deseja usar \n")
            
            print("1-Retângulo")
            print("2-Triângulo")
            print("3-Círculo")
            (int(input()))
            
            if area_veri == 1:
                lado1 = (float(input("Qual o valor do 1° lado")))
                lado2 = (float(input("Qual o valor  do 2° lado")))
           
            