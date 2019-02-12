import socket
import re
import os
from datetime import datetime

class Server:
    def serv(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = 'localhost'
        self.port = 80
        self.sock.bind((self.host, self.port))
        print('waiting to connection')
        self.sock.listen(10)
        while True:
            conn, addr = self.sock.accept()
            print('connected: ', addr)
            while True:
                data = conn.recv(1024 * 64)
                conn.settimeout(10)
                if not data:
                    print('There are no connections')
                    break
                else:
                    print(data)
                    name = self.parse(data)
                    if False :
                        conn.send(b'Bad request')
                        conn.close()
                    else:
                        response = self.resp(name)
                        name = self.bufer(name)
                        conn.send(response.encode('utf-8'))
                        conn.send(name.encode('utf-8'))
                        conn.close()


    def parse(self, name)->'response':
        name = re.sub('\W', '\r', name.decode('utf-8')).split()
        print(name)
        if name[0] == 'GET':
            name_file = name[1] + '.' + name[2]
            print('Запрашиваемый файл :' + name_file)
            if os.path.exists(name_file):
                print('pk')
            return name_file
        else:
            return False


    def resp(self, name):
        response = 'HTTP/1.1 200 OK\n'
        date = datetime.now()
        response = response + 'Date: ' + (str(date) + '\n')
        size = 'Content length: ' + str(os.path.getsize(name)) + ' bytes.'
        response = response + size
        response = response + '\nContent-Type:text/html\n\n'
        print(response)
        return response

    def bufer(self, name):
        f = open(name, 'r')
        name = f.read()
        print(name)
        return name

if __name__ =='__main__':
    obj = Server()
    obj.serv()