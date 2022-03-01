import re
import socket
import time
import subprocess

from socket_client import HOST, PORT


def get_parsed_data(data):
    result = []
    pattern = '^\d+$'
    for string_input in data:
        if not re.fullmatch(pattern, string_input):
            break
        result.append(int(string_input))

    if len(data) != len(result):
        print('please input integer only')
    return result


if __name__ == '__main__':
    input_data = input(
        "Server is ready. You can type intergers and then click [ENTER].  Clients will show the mean, median, and mode of the input values.\n")

    inputs = input_data.strip().split()

    parsed_data = get_parsed_data(inputs)

    client1 = subprocess.Popen(['python', 'socket_client.py'])

    time.sleep(1)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    s.send(str(parsed_data).encode())
    s.recv(1024)
    s.close()
