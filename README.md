# inter-process-communication

## Description
Create a program that uses 4 processes as follows. The Server process will monitor keyboard input from the user, and send the data to all Client processes.

You can use any programming language you want.

### Server

Accept user keyboard input. The user types integers and separate them by using [Space]. After clicking [Enter], server will write data to each clients via a socket, pipe, or the shared memory, respectively.

### Client1

Reads intergers from the socket and calculate the Mean value of the integers.

### Client2

Reads intergers from the pipe and calculate the Median value of the integers.

### Client3

Reads intergers from the shared memory, and then calculating the Mode value of the integers.