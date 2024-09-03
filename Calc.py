
import math

def separ():
    return("=============================================")

while True: 
    print(separ())
    veri = 0
    
    print("O que voçê deseja fazer? \n")
    print("1-Calcular")
    print("2-Sair")
    veri = (int(input()))
    
    print(separ())
    
    if veri == 2:
        break
    
    if veri == 1: 
        print(separ())
        area_veri = 0
         
        print("\nQual aréa voçê deseja trabalhar?\n ")      
        print("1-Geometria")
        print("2-Física")
        area_veri = (int(input()))
        
        print(separ())
        
        if area_veri == 1:
            print(separ())
            fig_veri = 0
            
            print("Qual polígono deseja usar?\n ")
            print("\n1-Retângulo")
            print("2-Triângulo")
            print("3-Círculo")
            fig_veri = (int(input()))
            
            print(separ())
            
            if fig_veri == 1:
                print(separ())
                
                l1 = (float(input("Qual o valor da base do retângulo? ")))
                l2 = (float(input("Qual o valor  da altura do retângulo? ")))
                
                area_r = l1 * l2
                peri_r = (l1 * 2) + (l2 * 2)
                elv = (l1** 2) + (l2 ** 2)
                diag = math.sqrt(elv)
                
                
                print(f"A aréa desse retângulo é {area_r}")
                print(f"O perímetro é {peri_r}")
                print(f"A diagonal é {diag} \n")
                
                print(separ())
                
            if fig_veri == 2:
                print(separ())
                tp_trg = 0
                
                print("Qual o tipo desse triângulo? \n")
                print("1-Retângulo")
                print("2-Equilátero")
                tp_trg = (int(input()))
                
                print(separ())
                
                if tp_trg == 1:
                    print(separ())
                    hip_veri = "nada"
                    
                    l1 = (float(input("Qual o valor da base do triângulo? ")))
                    l2 = (float(input("Qual o valor  da altura do triângulo? ")))
                    hpt = (float(input("Qual o valor da hipotenusa do triângulo?\n ")))
                    print("(Obs: caso não saiba a hipotenusa digite n \n)")
                    hip_veri = (str(input()))
                    
                    if hip_veri == "n":
                        elv_t = (l1** 2) + (l2** 2)
                        hpt = math.sqrt(elv_t)
                    
                    area_t = (l1 * l2) / 2
                    peri_t = (l1 + l2 + hpt) / 2
                    
                    print(f"O valor da aréa é {area_t}")
                    print(f"O valor do perímetro é {peri_t}")
                    if hip_veri == "n":
                        print(f"E a hipotenusa é {hpt}")
                        
                    print(separ())
                    
                    
                
                if tp_trg == 2:
                    print(separ())
                    
                    
                
                
                