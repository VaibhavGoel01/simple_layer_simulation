import socket
import threading

def application_layer(msg):
    print("[Application Layer] Received message:", msg)
    return msg

def transport_layer(msg):
    print("[Transport Layer] TCP - Reliable transmission")
    return msg

def internet_layer(msg):
    print("[Internet Layer] Routing from 192.168.1.2 to 192.168.1.1")
    return msg

def data_link_layer(msg):
    print("[Data Link Layer] Framed data with MAC: AA:BB:CC:DD:EE:FF")
    return msg

def physical_layer(msg):
    print("[Physical Layer] Transmitting bits...\n")
    return msg

# Handle incoming client messages
def handle_client(conn, addr):
    print(f"[+] Connected to {addr}")
    while True:
        try:
            msg = conn.recv(1024).decode()
            if not msg:
                break
            print("\n--- Message Transmission Simulation ---")
            msg = physical_layer(
                    data_link_layer(
                        internet_layer(
                            transport_layer(
                                application_layer(msg)
                            )
                        )
                    )
                )
        except:
            break
    conn.close()
    print(f"[-] Disconnected from {addr}")

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 12345))
    server.listen(1)
    print("[*] Server listening on port 12345...")
    conn, addr = server.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()

if __name__ == "__main__":
    start_server()
