import os
import time
import keyboard
import pyperclip
import tkinter as tk


def convert_string(text):
    """
    Converts the text to the desired encoding

    :param text: input text
    :return: converted text
    """
    replacements = {
        "´ı": "í", "´a": "á", "¨a": "ä", "´e": "é", "´i": "í", "´o": "ó", "´u": "ú", "´y": "ý",
        "t’": "ť", "l’": "ľ", "d’": "ď", "ˇs": "š", "ˇc": "č", "ˇn": "ň", "ˇz": "ž",
        "ˆo": "ô",
        "´A": "Á", "¨A": "Ä", "´E": "É", "´I": "Í", "´O": "Ó", "´U": "Ú", "´Y": "Ý",
        "T’": "Ť", "L’": "Ľ", "D’": "Ď", "ˇS": "Š", "ˇC": "Č", "ˇN": "Ň", "ˇZ": "Ž",
        "Ô": "Ô"
    }

    for key, value in replacements.items():
        text = text.replace(key, value)

    return text


def process_clipboard_content():
    """
    Processes the clipboard content.
    Timeout is set to 0.1 seconds to prevent the keyboard library
    to overrun the process_clipboard_content function.

    :return:
    """
    time.sleep(0.1)

    root = tk.Tk()
    root.withdraw()

    try:
        text = root.clipboard_get()

        converted_text = convert_string(text)
        pyperclip.copy(converted_text)
    except tk.TclError:
        # Clipboard is not text (image, audio, etc.)
        return


def exit_program(process_name):
    """
    Exits the program gracefully.
    """
    print("Exiting program.")
    os.system('taskkill /IM "' + process_name + '" /F')

if __name__ == "__main__":
    keyboard.add_hotkey('ctrl+c', process_clipboard_content)
    keyboard.wait("ctrl+0")

    exit_program(process_name="clipboard-pdf-changer.exe")



