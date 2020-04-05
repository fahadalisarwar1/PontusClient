from core.utils import display_msg, zipdir
import json
from glob import glob
import os
import zipfile


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


        with open(filename, "wb") as file:
            file.write(file_content)
        display_msg("File " + filename + "Downloaded Successfully")

    def upload_file(self, file_or_folder):
        display_msg("Uploading")
        if file_or_folder == "quit":
            display_msg("Exiting upload function", "r")
            return
        file_data = b''

        if os.path.isfile(file_or_folder):
            with open(file_or_folder, "rb") as file:
                file_data = file.read()
            zipped_name = os.path.splitext(file_or_folder)[0]
        else:
            zipped_name = file_or_folder + ".zip"
            zipf = zipfile.ZipFile(zipped_name, "w", zipfile.ZIP_DEFLATED)
            zipdir(file_or_folder, zipf)
            zipf.close()
            with open(zipped_name, "rb") as file:
                file_data = file.read()
            os.remove(zipped_name)
        
        encoded_data = file_data + self.client.DELIMETER.encode()

        self.client.send_data(zipped_name)

        self.client.sock.send(encoded_data)
        



def download(client):
    # display_msg("Downloading file")

    ft = FileTransfer(client)
    ft.download_file()

def upload(client):
        files_list = glob("*")
        d1 = {}
        for index, file in enumerate(files_list):
            d1[index] = file
        d1_str = json.dumps(d1)

        data = d1_str + client.DELIMETER
        data_encoded = data.encode()
        client.sock.send(data_encoded)

        filename = client.receive_data()
        ft = FileTransfer(client)

        ft.upload_file(filename)



