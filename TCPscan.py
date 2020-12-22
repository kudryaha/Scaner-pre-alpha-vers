import os
import socket
from datetime import datetime
import time
startTime = time.time()


with open("hosts.txt") as f:
    hosts_count = 0
    for line in f:
        hosts_count += 1


t1 = datetime.now()

def scan(addr):
    i = 0
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #communication domain - AF_INET (Internet протоколы).type of the socket - SOCK_STREAM; Этот тип обеспечивает последовательный, надежный, ориентированный на установление двусторонней связи поток байт
    socket.setdefaulttimeout(1)
    conn = s.connect_ex(addr) #https://www.sololearn.com/Discuss/808820/what-is-the-difference-between-connect-and-connect_ex-in-python-socket
    if conn == 0:
        i += 1
        print('Port %d: OPEN' % (i,))
        return 1
    else:
        return 0
    s.close()

def run1():
   for ip in range(0,hosts_count):
       with open("hosts.txt") as file_handler:
           for line in file_handler:
               addr = line
      if (scan(addr)):
          results = open('RESULTS.txt', 'a+')
          text_for_file =(' port %d: OPEN' %(addr,))
          results.write(text_for_file)
          results.close()
   date = time.time()
   os.rename('RESULTS.txt', '%d.txt'%(date))


ыыыыыыыыы

