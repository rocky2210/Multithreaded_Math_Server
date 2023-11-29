from subprocess import Popen, STDOUT, PIPE
from threading import Thread
import colorama

colorama.init(autoreset=True)

def start_new_math_thread(conn, addr):
    t = MathServerCommnicationThread(conn, addr)
    t.start()

class ProcessOutputThread(Thread):
    def __init__(self, proc, conn):
        Thread.__init__(self)
        self.proc = proc 
        self.conn = conn

    def run(self): 
        while not self.proc.stdout.closed and not self.conn._closed:
            try:
                self.conn.sendall(self.proc.stdout.readline())
            except Exception as e:
                print(f"Error sending data in  Host {self.addr[0]}:Port {self.addr[1]} - error {e}")
   
class MathServerCommnicationThread(Thread):
    def __init__(self,conn,addr):
        Thread.__init__(self)
        self.conn = conn
        self.addr = addr

    def run(self):
        # Print connected device information
        print(f"{colorama.Fore.BLUE}{colorama.Style.BRIGHT}{self.addr[0]} {colorama.Style.RESET_ALL}connected with back port {colorama.Fore.GREEN}{colorama.Style.BRIGHT}{self.addr[1]}...!")
        message = (colorama.Fore.YELLOW +"\n\t\tSimple Multithreaded Math Server💻 \n\nGive any math expressions, and I will answer you ...!\n\nEnter \"quit\" to exit ❌ \n\n$" +colorama.Style.RESET_ALL).encode()
        self.conn.sendall(message)

        p = Popen(['bc'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
        output = ProcessOutputThread(p, self.conn)
        output.start()

        while not p.stdout.closed or not self.conn._closed:
            try:
                data = self.conn.recv(1024)
                if not data:
                    break
                else:
                    try:
                        data = data.decode()
                        query = data.strip()
                        if query == 'quit':
                        # if query == 'quit' or query == 'exit':
                            p.communicate(query.encode(), timeout=1)
                            if p.poll() is not None:
                                print(f"{colorama.Fore.RED}{colorama.Style.BRIGHT}{self.addr[0]}{colorama.Style.RESET_ALL} : {colorama.Fore.YELLOW}{colorama.Style.BRIGHT}{self.addr[1]} is disconnected..!\n")
                                break
                        elif query == 'help':
                            help_message = (f"{colorama.Fore.BLUE}{colorama.Style.BRIGHT}\nAvailable Commands: \n"
                                            "-> Enter any valid math expression to get the result.\n"
                                            "-> Use 'quit' to exit the server.\n"
                                            f"-> Use 'help' to display this message.\n\n{colorama.Style.RESET_ALL}").encode()
                            self.conn.sendall(help_message)
                        else:
                            query = query + '\n'
                            p.stdin.write(query.encode())
                            p.stdin.flush()
                    except Exception as e:
                        print(f"Error processing data in Host {self.addr[0]}:Port {self.addr[1]} - error {e}")
            except:
                print(f"Error receiving data in Host {self.addr[0]}:Port {self.addr[1]} - error {e}")
        self.conn.close()
                        

