import socket
from math_server import start_new_math_thread
from colr import *

# HOST = ''
# PORT = 8880
HOST = input(fg + stb +"Enter the host (press Enter for default): "+rs) or ''
PORT = int(input(fb + stb +"Enter the port: "+rs))

print(fy+ stb + f"\n\t\tMultithreaded Math Server\n\n" + fc +f"Started and listening on {fg}{stb}{HOST}{rs}:{fb}{stb}{PORT}{rs}\n")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
s.bind((HOST, PORT))
s.listen()

while True:
    # Continuously accepts incoming connections 
    conn,addr = s.accept() 
    # each connection starts the new thread
    start_new_math_thread(conn,addr)

s.close()