import socket
import random
from threading import Thread
from datetime import datetime

SERVER_HOST = "localhost"
SERVER_PORT = 42515
separator_token = "<SEP>"
s = socket.socket()

print(f"[*] Соединение {SERVER_HOST}:{SERVER_PORT}...")
s.connect((SERVER_HOST, SERVER_PORT))
print("[+] соединен.")

name = input("Введите ваш никнейм: ")

def listen_for_messages():
    while True:
        message = s.recv(1024).decode()
        print("\n" + message)

t = Thread(target=listen_for_messages)
t.daemon = True
t.start()

while True:
    to_send =  input()
    to_send = f"{name}{separator_token}{to_send}"
    s.send(to_send.encode())
s.close()