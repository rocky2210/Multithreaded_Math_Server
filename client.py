import socket
from colr import *

def main():
    HOST = input(fg+stb+"Enter the server host: "+rs)
    PORT = int(input(fb+stb+"Enter the server port: "+rs))  

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
            # print(fg+stb+"Connecting to the server.....\n\n"+rs)
            print(fg+stb+"Connected to the server."+rs)

            # Receive and print the initial message from the server
            initial_message = s.recv(1024).decode()
            print(initial_message)

            while True:
                expression = input("$ ")
                if expression.lower() == 'quit':
                    break
                s.sendall(expression.encode()) # Sends expression
                data = s.recv(1024).decode() # Receives data from server
                print("Result:", data)

        except Exception as e:
            print(f"Error connection failed {e}")

    print("Closing the connection.")
    s.close()

if __name__ == "__main__":
    main()
