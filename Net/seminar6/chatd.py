#!/bin/python3
import socket
import threading

host = '127.0.0.0'
port = 4444

chatd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
chatd.bind((host, port))
chatd.listen()

clients = []
nicknames = []

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast('{} left the chat!'.format(nickname).encode('ascii'))
            nicknames.remove(nickname)
            break

def broadcast(message):
    for client in clients:
        client.send(message)

def receive():
    while True:
        client, address = chatd.accept()
        print("Connected with {}".format(str(address)))
        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)
        print("Nickname is {}".format(nickname))
        broadcast("{} joined chat!".format(nickname).encode('ascii'))
        client.send('Connected to server!'.encode('ascii'))
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("Chatd started")
receive()
