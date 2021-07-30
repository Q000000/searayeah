import os
import pyperclip
from pynput import keyboard
from shutil import copy

TEMPLATE = "template.svg"
FIGURES_PATH = (
    os.path.dirname(os.getcwd())
    + "/ml/data_collection_and_analysis_in_python/figures/"
)


def on_activate_1():
    global CURRENT_PATH
    print("inkscape opened")

    name = pyperclip.paste()
    path_name = FIGURES_PATH + str(name) + ".svg"

    if not os.path.isfile(path_name):
        copy(str(TEMPLATE), path_name)

    os.system(f"inkscape {path_name} &> /dev/null")
    os.system(f"inkscape --export-type=pdf {path_name} --export-latex")


def on_activate_2():
    print("<ctrl>+2 pressed")


with keyboard.GlobalHotKeys(
    {"<ctrl>+1": on_activate_1, "<ctrl>+2": on_activate_2}
) as h:
    h.join()
