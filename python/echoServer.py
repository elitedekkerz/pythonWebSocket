#!/usr/bin/python3
from websocket_server import WebsocketServer

server =  WebsocketServer(1337 , host='127.0.0.1')

def addClient(client):
    print('newClient')

def echo(client, server, message):
    server.send_message(client, message)

server.set_fn_new_client(addClient)
server.run_forever()
