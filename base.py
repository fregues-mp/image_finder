import os
import pyautogui
from datetime import datetime
import keyboard
import cv2
import numpy as np

log_dir = r'logs'
os.makedirs(log_dir, exist_ok=True)

date_time = datetime.now().strftime("%d-%m-%Y")
file_name_log = f'LOG_{date_time}.txt'
path_log = os.path.join(log_dir, file_name_log)

log_file = open(path_log, 'a')

def log(msg):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"[{timestamp}] {msg}"
    print(log_message)
    log_file.write(log_message + '\n')

def VI():
    if keyboard.is_pressed('esc'):
        log("File: - - - 'Exit' | Finish | - - - - - - - - - - | 0")
        return True
    return False 

def DIP(image, threshold=0.8):
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)

    modelo = cv2.imread(image, cv2.IMREAD_UNCHANGED)
    if modelo is None:
        log(f"File: - - - '{image}' | Error | - - - - - - - - - - | 0")
        return None, None

    has_transparency = (modelo.shape[2] == 4) if len(modelo.shape) == 3 else False

    if has_transparency:
        bgr_modelo = modelo[:, :, :3]
        alpha_modelo = modelo[:, :, 3]
        mask = cv2.threshold(alpha_modelo, 0, 255, cv2.THRESH_BINARY)[1]
        result = cv2.matchTemplate(screenshot, bgr_modelo, cv2.TM_CCOEFF_NORMED, mask=mask)
    else:
        bgr_modelo = modelo
        result = cv2.matchTemplate(screenshot, bgr_modelo, cv2.TM_CCOEFF_NORMED)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    if max_val >= threshold:
        return max_loc, bgr_modelo.shape[:2]
    
    return None, None

def EI(name):
    pos, _ = DIP(r'data/reset.png')
    if pos:
        log(f"File: - - - '{name}' | Found | - - - - - - - - - - | 0")
        return True
    return False

def MTP(pos, size, offset_x=0, offset_y=0):
    x = pos[0] + offset_x
    y = pos[1] + offset_y
    pyautogui.moveTo(x, y)

def center(pos, size):
    MTP(pos, size, size[1] // 2, size[0] // 2)

def bottom(pos, size):
    MTP(pos, size, size[1] // 2, size[0])

def top(pos, size):
    MTP(pos, size, size[1] // 2, 0)

def left(pos, size):
    MTP(pos, size, 0, size[0] // 2)

def right(pos, size):
    MTP(pos, size, size[1], size[0] // 2)

def top_left(pos, size):
    MTP(pos, size, 0, 0)

def top_right(pos, size):
    MTP(pos, size, size[1], 0)

def bottom_left(pos, size):
    MTP(pos, size, 0, size[0])

def bottom_right(pos, size):
    MTP(pos, size, size[1], size[0])

def EI_Click(*paths, name, move_func, value): 
    for path in paths:
        pos, size = DIP(path)
        if pos:
            move_func(pos, size)
            pyautogui.click()
            log(f"File: - - - '{name}' | Found | {move_func.__name__} | 0")
            return True
        log(f"File: - - - {name} | Not Found | - - - - - - - - - - | {value}")
    return False
