from socket import *

# Define the port for both registration and DNS query
PORT = 53533

# Dictionary to store DNS records (Name: IP Address)
dns_records = {}

# Function to handle registration requests
def handle_registration(data):
    parts = data.decode().split('\n')
    name = parts[1].split('=')[1]
    ip_address = parts[2].split('=')[1]
    dns_records[name] = ip_address
    return f"Registered {name} with IP Address {ip_address}"

# Function to handle DNS queries
def handle_dns_query(data):
    parts = data.decode().split('\n')
    name = parts[1].split('=')[1]
    if name in dns_records:
        response = f"TYPE=A NAME={name} VALUE={dns_records[name]} TTL=10"
        return response

# Create a UDP socket
sock = socket(AF_INET,SOCK_DGRAM)
sock.bind(('', PORT))

# print(f"AS listening on port {PORT}")

while True:
    data, addr = sock.recvfrom(1024)
    response = None

    # Check if it's a registration request or a DNS query
    if 'VALUE' in data.decode():
        print("Register")
        response = handle_registration(data)
        sock.sendto("Success".encode(),addr)
    else:
        print("Query")
        response = handle_dns_query(data)
        sock.sendto(response.encode(),addr)
