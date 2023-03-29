import forca
import advinhacao

def escolha():
    print("**********************")
    print("***escolha seu jogo***")
    print("**********************")

    print("(1) para forca e (2) para jogo da advinhção")

    escolha = int(input("qual jogo?: "))

    if(escolha == 1):
        print("jogando forca")
        forca.jogo()
    elif(escolha == 2):
        print("jogando advinhação")
        advinhacao.jogo()
if(__name__ == "__main__"):
    escolha()
#eu poderia criar uma função para o algoritmo utilizando def e apontar para o programa
#exepmlo if(escolha ==1)
#              foca.jogar() ou  advinhacao.jogar()
#mas tem que colocar a importação no começo do codigo r
