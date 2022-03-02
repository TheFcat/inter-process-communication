import re
import socket
import subprocess
import time
from multiprocessing import shared_memory
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
    shm = shared_memory.SharedMemory(create=True, size=5000)
    client1 = subprocess.Popen(['python', 'socket_client.py'])
    # client2 = subprocess.Popen(['python', 'pipe_client.py'])
    client3 = subprocess.Popen(['python', 'shared_memory_client.py', shm.name])
    input_data = input(
        "Server is ready. You can type intergers and then click [ENTER].  Clients will show the mean, median, and mode of the input values.\n")

    inputs = input_data.strip().split()
    parsed_data = get_parsed_data(inputs)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    s.send(str(parsed_data).encode())
    s.recv(1024)
    buffer = shm.buf
    buffer[1:len(parsed_data) + 1] = bytearray(parsed_data)
    buffer[0] = len(parsed_data)
    time.sleep(5)
    s.close()
    shm.close()
    shm.unlink()