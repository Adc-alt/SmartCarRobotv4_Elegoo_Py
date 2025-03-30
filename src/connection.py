import socket
import time

class connection:
    def __init__(self, ip="192.168.4.1", port=100, timeout=30):
        self.ip = ip
        self.port = port
        self.timeout = timeout
        self.socket = None

    def connect(self):
        try:
            if self.socket:
                self.socket.close()
            
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.settimeout(self.timeout)
            self.socket.connect((self.ip, self.port))
            time.sleep(1)  # Wait after connection
            return True
        except Exception as e:
            return False

    def send(self, message):
        if not self.socket:
            return False
        try:
            self.socket.send(message.encode())
            return True
        except Exception as e:
            return False

    def receive(self):
        if not self.socket:
            return None
        try:
            data = self.socket.recv(1024).decode()
            return data
        except socket.timeout:
            return None
        except Exception as e:
            return None

    def close(self):
        if self.socket:
            try:
                self.socket.close()
            except Exception as e:
                pass
            finally:
                self.socket = None