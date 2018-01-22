import socket
UDP_IP = "127.0.0.1"
UDP_PORT = 5030

def fact(n):
  f = 1
  for i in range(1, n +1):
   f *= i
  return f

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    s = fact(int (data))
    print "received message:", s
    d = str(s)
    sock.sendto(d, addr)   
    
