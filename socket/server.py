import socket

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to localhost:3000
server_socket.bind(('localhost', 3000))

# Listen for incoming connections (max 5 queued)
server_socket.listen(5)
print("Server listening on localhost:3000...")

try:
    while True:
        # Wait for a connection
        client_socket, client_address = server_socket.accept()
        print(f"Connected to client: {client_address}")

        try:
            while True:
                # Receive data (up to 1024 bytes)
                data = client_socket.recv(1024).decode()
                if not data:
                    # Client closed connection
                    print(f"Client {client_address} disconnected.")
                    break
                
                print(f"Received from {client_address}: {data}")
                
                # Echo back the message with a prefix
                response = f"Server received: {data}"
                client_socket.send(response.encode())
                
        except socket.error as e:
            print(f"Client error: {e}")
        finally:
            # Clean up the client connection
            client_socket.close()
            print(f"Closed connection with {client_address}")

except KeyboardInterrupt:
    print("\nServer terminated by user.")
finally:
    # Clean up the server socket
    server_socket.close()
    print("Server socket closed.")



#netstat -an | grep 3000
#kill <pid>
