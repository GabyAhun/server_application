import socket
import time
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', filename='client_log_file.txt', encoding='utf-8')

def send_messages(message):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 30007))
    start_time = time.time()
    address = client.getsockname()
    logging.info(f"Connected to server at {address}.")

    try:
        message = input("Enter your message: ")
        time_to_wait = float(input("Enter the periodic sending time (number only) in sec: "))
        print("Sending message periodically...")
        while True:
            client.send(message.encode('utf-8'))
            logging.info(f"Sent message to server: {message}")
            time.sleep(time_to_wait)
    except KeyboardInterrupt:
        pass
    finally:
        client.close()
        logging.info(f"Disconnected from server.")

    end_time = time.time()

    elapsed_time = end_time - start_time
    speed = len(message) / elapsed_time
    print(f"Speed: {speed} bits per second")

def main():
    message = []
    send_messages(message)

if __name__ == "__main__":
    main()
