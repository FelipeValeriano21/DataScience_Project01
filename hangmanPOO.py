# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

	# Método Construtor

    def __init__(self,nome,pontuação = 0, erros = 0, palavra = ""):
          
          palavras = ["Amarelo", "Azul", "Verde", "Vermelho"]
          self.nome = nome
          self.palavra = random.choice(palavras)

          print("BEM VINDO AO GAME",self.nome)

	# Método para adivinhar a letra
    
    def advinharLetra(self, letra):
        for i in range(len(self.palavra)):
            print("_")
            if letra.lower() == self.palavra[i].lower():
                print(letra)  # Imprime a letra adivinhada
            else:
                print("_")  # Imprime um espaço vazio para letras não adivinhadas
        print("A palavra é ", self.palavra)



	# Método para verificar se o jogo terminou
		
	# Método para verificar se o jogador venceu
		
	# Método para não mostrar a letra no board
 
		
	# Método para checar o status do game e imprimir o board na tela


jog1 = Hangman("Felipe")
jog1.advinharLetra("a")
jog1.advinharLetra("o")


