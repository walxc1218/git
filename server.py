from socket import *
import os, sys
import time

HOST = '0.0.0.0'
PORT = 8912
ADDR = (HOST, PORT)
FILES = '/home/tarena/test/'
class FtpServer(object):
    def __init__(self, connfd):
        self.connfd = connfd

    def do_list(self):
        print('do_list')
        file_list = os.listdir(FILES)
        if not file_list:
            self.connfd.send('文件库为空'.encode())
            return
        else:
            self.connfd.send(b'OK')
            time.sleep(0.1)

        files = ''
        for file in file_list:
            if file[0] != '.' and\
                os.path.isfile(FILES + file):
                files += file + '#'

        self.connfd.send(files.encode())

    def do_get(self, filename):
        try:
            fd = open(FILES + filename, 'rb')
        except Exception as e:
            self.connfd.send('文件不存在'.encode())
            return

        self.connfd.send(b'OK')
        time.sleep(0.1)
        while True:
            data = fd.read(1024)
            if not data:
                time.sleep(0.1)
                self.connfd.send(b'##')
            self.connfd.send(data)

    def do_put(self, filename):
        if os.path.exists(FILES + filename):
            self.connfd.send('文件存在'.encode())
            return

        try:
            fd = open(FILES + filename, 'wb')
        except:
            self.connfd.send('长传失败'.encode())
            return
        self.connfd.send(b'OK')
        while True:
            data = self.connfd.recv(1024)
            if data == b'##':
                break
            fd.write(data)
        fd.close()

def main():
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sockfd.bind(ADDR)
    sockfd.listen(5)

    print('listen 8912')
    while True:
        try:
            connfd, addr = sockfd.accept()
        except KeyboardInterrupt as e:
            sockfd.close()
            sys.exit('服务器退出')
        except Exception as e:
            print('error', e)
            continue

        print('链接客户端:', addr)
        pid = os.fork()

        if pid == 0:
            p = os.fork()
            if p == 0:
                sockfd.close()
                ftp = FtpServer(connfd)
                while True:
                    data = connfd.recv(1024).decode()

                    if not data or data[0] == 'Q':
                        connfd.close()
                        sys.exit('客户端退出')
                    elif data[0] == 'L':
                        ftp.do_list()
                    elif data[0] == 'G':
                        filename = data.\
                            split(' ')[-1]
                        ftp.do_get(filename)

                    elif data[0] == 'P':
                        filename = data.\
                            split(' ')[-1]
                        ftp.do_put(filename)
            else:
                os._exit(0)
        else:
            connfd.close()
            os.wait()

main()


