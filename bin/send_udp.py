import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 9876

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto("Hello, world", (UDP_IP, UDP_PORT))