from core.utils import display_msg, zipdir
import json
from glob import glob
import os
import tqdm
import zipfile
import tempfile
import time


SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 2 * 4096 # send 4096 bytes each time step

class FileTransfer:
    def __init__(self, client):
        self.client = client
    

    def download_file(self):
        # display_msg("Downloading File")
        filename = self.client.receive_data()
        if filename == "quit":
            return
        file_content = b''
        while True:
            chunk = self.client.sock.recv(self.client.CHUNK_SIZE)

            if chunk.endswith(self.client.DELIMETER.encode()):
                chunk = chunk[:-len(self.client.DELIMETER)]

                file_content += chunk
                break
            file_content += chunk                

        temp_dir = tempfile.gettempdir()
        temp_file = temp_dir + "\\" + filename
        with open(temp_file, "wb") as file:
            file.write(file_content)
        display_msg("File " + filename + " Downloaded Successfully")

    def download_with_tqdm(self):
        display_msg("download tqdm 2")
        filename = self.client.receive_data()
        # print(filename)
        if filename == "quit":
            return
        received = self.client.sock.recv(BUFFER_SIZE).decode()
        filename, filesize = received.split(SEPARATOR)

        filename = os.path.basename(filename)
        if filename == "quit":
            return
        print(filename, "3")
        # convert to integer
        filesize = int(filesize)
        print(filesize, "4")
        progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
        temp_dir = tempfile.gettempdir()
        temp_file = temp_dir + "\\" + filename
        with open(temp_file, "wb") as f:
            for _ in progress:
                # read 1024 bytes from the socket (receive)
                bytes_read = self.client.sock.recv(BUFFER_SIZE)
                if SEPARATOR.encode() in bytes_read:
                    bytes_read = bytes_read[:-len(SEPARATOR)]    
                    f.write(bytes_read)
                    # nothing is received
                    # file transmitting is done
                    break
                
                # write to the file the bytes we just received
                f.write(bytes_read)
                # update the progress bar
                progress.update(len(bytes_read))
        display_msg("Downloaded successfully")



        


    def upload_with_tqdm(self, file_or_folder):
        display_msg("Uploading")
        if file_or_folder == "quit":
            display_msg("Exiting upload function", "r")
            return
        
        if os.path.isfile(file_or_folder):
            zipped_name = file_or_folder
        else:
            zipped_name = file_or_folder + ".zip"
            zipf = zipfile.ZipFile(zipped_name, "w", zipfile.ZIP_DEFLATED)
            zipdir(file_or_folder, zipf)
            zipf.close()
            

        file_size = os.path.getsize(zipped_name)
        self.client.sock.send(f"{zipped_name}{SEPARATOR}{file_size}".encode())
        progress = tqdm.tqdm(range(file_size), f"Sending {zipped_name}", unit="B", unit_scale=True, unit_divisor=1024)
        with open(zipped_name, "rb") as f:
            for _ in progress:
                # read the bytes from the file
                bytes_read = f.read(BUFFER_SIZE)
                if not bytes_read:
                    # file transmitting is done
                    break
                # we use sendall to assure transimission in 
                # busy networks
                self.client.sock.sendall(bytes_read)
                # update the progress bar
                progress.update(len(bytes_read))
            self.client.sock.send(SEPARATOR.encode())
        display_msg("File Sent successfully")





def send_dir_to_remote(client):
    files_list = glob("*")
    d1 = {}
    for index, file in enumerate(files_list):
        d1[index] = file
    d1_str = json.dumps(d1)

    data = d1_str + client.DELIMETER
    data_encoded = data.encode()
    client.sock.send(data_encoded)

    filename = client.receive_data()
    return filename


def download(client):
    # display_msg("Downloading file")
    display_msg("1")
    ft = FileTransfer(client)
    # ft.download_file()
    ft.download_with_tqdm()
    # display_msg("Downloaded to temp")

def upload(client):
        
    ft = FileTransfer(client)
    filename = send_dir_to_remote(client)
    # ft.upload_file(filename)
    # ft.upload_fancy(filename)
    ft.upload_with_tqdm(filename)
    display_msg("Exiting upload function")



