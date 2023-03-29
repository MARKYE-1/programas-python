
import random

def jogo():

   print("***************************")
   print("seja bem vindo ao meu jogo")
   print("***************************")

   numero_secreto = random.randrange(1,101)
   a = 0
   rodada = 0
   pontos = 1000

   print("qual nivel de dificuldade?")
   print("(1) facil: (2)facil: (3)dificil )")

   nivel = int(input("difine nivel: "))
   if(nivel == 1):
       a = 20
   elif(nivel == 2):
       a = 10
   else:
       a = 5
   print(numero_secreto)

   for rodada in range (1 , a + 1):    

     print("tentativa {} de {}".format(rodada,a))
     chute = input("digite o seu numero: ")
     numero = int(chute)

     print("você digitou", chute)

     if(numero < 1 or numero > 100):
          print("digite um nnumero entre 1 e 100")
          continue

     acertou = numero_secreto == numero
     maior = numero_secreto < numero
     menor = numero_secreto > numero

     if (acertou):
          print("você acertou")
          print("seus pontos foram {}".format(pontos))
          break
     else:
          if(maior):
               print("você errou, seu chute foi maior que o numero secreto")
          elif(menor):  
              print("você errou, seu chute foi menor que o numero secreto")
          pontos_perdidos = abs(numero_secreto - numero)
          pontos = pontos - pontos_perdidos  

     print("fim de jogo")

if(__name__ == "__main__"):     
     jogo()