import pyautogui

# Exibe as coordenadas do mouse enquanto ele se move pela tela
print("Mova o mouse pela tela para ver as coordenadas. Pressione Ctrl+C para sair.")
try:
    while True:
        x, y = pyautogui.position()
        position_str = f'X: {x}, Y: {y}'
        print(position_str, end='\r', flush=True)
except KeyboardInterrupt:
    print("\nPrograma encerrado.")
