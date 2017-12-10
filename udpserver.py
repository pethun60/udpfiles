#!/usr/bin/python

import socket
import sys
from datetime import datetime

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message2 = str(datetime.now())
# Bind the socket to the port
server_address =('192.168.1.186', 10000)
address =('192.168.1.199', 5556)
print >>sys.stderr, 'starting up on %s port %s' % server_address
print >>sys.stderr, ' sending to  %s port %s' % address
sock.bind(server_address)
sent = sock.sendto(message2, address)
print >>sys.stderr, 'sent %s bytes back to %s' % (message2, address)

while True:


    print >>sys.stderr, '\nwaiting to receive message'
    data, address = sock.recvfrom(5556)


    print >>sys.stderr, 'received %s bytes from %s' % (len(data), address)
    print >>sys.stderr, data

    # if data:
        # sent = sock.sendto(message2, address)
        # print >>sys.stderr, 'sent %s bytes back to %s' % (message2, address)
