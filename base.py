import os
import pyautogui
from datetime import datetime
import keyboard
import cv2
import numpy as np

# LOGS
log_dir = r'logs'
os.makedirs(log_dir, exist_ok=True)

data_atual = datetime.now().strftime("%d-%m-%Y")
nome_arquivo_log = f'LOG_{data_atual}.txt'
caminho_log = os.path.join(log_dir, nome_arquivo_log)

log_file = open(caminho_log, 'a')

def log(msg):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"[{timestamp}] {msg}"
    print(log_message)
    log_file.write(log_message + '\n')

parar = False

def VI(): # parar no console
    if keyboard.is_pressed('esc'):
        log("File: - - - 'Exit' | Finish | - - - - - - - - - - | 0")
        return True
    return False 

def DIP(image, threshold=0.8): # detectar imagem na tela
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)

    modelo = cv2.imread(image, cv2.IMREAD_UNCHANGED)
    if modelo is None:
        log(f"File: - - - '{image}' | Error | - - - - - - - - - - | 0")
        return None, None

    if len(modelo.shape) == 3 and modelo.shape[2] == 4:
        bgr_modelo = modelo[:, :, :3]
        alpha_modelo = modelo[:, :, 3]
        mask = cv2.threshold(alpha_modelo, 0, 255, cv2.THRESH_BINARY)[1]
    else:
        bgr_modelo = modelo
        mask = None

    if mask is not None:
        resultado = cv2.matchTemplate(screenshot, bgr_modelo, cv2.TM_CCOEFF_NORMED, mask=mask)
    else:
        resultado = cv2.matchTemplate(screenshot, bgr_modelo, cv2.TM_CCOEFF_NORMED)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(resultado)

    if max_val >= threshold:
        return max_loc, bgr_modelo.shape[:2]

    return None, None

def EI(name):
    pos, _ = DIP(r'data/reset.png')
    if pos:
        log(f"File: - - - '{name}' | Found | - - - - - - - - - - | 0")
        return True
    return False


def EI_ClickCenter(image, name): # encontra a imagem determinada e clica
    pos, tamanho = DIP(image)
    if pos:
        centro_x = pos[0] + tamanho[1] // 2
        centro_y = pos[1] + tamanho[0] // 2
        pyautogui.moveTo(centro_x, centro_y)
        pyautogui.click()
        log(f"File: - - - '{name}' | Found | - - - - - - - - - - | 0")
        return True
    return False

def PN(*paths, name, value):
    for path in paths:
        if EI_ClickCenter(path, name):
            return True
        log(f"File: - - - {name} | Not Found | - - - - - - - - - - | {value}")
    return False
