from subprocess import Popen, STDOUT, PIPE
from threading import Thread
from colr import *

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
                print(f"Error sending data in  Host {self.addr[0]}: Port {self.addr[1]} - error {e}")

   
class MathServerCommnicationThread(Thread):
    def __init__(self,conn,addr):
        Thread.__init__(self)
        self.conn = conn
        self.addr = addr

    def run(self):
        # Print connected device information
        print(f"{fb}{stb}{self.addr[0]} {rs}connected with back port {fg}{stb}{self.addr[1]}")
        message = (fy + stb + "\n\t\tSimple Multithreaded Math Server💻 \n\n"+
                   fm + stb + "Give any math expressions, and I will answer you ...!\n\n"+
                   fm + stb + "Enter \"quit\" to exit ❌ \n\n" +rs).encode()
        
        self.conn.sendall(message)

        p = Popen(['bc'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
        output = ProcessOutputThread(p, self.conn)
        output.start()

        while not p.stdout.closed or not self.conn._closed:
            try:
                # Data receiving
                data = self.conn.recv(1024)
                if not data:
                    # disconnected message
                    print(f"{fr}{stb}{self.addr[0]}{rs} : {fy}{stb}{self.addr[1]} is disconnected..!{rs}\n")
                    break
                else:
                    try:
                        data = data.decode()
                        query = data.strip()
                        if query.lower() == 'quit':
                        # if query == 'quit' or query == 'exit': 
                            p.communicate(query.encode(), timeout=1)
                            if p.poll() is not None:
                                break
                        elif query == 'help':
                            help_message = (f"{fb}{stb}\nAvailable Commands: \n"
                                            "-> Enter any valid math expression to get the result.\n"
                                            "-> Use 'quit' to exit the server.\n"
                                            f"-> Use 'help' to display this message.\n\n{rs}").encode()
                            self.conn.sendall(help_message)
                        else:
                            query = query + '\n'
                            p.stdin.write(query.encode())
                            p.stdin.flush()
                    except Exception as e:
                        print(f"Error processing data in Host {self.addr[0]}: Port {self.addr[1]} - error {e}")
            except:
                print(f"Error receiving data in Host {self.addr[0]}: Port {self.addr[1]} - error {e}")
        self.conn.close()
                        

