import subprocess
import threading
import time

def run_server():
    subprocess.run(["python", "server.py"])

def run_client():
    subprocess.run(["python", "client.py"])

def main():
    server_thread = threading.Thread(target=run_server)
    client_thread = threading.Thread(target=run_client)

    server_thread.start()
    time.sleep(1)
    client_thread.start()

    server_thread.join()
    client_thread.join()

if __name__ == "__main__":
    main()
