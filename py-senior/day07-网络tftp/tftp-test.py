
from socket import *
import struct

send = struct.pack("!H8sb5sb", 1, b"test.jpg", 0, b"octet", 0)

udpsocket = socket(AF_INET, SOCK_DGRAM)
udpsocket.sendto(send,("localhost",69))
udpsocket.close()
