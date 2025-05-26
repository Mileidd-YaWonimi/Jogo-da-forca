import pgzrun
from forca import Forca
from palavras import lista_palavras
import random

WIDTH = 800
HEIGHT = 600
pontuacao = 0
jogo = None

def novo_jogo():
    global jogo
    palavra = random.choice(lista_palavras)
    jogo = Forca(palavra)

novo_jogo()

def draw():
    screen.fill((200, 200, 255))
    screen.draw.text("Jogo da Forca", center=(400, 50), fontsize=50, color="black")
    screen.draw.text(f"Pontuação: {pontuacao}", topleft=(10, 10), fontsize=30, color="black")
    screen.draw.text("Palavra: " + jogo.get_palavra_oculta(), center=(400, 150), fontsize=40, color="black")
    screen.draw.text("Letras erradas: " + ', '.join(jogo.letras_erradas), center=(400, 220), fontsize=30, color="red")

    if jogo.estado == 'perdeu':
        screen.draw.text("Você perdeu!", center=(400, 300), fontsize=50, color="red")
        screen.draw.text(f"A palavra era: {jogo.palavra}", center=(400, 360), fontsize=40, color="black")
        screen.draw.text("Pressione R para reiniciar", center=(400, 420), fontsize=30, color="black")
    elif jogo.estado == 'venceu':
        screen.draw.text("Você venceu!", center=(400, 300), fontsize=50, color="green")
        screen.draw.text("Pressione R para jogar novamente", center=(400, 360), fontsize=30, color="black")

def on_key_down(key):
    global pontuacao
    if jogo.estado == 'jogando':
        letra = key.name.upper()
        if len(letra) == 1 and letra.isalpha():
            resultado = jogo.tentar(letra)
            if resultado == 'venceu':
                pontuacao += 1
    elif key == keys.R:
        novo_jogo()

pgzrun.go()
