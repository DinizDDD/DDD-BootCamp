
import math

with open("historico.txt", "w") as arq:
    pass

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

        if peri_r < 0 or area_r < 0 or diag < 0:
            print("Não pode haver comprimento ou tamanho negativo \n")


        print(f"\nA aréa desse retângulo é {area_r}")
        print(f"O perímetro é {peri_r}")
        print(f"A diagonal é {diag:.2f} \n")
        
        with open("historico.txt", "a") as arq:
            arq.write(f"\n{l1} * {l2} = {area_r}")
            arq.write(f"\n{l1} + {l1} + {l2} + {l2} = {peri_r}")
            arq.write(f"\nx^2 = {l1}^2 + {l2}^2 \n x^2 = {l1**2} + {l2**2} \n x^2 = {elv} \n RAIZ_{elv} = {diag} \n ")
                    
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
            
            area_tr = (l1 * l2) / 2
            peri_tr = (l1 + l2 + hpt) / 2

            if peri_tr < 0 or area_tr < 0 or hpt < 0:
                print("Não pode haver comprimento ou tamanho negativo \n")
        
            print(f"O valor da aréa é {area_tr}")
            print(f"O valor do perímetro é {peri_tr:.2f}")
            if hpt == 0:
                elv_t = (l1** 2) + (l2** 2)
                hpt = math.sqrt(elv_t)

                print(f"E a hipotenusa é {hpt:.2f}")
                
            with open("historico.txt", "a") as arq:
                arq.write(f"\n{l1} * {l2} / 2 = {area_tr}")
                arq.write(f"\n{l1} + {l2} + {hpt} = {peri_tr}")
                arq.write(f"\nx^2 = {l1}^2 + {l2}^2 \n x^2 = {l1**2} + {l2**2} \n x^2 = {elv_t} \n RAIZ_{elv_t} = {hpt} \n")
            
            separ()
            

        if tp_trg == 2:
            separ()
            
            print("Será possível calcular: aréa, perímetro e altura desse triângulo\n")

            l1 = (float(input("Qual o valor do lado do triângulo? ")))

            area_te = ((l1** 2) * (math.sqrt(3))) / 4
            peri_te = l1 * 3
            alt_te = (l1 * (math.sqrt(3))) / 2
            
            if area_te < 0 or peri_te < 0 or alt_te < 0:
                print("Não é possível ter uma altura ou comprimento menor que zero")

            if peri_te < 0 or area_te < 0 or alt_te < 0:
                print("Não pode haver comprimento ou tamanho negativo \n")

            print(f"\nA aréa desse triângulo é {area_te:.2f}")
            print(f"O perímetro é {peri_te}")
            print(f"E a altura(h) é {alt_te:.2f}")
            
            with open("historico.txt", "a") as arq:
                arq.write(f"\n{l1}^2 * RAIZ_3 / 4 = {area_te}")
                arq.write(f"\n{l1} + {l1} + {l1} = {peri_te}")
                arq.write(f"\n{l1} * RAIZ_3 / 2 = {alt_te} \n")
            
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

            if raio < 0 or compri < 0 or area_c < 0:
                print("Não pode haver comprimento ou tamanho negativo \n")
            
            if raio < 0 or compri < 0 or area_c < 0:
                print("Não é possível ter uma altura ou comprimento menor que zero")
            
            
            print(f"\nO raio do círculo é {raio}")
            print(f"O comprimento do círculo é {compri:.2f}")
            print(f"A aréa do círculo é {area_c:.2f}")
            
            with open("historico.txt", "a") as arq:
                arq.write(f"\n{diam} / 2 = {raio}")
                arq.write(f"\n2 * PI * {raio} = {compri}")
                arq.write(f"\nPI * {raio}^2 = {area_c} \n")

            separ()
 
        if cir_veri == 2:
            separ()

            raio = (float(input("Qual o valor do raio? ")))

            diam = raio * 2
            compri = (2 * math.pi) * raio
            area_c = math.pi * (raio** 2)
            
            if diam < 0 or compri < 0 or area_c < 0:
                print("Não é possível ter uma altura ou comprimento menor que zero")

            if diam < 0 or compri < 0 or area_c < 0:
                print("Não pode haver comprimento ou tamanho negativo \n")

            print(f"\nO diâmetro do círculo é {diam}")
            print(f"O comprimento do círculo é {compri:.2f}")
            print(f"A aréa do círculo é {area_c:.2f}")

            with open("historico.txt", "a") as arq:
                arq.write(f"\n{raio} * 2 = {diam}")
                arq.write(f"\n2 * PI * {raio} = {compri}")
                arq.write(f"\nPI * {raio}^2 = {area_c} \n")          

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
        
        with open("historico.txt", "a") as arq:
                arq.write(f"\n{s} - {s0} / {t} - {t0} = {vm} \n")
                       
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
        
        with open("historico.txt", "a") as arq:
                arq.write(f"\n{v} - {v0} / {t} - {t0} = {a} \n")
        
        separ()
        

while True: 
    separ()
    veri = 0
    
    print("O que você deseja fazer? \n")
    print("1-Calcular")
    print("2-Sair")
    print("3-Ver histórico")
    veri = (int(input()))
    
    separ()
    
    
    if veri == 3:
        with open("historico.txt") as file:
            content = file.read()
            print(content)

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