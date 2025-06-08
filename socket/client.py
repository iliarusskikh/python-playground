import socket
import sys

try:
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect to the server
    client_socket.connect(('localhost', 3000))
    print("Connected to server at localhost:3000")

    while True:
        # Get user input
        msg = input("You (type 'exit' to quit): ")
        
        # Check for exit command
        if msg.lower() == 'exit':
            print("Closing connection...")
            break
        
        # Send message to server
        client_socket.send(msg.encode())
        
        # Receive response (up to 1024 bytes)
        response = client_socket.recv(1024).decode()
        print("Server:", response)

except ConnectionRefusedError:
    print("Error: Could not connect to server. Ensure the server is running on localhost:3000.")
except socket.error as e:
    print(f"Socket error: {e}")
except KeyboardInterrupt:
    print("\nClient terminated by user.")
finally:
    # Clean up the connection
    client_socket.close()
    print("Connection closed.")
