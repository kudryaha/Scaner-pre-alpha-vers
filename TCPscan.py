import socket
from datetime import datetime
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
 
t1 = time.strftime("%Y.%m.%d-%H;%M;%S")
errors = False
 
def send_message():
    with open('res.txt', 'r') as f:
        filename = "res.txt"      
        attachment = MIMEText(f.read())
        attachment.add_header('Content-Disposition', 'attachment', filename=filename)
        msg = MIMEMultipart('alternative')
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login('yapishukursach@gmail.com', 'Python420420')
        toEmail, fromEmail = 'yapishukursach@gmail.com', 'yapishukursach@gmail.com'
        msg['Subject'] = 'subject'
        msg['From'] = fromEmail
        body = 'WARNING'
        content = MIMEText(body, 'plain')
        msg.attach(content)
        msg.attach(attachment)
        s.sendmail(fromEmail, toEmail, msg.as_string())
 
def diff():
    global t1
    global errors
    with open('names.txt') as names:
        with open(names.readlines()[-1].strip() + '.txt') as text_one, open(t1 + '.txt') as text_two:
            dif = []
            lines = set(text_two.readlines())
            for line in text_one:
                if line not in lines:
                    errors = True
                    dif += line
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
                f1.write(f"Port {ip}:{port} open\n")
            else:
                f1.write(f"Port {ip}:{port} closed\n")
 
 
if __name__ == '__main__':
    with open('res.txt', 'w') as result:
        for i in diff():
            result.write(i)          
    with open('names.txt', 'a') as f3:
        f3.write(t1 + '\n')
    if errors:
        print('warning message was sent')
        send_message()
    print('no warnings')
 
