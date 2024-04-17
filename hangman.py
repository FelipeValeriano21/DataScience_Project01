# Projeto Forca | Curso Data Science Academy 

#Importanto Pacotes 
import random
from os import system, name 

#Limpar a tela de cada execução
def limpa_tela():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def game():

    limpa_tela()

    print("\n Bem-Vindo ao Jogo da Forca do Brasileirão 2024")
    print("\n Advinhe a palavra abaixo:\n")

    palavras = ["são paulo", "corinthians", "flamengo", "santos", "palmeiras", "vasco"]

    palavra = random.choice(palavras)

    print(palavra)

    letras_descobertas = ['_' for letra in palavra]

    chances = len(palavra)

    letras_erradas = []

    while chances > 0:
        print(" ".join(letras_descobertas))
        print("\nChances restantes", chances)
        print("Letras erradas", " ".join(letras_erradas))

        tentativa = input("Digite uma letra: ").lower()

        if tentativa in palavra:
            index = 0
            
            for letra in palavra:
                
                if tentativa == letra: 
                    letras_descobertas[index] = letra
                index+= 1

            else:
                chances -= 1 
                letras_erradas.append(tentativa)

                print(letras_descobertas)

game()