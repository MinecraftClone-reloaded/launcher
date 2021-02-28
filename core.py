import os
import json

def launch_game(username):
    os.popen(f"java -jar desktop-1.0.jar name={username}")

def launch_game_server(username, host, port):
    os.popen(f"java -jar desktop-1.0.jar name={username} host={host} port={port} online")

def save_user_name(username):
    text = json.dumps({
        "username": username
    })

    with open("user.json", "w") as file:
        file.write(text)
        file.flush()

def save_server(host, port, online):
    text = json.dumps({
        "host": host,
        "port": port,
        "online": online
    })

    with open("server.json", "w") as file:
        file.write(text)
        file.flush()

def load_username():
    with open("user.json") as file:
        data = file.read()
    return json.loads(data)["username"]

def load_server():
    with open("server.json") as file:
        data = file.read()
    return json.loads(data)