"""

    Title: Python assignment for Singapore Polytechnic
    Desc: Electronic Services and Protection Services Application
    Author: Priya 
    Group: DICS1
    Assignment Part 2

"""

#-------------------------------------------------------------------------------------- 1. IMPORT STUFF
import os, socket, datetime
print(os.getcwd()) # get current directory


#-------------------------------------------------------------------------------------- 2. INFO
host = socket.gethostname()
port = 8888
membership_folder = "Membership"
sales_folder = "Sales"


#-------------------------------------------------------------------------------------- 3. TIMESTAMP
# to be displayed at the end when client exits
def get_current_timestamp():
    return datetime.datetime.now().strftime("Date: %d-%m-%Y | Time: %H:%M:%S")


#-------------------------------------------------------------------------------------- 4. GET FILE TO READ
def getFile(folder, filename):
    file_path = os.path.join(os.getcwd(), folder, filename + ".uvm")
    try:
        with open(file_path, "r") as f:
            temp = f.read()
        return temp
    except FileNotFoundError:
        return "File not found"


#-------------------------------------------------------------------------------------- 5. SOCKET SERVER
def start_server(host, port):
    # create socket
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(">> Socket created") 
    serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # bind socket to port
    serversocket.bind((host, port))
    print(">> Socket bind completed") 
    # it is listening
    serversocket.listen(5)
    print(">> Socket is now listening on " + str(host) + " at Port: " + str(port)) 
    print("-" * 68)

    while True:
        connection, client_address = serversocket.accept()
        with connection:
            ip, port = client_address[0], client_address[1]
            print("\n>> Accepting connection from " + ip + ":" + str(port) + "...") # inform client that server is in the process of accepting
            print("\n>> Connection established with " + ip + ":" + str(port) +  "...") # inform it is successfully est
            print("\n>> Waiting for client response now...") # waiting for response from client
            
            while True:
                try: # used try and except function due to connection reset error I encountered during coding
                    data = connection.recv(1024).decode('utf-8', errors='ignore')
                    if not data:
                        break

                    if len(data) > 0:
                        print("\n>> File to locate / download: " + str(data))
                        # Quit but don't shut the server connection.
                        if data.strip().lower() == "q":
                            print("\n>> Quitting server session...\n")
                            print(f">> Client request received at {get_current_timestamp()}\n")
                            break
                        # Exit to shutdown the server connection.
                        elif data.strip().lower() == "x":
                            print("")
                            print("-" * 68)
                            print(f"\n>> Client request to shut down server received at\n   {get_current_timestamp()}\n")
                            print("-" * 68)
                            print("\n>> Shutting down server.")
                            connection.sendall(b"!!! You have exited the server.\n\n")
                            serversocket.close()
                            return
                        else:
                            if data.startswith("m"):  # Membership receipts
                                folder = membership_folder
                                filename = data[1:]  # Remove the 'M' prefix
                            elif data.startswith("s"):  # Sales receipts
                                folder = sales_folder
                                filename = data[1:]  # Remove the 'S' prefix
                            else:
                                connection.sendall(b"File not found")
                                print("\n>> Invalid request:", data)
                                continue
                            # file_contents ---- get the file requested by client
                            file_contents = getFile(folder, filename)
                            if file_contents:
                                connection.sendall(file_contents.encode('utf-8', errors='ignore'))
                                print("\n>> Request for " + str(data) + " reply sent to client console successfully.")
                                continue
                            # Not found msg prompt when file not found
                            else:
                                connection.sendall(b"File not found")
                                print("\n>> File not found:", data)
                                continue

                except ConnectionResetError:
                    print("\n>> Connection to the server was closed unexpectedly.")
                    break

        print("\n>> Client connection closed.")
        print("-" * 68)
        print(" ")


#-------------------------------------------------------------------------------------- 6. DISPLAY SERVER STARTUP
print("")
print("-" * 68)
print(">> Starting up server on %s at Port: %s" % (host, port))
print("-" * 68)
start_server(host, port)


