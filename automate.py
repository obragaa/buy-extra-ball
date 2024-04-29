import time
import pyautogui

def comprar_bola_extra():
    # Suponha que as coordenadas do botão de compra sejam (x, y)
    x = 1708  # Substitua pelo valor correto
    y = 1399  # Substitua pelo valor correto

    # Mensagem de início da automação
    print("Iniciando automação para comprar a bola extra...")

    try:
        while True:
            # Simular clique na tela nas coordenadas do botão de compra
            pyautogui.click(x, y)
            print("Bola extra comprada com sucesso!")
            time.sleep(3)  # Espera 3 segundos antes de continuar
    except KeyboardInterrupt:
        print("\nPrograma encerrado.")

if __name__ == "__main__":
    comprar_bola_extra()
