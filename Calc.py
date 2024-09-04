
import math

def separ():     
    print("=============================================")

def geometria():
    separ()
    pol_veri = 0

    print("Qual polígono deseja usar?\n ")
    print("\n1-Retângulo/Quadrado")
    print("2-Triângulo")
    print("3-Círculo")
    pol_veri = (int(input()))

    separ()


    if pol_veri == 1:
        separ()
        
        print("Será possível calcular: aréa, perímetro e diagonal desse retângulo\n")
        
        l1 = (float(input("Qual o valor da base do retângulo? ")))
        l2 = (float(input("Qual o valor  da altura do retângulo? ")))
        
        area_r = l1 * l2
        peri_r = (l1 * 2) + (l2 * 2)
        elv = (l1** 2) + (l2 ** 2)
        diag = math.sqrt(elv)
        
        print(f"\nA aréa desse retângulo é {area_r}")
        print(f"O perímetro é {peri_r}")
        print(f"A diagonal é {diag:.2f} \n")
        
        separ()

        
    if pol_veri == 2:
        separ()
        tp_trg = 0
        
        print("Qual o tipo desse triângulo? \n")
        print("1-Retângulo")
        print("2-Equilátero")
        tp_trg = (int(input()))
        
        separ()

        
        if tp_trg == 1:
            separ()
            
            print("Será possível calcular: aréa, perímetro e hipotenusa desse triângulo\n")
                                
            l1 = (float(input("Qual o valor da base do triângulo? ")))
            l2 = (float(input("Qual o valor  da altura do triângulo? ")))
            hpt = (float(input("Qual o valor da hipotenusa do triângulo? (Obs: caso não saiba a hipotenusa digite 0\n ")))
            
            if hpt == 0:
                elv_t = (l1** 2) + (l2** 2)
                hpt = math.sqrt(elv_t)
            
            area_tr = (l1 * l2) / 2
            peri_tr = (l1 + l2 + hpt) / 2
        
            print(f"O valor da aréa é {area_tr}")
            print(f"O valor do perímetro é {peri_tr:.2f}")
            if hpt == 0:
                print(f"E a hipotenusa é {hpt:.2f}")
            
            separ()
            

        if tp_trg == 2:
            separ()
            
            print("Será possível calcular: aréa, perímetro e altura desse triângulo\n")

            l1 = (float(input("Qual o valor do lado do triângulo? ")))

            area_te = ((l1** 2) * (math.sqrt(3))) / 4
            peri_te = l1 * 3
            alt_te = (l1 * (math.sqrt(3))) / 2

            print(f"\nA aréa desse triângulo é {area_te:.2f}")
            print(f"O perímetro é {peri_te}")
            print(f"E a altura(h) é {alt_te:.2f}")
            
            separ()


    if pol_veri == 3:
        separ()
        
        print("Será possível calcular: raio, diâmetero, comprimento e aréa desse triângulo\n")

        print("Qual a primeira informção do círculo você deseja inserir\n")
        print("1-Diâmetro")
        print("2-Raio\n")
        cir_veri = (int(input()))

        separ()

        
        if cir_veri == 1:
            separ()

            diam = (float(input("Qual o valor do diâmetro ")))

            raio = diam / 2
            compri = (2 * math.pi) * raio
            area_c = math.pi * (raio** 2)
            
            
            print(f"O raio do círculo é {raio}")
            print(f"O comprimento do círculo é {compri:.2f}")
            print(f"A aréa do círculo é {area_c:.2f}")

            print(separ())


        if cir_veri == 2:
            separ()

            raio = (float(input("Qual o valor do raio? ")))

            diam = raio * 2
            compri = (2 * math.pi) * raio
            area_c = math.pi * (raio** 2)

            print(f"O diâmetro do círculo é {diam}")
            print(f"O comprimento do círculo é {compri:.2f}")
            print(f"A aréa do círculo é {area_c:.2f}")

            separ()

def fisica():
    print("O que você deseja calcular?\n ") 
    print("1-Velocidade Média ")
    print("2-Aceleração Média ")
    fis_veri = (int(input()))
    
    if fis_veri == 1:
        separ()
        
        s = (float(input("Informe o valor de posição final ")))
        s0 = (float(input("Informe o valor de posição inicial ")))
        t = (float(input("Informe o valor de tempo final ")))
        t0 = (float(input("Informe o valor de tempo inicial ")))
        
        if (t - t0) == 0:
            print("\nNão é possível dividir por zero")
        else:
            vm = (s - s0) / (t - t0)
        
        print(f"\nA velocidade Média é {vm}")
        
        separ()
        
    if fis_veri == 2:
        separ()
        
        v = (float(input("Informe o valor de posição final ")))
        v0 = (float(input("Informe o valor de posição inicial ")))
        t = (float(input("Informe o valor de tempo final ")))
        t0 = (float(input("Informe o valor de tempo inicial ")))
        
        if (t - t0) == 0:
            print("\nNão é possível dividir por zero")
        else:
            a = (v - v0) / (t - t0)
        
        
        print(f"\nA aceleração média é {a}")
        
        separ()
        

while True: 
    separ()
    veri = 0
    
    print("O que você deseja fazer? \n")
    print("1-Calcular")
    print("2-Sair")
    veri = (int(input()))
    
    separ()

    
    if veri == 2:
        break

    
    if veri == 1: 
        separ()
        area_veri = 0
         
        print("\nQual aréa você deseja trabalhar?\n ")      
        print("1-Geometria")
        print("2-Física")
        area_veri = (int(input()))
        
        separ()

        
        if area_veri == 1:
            geometria()   

        if area_veri == 2:
            fisica()             
                         