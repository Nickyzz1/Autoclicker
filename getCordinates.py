import pyautogui
import time
import sys

sec = 7

print("Passe o mouse sobre o input (7s)")
for i in range(sec, 0, -1):
    print(f"{i} segundos...", end='\r')
    time.sleep(1)

print(" " * 20, end='\r')  # Limpa a linha
print("Posição do input:", pyautogui.position())

print("Passe o mouse sobre a opção do dropdown (7s)")
for i in range(sec, 0, -1):
    print(f"{i} segundos...", end='\r')
    time.sleep(1)

print(" " * 20, end='\r')
print("Posição da opção:", pyautogui.position())
