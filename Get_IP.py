#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Arya Tripathi
#
# Created:     03-11-2023
# Copyright:   (c) Arya Tripathi 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import socket

def get_local_ip():
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Connect to a remote server (doesn't have to be reachable)
        s.connect(("8.8.8.8", 80))

        # Get the local IP address
        local_ip = s.getsockname()[0]

        # Close the socket
        s.close()

        return local_ip
    except socket.error:
        return None

# Get and print the local IP address
local_ip = get_local_ip()
if local_ip:
    print("Local IP address:", local_ip)
else:
    print("Unable to retrieve local IP address.")