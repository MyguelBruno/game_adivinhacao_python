# ~ GAME DE ADIVINHAÇÃO

import random

def jogo_de_adivinhação():
  print('Bem-vindo ao jogo de adivinhação')
  print('Estou pensando em um número entre 1 e 100')
  print('Você tem 10 tentativas para acertá-lo')

  n = random.randint(1,100)
  tentativas = 0
  max_tentativas = 10

  while tentativas < max_tentativas:
    palpite = int(input((f'\nDigite seu {tentativas + 1}° palpite:\n')))
    tentativas += 1
    
    if palpite < n:
      print('Palpite muito baixo!')
    elif palpite > n:
      print('Palpite muito alto!')
    else:
      print(f'Parabens! Você acertou em {tentativas} tentativas!')
      
      return
  
  print(f'Você errou! O número era: {n}')

jogo_de_adivinhação()
