import socket
import threading

def application_layer(msg):
    print("[Application Layer] Preparing message:", msg)
    return msg

def transport_layer(msg):
    print("[Transport Layer] Establishing TCP connection")
    return msg

def internet_layer(msg):
    print("[Internet Layer] Sending packet from 192.168.1.1 to 192.168.1.2")
    return msg

def data_link_layer(msg):
    print("[Data Link Layer] Adding frame with MAC: 11:22:33:44:55:66")
    return msg

def physical_layer(msg):
    print("[Physical Layer] Converting to bits...\n")
    return msg

def send_messages(sock):
    while True:
        msg = input("You: ")
        print("\n--- Message Transmission Simulation ---")
        layered_msg = physical_layer(
                        data_link_layer(
                            internet_layer(
                                transport_layer(
                                    application_layer(msg)
                                )
                            )
                        )
                    )
        sock.send(layered_msg.encode())

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 12345))
    print("[*] Connected to server.")
    send_messages(client)

if __name__ == "__main__":
    start_client()