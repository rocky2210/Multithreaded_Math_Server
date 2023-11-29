import socket
from math_server import start_new_math_thread
import colorama

colorama.init(autoreset=True)
# HOST = ''
# PORT = 8880

HOST = input(colorama.Fore.GREEN + colorama.Style.BRIGHT +"Enter the host (press Enter for default): "+colorama.Style.RESET_ALL) or ''
PORT = int(input(colorama.Fore.BLUE+ colorama.Style.BRIGHT +"Enter the port: "+colorama.Style.RESET_ALL))
print(colorama.Fore.YELLOW + colorama.Style.BRIGHT + f"\n\t\tMultithreaded Math Server\n\n" + colorama.Fore.CYAN +f"Started and listening on {colorama.Fore.GREEN}{colorama.Style.BRIGHT}{HOST}{colorama.Style.RESET_ALL}:{colorama.Fore.BLUE}{colorama.Style.BRIGHT}{PORT}\n")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# setsockopt (level,option,value)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
# Bind
s.bind((HOST, PORT))
# Lisiten 
s.listen()

while True:
    # Continuously accepts incoming connections 
    conn,addr = s.accept() 
    # each connection starts the new thread
    start_new_math_thread(conn,addr)

s.close()