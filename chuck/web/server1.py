from socket import * 

def createServer():
    # making a socket / making the phone,
    # \and later we can decide whether we want to recieve or send
    serversocket = socket(AF_INET, SOCK_STREAM)
    try:
        # this is like connect but it means i'm willing to 
        # \recieve on this port 9000 a phone call
        serversocket.bind(('localhost', 9000))
        # the server is asking the os to queue the connection 
        #\requests up to 5 if the server is busy
        serversocket.listen(5)
        while(1):
            # this accept() is blocking, it is waiting, 
            # it can sit there forever, if no one calls nothing happens
            (clientsocket, address) = serversocket.accept()
            #this line runs only we the call is connected (received a request)
            # according to the protocol, the client must send first
            # so here is recv instead of send (in the case of the browser)
            
            rd = clientsocket.recv(5000).decode()
            # we split the data, as it will be sent in one line, 
            # split every time it encounters '\n' newline
            pieces = rd.split("\n")
            if (len(pieces) > 0) : print(pieces[0])
            # the data that are going to be sent back 
            data = "HTTP/1.1 200 OK\r\n"
            data += "Content-Type: text/html; charset=utf-8\r\n"
            data += "\r\n"
            data += "<html><body><h1>Hello World</h1></body></html>\r\n\r\n"

            clientsocket.sendall(data.encode())
            # hanging up the call
            clientsocket.shutdown(SHUT_WR)
    except KeyboardInterrupt :
        print("\nShutting down...\n")
    except Exception as exc:
        print("Error: \n")
        print(exc)

    serversocket.close()

# the app gets executed from here, first displays this line
print("Access http://localhost:9000")
# and then calls function 
createServer()