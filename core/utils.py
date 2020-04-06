from colorama import init
init()
import os
from colorama import Fore, Style
from elevate import elevate


def display_msg(msg, color="g"):
    full_msg = "[+] " + msg 
    if color == "g":
        print(Fore.GREEN + full_msg)
    elif color == "y":
        print(Fore.YELLOW + full_msg)
    else:
        print(Fore.RED + full_msg)
    Style.RESET_ALL


def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))



def elevate_script():

    elevate()
    