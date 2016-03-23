import socket
import sys

class BingoSocket:

    port=''
    host=''
    def __init__(self,host,port):
        self.port=port
        self.host=host
    def createSocket(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print 'Socket created'
        try:
            s.bind((self.host, self.port))
        except socket.error , msg:
            print 'Bind failed. Error code: ' + str(msg[0]) + 'Error message: ' + msg[1]
            sys.exit()
        print "Socket binding complete"
        return s

