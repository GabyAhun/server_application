import socket
import threading
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', filename='server_log_file.txt', encoding='utf-8')

def handle_client(client_socket, messages, lock):
    address = client_socket.getpeername()
    logging.info(f"Connection from {address} established.")

    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        message = data.decode('utf-8')
        with lock:
            messages.append(message)
        logging.info(f"Received message from {address}: {message}")

    logging.info("Connection closed.")
    client_socket.close()

def main():
    messages = []
    lock = threading.Lock()
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 30007))
    server.listen(5)
    logging.info("Server is listening on port 50007...")

    while True:
        client_socket, _ = server.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket, messages, lock))
        client_handler.start()

if __name__ == "__main__":
    main()
