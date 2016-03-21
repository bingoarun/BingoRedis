from BingoSocket import BingoSocket
from BingoDataHandler import BingoDataHandler

HOST=''
PORT=1234
FILE='file/data'

mySocket=BingoSocket(HOST,PORT)
newSocket = mySocket.createSocket()
newSocket.listen(1)
print 'Socket is now listening'
(conn, addr) = newSocket.accept()


myDataHandler = BingoDataHandler(FILE)

print 'Connected with ' + addr[0] + ':' + str(addr[1])


while True:
    # RECEIVE DATA
    data = conn.recv(1024)

    # PROCESS DATA
    tokens = data.split(' ',3)
    command = tokens[0]
    if command=='GET':
        reply = myDataHandler.getData(tokens[1])+'\n'
    elif command=='PUT':
        stored_data = myDataHandler.putData(tokens[1],tokens[2])
        reply = 'OK\n'
    elif command.rstrip()=='QUIT':
        myDataHandler.writeToFile()
        conn.send('Quit')
        break
    else:
        reply = 'Unknown command: '+command

    # SEND REPLY
    conn.send(reply)
conn.close() # When we are out of the loop, we're done, close