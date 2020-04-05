from core.connection import conn
from core.connection.handler import connection_handler




if __name__ == "__main__":
    client = conn.Client("192.168.0.12", 8080)
    client.connect_with_server()
    connection_handler(client)
    client.close()