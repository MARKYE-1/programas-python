import random

def jogo():

  imprime_mensagem_abertura()

  palavra_secreta = carrega_palavra_secreta()
  
  letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

  enforcou = False
  acertou = False
  erros = 0
 
  print(letras_acertadas)

  while( not enforcou and not acertou):
    chute = pede_chute()    
    if(chute in palavra_secreta):
      chute_acertado(chute,letras_acertadas,palavra_secreta)
    else:
      erros = erros + 1
      desenha_forca(erros)

    enforcou = erros == 6
    acertou = "_" not in letras_acertadas
    print(letras_acertadas)

  if(acertou):
    print("você ganhou")
    imprime_mensagem_vencedor()

  elif(enforcou):
    print("você perdeu")
    imprime_mensagem_perdedor(palavra_secreta) 

  print("FIM DO JOGO")


def imprime_mensagem_abertura():
    
  print("**********************")
  print("****jogo da forca ****")
  print("**********************")


def carrega_palavra_secreta():
  arquivo = open("palavras.txt", "r")
  palavras = []
  for linha in arquivo:
    linha = linha.strip()
    palavras.append(linha)#appende é usado para adicionar itens ao final de uma lista

  arquivo.close() 
  numero = random.randrange(0,len(palavras))
  palavra_secreta = palavras[numero].upper()
  return palavra_secreta

def inicializa_letras_acertadas(palavra_secreta):
  return ["_" for letra in palavra_secreta]
  

def pede_chute():
  chute = input("digite a palavra: ")
  chute = chute.strip().upper()#função strip para funcionar mesmo com a tecla espaço
  return chute

def chute_acertado(chute,letras_acertadas,palavra_secreta):
  index = 0
  for letra in palavra_secreta:
    if(chute == letra):#uper é utilizado para formatar palavras totalmente em maiusculas 
      letras_acertadas[index] = letra
    index = index + 1
  return chute,letras_acertadas,palavra_secreta

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")  


def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")
        print(" |            ")
        print("_|___         ")
        print()

if(__name__ == "__main__"):
  jogo()