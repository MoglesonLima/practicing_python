# -*- coding: UTF-8 -*-

#import
from random import randint

#Pergunta
play = input("Vamos jogar (S/N): ")  

laco_inicio = True
while laco_inicio:
    
    #Verificar S e N
    yes_play = (play == "S") or (play == "s")
    not_play = (play == "N") or (play == "n")
    
    if yes_play:
        print("Vamos começar!")
        num_random = randint(1, 10)
        
        #Verificando se é int
        ver_seInt = True
        while ver_seInt:
            try:
                chut = int(input("Digite um valor de 1 a 10: "))
                ver_seInt = False
            except ValueError:
                print("Valor not int!...")     
        
        #Verificar chut
        laco_chut = True
        while laco_chut:
            verificar_chut = (chut == num_random)
            try:
                if verificar_chut:
                    play = input("***Parabéns você acertou!***\nDeseja continuar jogando(S/N): ")
                    laco_chut = False
                else:
                    maior = chut < num_random
                    if maior:
                        print("O valor sorteado é maior!")
                    else:
                        print("O valor sorteado é menor!")
                    chut = int(input("OPS...Tente novamente: "))
            except ValueError:
                print("Valor not int!...")
               

    elif not_play:
        print("Vlw!!!")
        laco_inicio =  False
    else:
        play = input("Resposta invalida, introduza um valor válido (S/N): ")
