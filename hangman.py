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

    #Definir a lista de palavras possíveis
    palavras = ["são paulo", "corinthians", "flamengo", "santos", "palmeiras", "vasco"]
    
    #Escolher uma palavra aleatória da lista 
    palavra = random.choice(palavras)

    #Criar uma lista vazia para armazenar as letras adivinhadas
    letras_advinhadas = [' _ ' for letra in palavra]

    #Definir o número máximo de tentativas permitidas
    chances = len(palavra)

    letras_erradas = []
    
    while chances > 0:

        print("".join(letras_advinhadas),"\n")
        print("Chances restantes: ", chances)

        letraTentada = input("Digite uma letra\n")

        if(letraTentada in palavra):
            
            index = 0

            for letra in palavra:
                if letraTentada == letra:
                    letras_advinhadas[index] = letra
                index = index + 1    
                resposta = ''.join(letras_advinhadas)
                
                if resposta == palavra:
                    print("Você venceu!")
                    break 
                
        else:
            chances = chances - 1
            letras_erradas.append(letraTentada)
            print("Letra incorreta\n")
        
    else:
        print("Você perdeu!\n")
        print("A plavra era", palavra)    

game()