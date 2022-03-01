import socket
HOST = '127.0.0.1'
PORT = 7000


class SocketClient:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((HOST, PORT))
        self.socket.listen(5)
        print('Client1 is ready')
        self.run()

    def run(self):
        conn, addr = self.socket.accept()
        input_data = conn.recv(1024)
        self.calculate_mean(eval(input_data.decode()))
        conn.send('done'.encode())
        conn.close()

    def calculate_mean(self, input_data):
        if not input_data:
            return
        mean = sum(input_data) / len(input_data)
        print(f'Mean is {mean}')


if __name__ == '__main__':
    SocketClient()