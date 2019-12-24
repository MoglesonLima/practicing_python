# -*- coding: UTF-8 -*-

#import random, específicando o pack randint
from random import randint

#Verificação Respostas válidas(S/N)
def verficarResp(respUser):
    if ((respUser == "S") or (respUser == "s") or (respUser == "N") or (respUser == "n")):
        respUser = True
    else:
        respUser = False
    return respUser
 
#Função pra testar
def testarChut(numero, chut):
    if  numero == chut:
        test = True
    else:
        test = False
    return test

#Verificar Type
def verficarTipo(chut):
    if  type(chut) ==  int:
        tipoInt = True
    else:
        tipoInt = False
    return tipoInt

#implementação
resp = input("Vamos jogar? (S/N)\n: ")

varBoolean = True

while varBoolean == True:
    #Verificando se a variável resp é válida
    if verficarResp(resp):
        if ((resp == "s") or (resp == "S")):
            print("Vamos lá, realizando o sorteio!")
            valor = randint(0,10)
            try:
                chut = int(input("Digite um valor entre de 0 há 10: "))
                #Verificando se o chut
                while True:
                    if testarChut(valor, chut):
                        resp = input("Parabéns você acertou, vamos continuar? (S/N): ")
                        break
                    else:
                        chut = int(input("Você errou, tente novamente: "))
             
            #Excessão caso o tipo chut não seja int
            except ValueError:
                print("Valor invalido, introduza um Nº inteiro!")
        elif((resp == "n") or (resp == "N")):
            print("Vlw... Até logo!")
            varBoolean  = False
    else:
        resp = input("Valor digitado invalido, vamos jogar? (S/N)\n: ")
