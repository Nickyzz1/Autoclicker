import pyautogui
import tkinter as tk
from tkinter import messagebox
import time

COORD_INPUT = (796, 185)     # onde clicar no campo de input
COORD_OPTION = (792, 215)    # onde clicar na opção do dropdown

# quantas vezes repetir
REPETICOES = 20

# tempo entre cliques
DELAY = 0.4

# contagem regressiva no terminal
def contagem_regressiva(segundos):
    for i in range(segundos, 0, -1):
        print(f"Iniciando em {i} segundos...", end='\r')
        time.sleep(1)
    print(" " * 30, end='\r') 

def iniciar():
    messagebox.showinfo("Auto Clicker", "Você tem 5 segundos pra posicionar a tela atrás!")
    contagem_regressiva(5)

    for i in range(REPETICOES):
        print(f"[{i+1}] Clicando no input")
        pyautogui.click(COORD_INPUT)
        time.sleep(DELAY)

        print(f"[{i+1}] Clicando na opção do dropdown")
        pyautogui.click(COORD_OPTION)
        time.sleep(DELAY)

    messagebox.showinfo("Auto Clicker", f"Finalizado: {REPETICOES} cliques feitos.")

# interface com botão
janela = tk.Tk() # cria janela
janela.title("Auto-Clickerzinho")
janela.geometry("200x150") # tamanho da janela

botao = tk.Button(janela, text="Iniciar", font=("Arial", 30), command=iniciar) # cria um btn na janela e chama função inciar quando clica no btn
botao.pack(expand=True) # coloca o btn na tela

janela.mainloop() # matém a janela aberta enquanto clica
