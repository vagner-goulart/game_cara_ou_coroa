
import random

lancar = 1

# mensagem inicial pedindo o input
def inicializar():
  print("Cara (1) - Coroa (2) - Sair (0)")
  return input("Cara ou Coroa?: ")

# teste para saber se deu cara, coroa, ou se o jogo deve fechar
def testa_lancar(cara_ou_coroa, lancar):

  if lancar == 0:
    print("Jogo fechado")
    lancar = 0
  
  elif cara_ou_coroa == 1 and lancar == 1:
    print("Você jogou Cara...\n")
    print("Ganhou, deu CARA!")

  elif cara_ou_coroa == 2 and lancar == 2:
    print("Voce jogou Coroa...\n")
    print("Ganhou, deu COROA!")
    
  else:
    print("voce jogou {}...\n".format(
      "CARA" if lancar == 1 else "COROA"
    ))
    print("Perdeu, deu {}".format(
      "CARA" if cara_ou_coroa == 1 else "COROA"))
  print("-" * 20)
  print()

# teste para saber se algum outro valor foi digitado ou se a moeda caiu em pé
def testa_lancar_valido(lancar):

  var_p_um_porcento = random.randint(0,101)

  lancar = inicializar()

  if var_p_um_porcento == 100:
    print()
    print("Uau, a moeda caiu em pé!")
    print("Deu EMPATE")
    print()
    lancar = inicializar()

  if lancar == "1" or lancar == "2" or lancar == "0":
    print()
    return int(lancar)
  else:
    while True:

      print()
      if lancar == "": 
        print("Ei, voce precisa digitar um valor para jogar.")
      else:
        print(f"{lancar} não é uma entrada válida")
      print("Escolha um dos valores abaixo!")
      print()
      lancar = inicializar()

      if lancar == "1" or lancar == "2" or lancar == "0":
        print()
        return int(lancar)
        break


# repete o jogo ateh que alguem o feche
while lancar != 0:

  lancar = testa_lancar_valido(lancar)

  cara_ou_coroa = random.randint(1,2)

  testa_lancar(cara_ou_coroa, lancar)

