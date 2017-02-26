# This skeleton is valid for both Python 2.7 and Python 3.
# You should be aware of your additional code for compatibility of the Python version of your choice.

import time
from socket import *
import sys

# Get the server hostname and port as command line arguments                    
host = sys.argv[1]  # FILL IN START		# FILL IN END
port = int(sys.argv[2])  # FILL IN START		# FILL IN END
timeout = 1  # in seconds

# Create UDP client socket
# FILL IN START		
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Note the second parameter is NOT SOCK_STREAM
# but the corresponding to UDP
# Set socket timeout as 1 second

timeout = 1
clientSocket.settimeout(timeout)

# FILL IN END

# Sequence number of the ping message
ptime = 0
lostPackages = []
# Ping for 10 times
while ptime < 15:
    ptime += 1
    # Format the message to be sent as in the Lab description
    # FILL IN START		# FILL IN END
    msg = "{0} ping".format(ptime)

    try:
        # FILL IN START
        sendTime = time.time()
        # Record the "sent time"

        # Send the UDP packet with the ping message
        clientSocket.sendto(msg.encode(), (host, port))
        # Receive the server response
        datarecv, address = clientSocket.recvfrom(1024)
        recvTime = time.time()

        responsemsg = str(datarecv)

        # Record the "received time"
        # Display the server response as an output
        timeDiffms = (recvTime - sendTime) * 1000.0
        print(("{0}".format(ptime)).ljust(5) + str(responsemsg[1:]).ljust(15) + "RRT: %.6f ms" % timeDiffms)
        # Round trip time is the difference between sent and received time
        # print(recvTime - sendTime)

    # FILL IN END
    except:
        # Server does not response
        # Assume the packet is lost
        print("Request timed out.")
        lostPackages.append(ptime)
        continue

# Close the client socket
clientSocket.close()
print("Lost Packages: ", lostPackages)
