import socket
from datetime import datetime
import time

t1 = time.strftime("%Y.%m.%d-%H;%M;%S")
 
def diff():
    global t1
    with open('names.txt') as names:
        with open(names.readlines()[-1].strip() + '.txt') as text_one, \
                open(t1 + '.txt') as text_two:
            dif = set(text_one) ^ set(text_two)
            dif = list(dif)
            dif.sort()
            print(dif)
            return dif

def scan(ip_, port_):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #communication domain - AF_INET (Internet протоколы).
    #type of the socket - SOCK_STREAM; Этот тип обеспечивает последовательный, надежный, ориентированный на установление двусторонней связи поток байт
    socket.setdefaulttimeout(1)
    conn = s.connect_ex((ip_, port_))
    if conn == 0:
        return 1
    else:
        return 0
    
with open(t1+'.txt', 'w') as f1:
    with open('hosts.txt') as f2:
        for line in f2:
            ip = line.split()[0]
            port = int(line.split()[1])
            scan(ip, port)
            if (scan(ip, port)):
                f1.write(f"Порт {ip}:{port} открыт\n")
            else:
                f1.write(f"Порт {ip}:{port} закрыт\n")

 
if __name__ == '__main__':
    with open('res.txt', 'w') as result:
        for i in diff():
            result.write(i)
    with open('names.txt', 'a') as f3:
        f3.write(t1 + '\n')
   
