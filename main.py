import socket
import os
import threading
from datetime import *
from time import time
from IPy import IP

os.system('cls')


def get_banner(connection):
    return connection.recv(1024)


def check_ip(target):
    try:
        IP(target)
        return(target)
    except ValueError:
        return socket.gethostbyname(target)


target = input("Enter The Target IP Or Website Name : ")
ending_port = int(input("Last Port (enter 0 for 65500) : "))
if ending_port == 0:
    ending_port = 65500
start_time = time()
converted_ip = check_ip(target)
os.system('cls')
length = int(len(target))

print('                      Mr.Nobody..!              ')
print('+' + '-'*59 + '+')
print("| *** Make Sure That you Connected With Internet ***        |")
print('|   Target IP     :     ', target)
print('|   From Port     :      ' + '[1,' + str(ending_port) + ']')
print('| Time started    :      ' + str(datetime.now()) + '         |')
print('+' + '-'*59 + '+')

ports = []

print('\n [-_0] Scanning Target : ' +
      str(target) + '\n')


def scan(port):
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    try:
        connection.connect((target, port))
        connection.close()
        print('[*] Port Open : ' + str(port))
        ports.append(port)

    except Exception:
        pass


scanned = 1
for port in range(1, ending_port + 1):
    thread = threading.Thread(target=scan, kwargs={'port': scanned})
    scanned += 1
    thread.start()

end_time = time()
total_ports = str(len(ports))

if '0' in total_ports:
    print(" All ports are closed.!")
else:
    print("\nTotal_Open_Ports   : ", total_ports)

for i in range(int(total_ports)):
    if total_ports == '100':
        ports.add('\n')
    else:
        pass

ports_list = str(ports)

current_time = datetime.now()

print("   Port Scanned     : ", scanned - 1)
print('List_Of_Open_Ports  :  ' + str(ports))
print(f"\n Scan in : {round(end_time - start_time,2)} sec")

f = open('port_scanned.txt', 'a')
f.write("-"*81)
f.write("\nDate : ")
f.write(str(current_time.day))
f.write("/")
f.write(str(current_time.month))
f.write("/")
f.write(str(current_time.year))
f.write("\nTarget : ")
f.write(target)
f.write("\nTotal_Open_Ports : ")
f.write(total_ports)
f.write("\nOpen_Ports : ")
f.write(ports_list)
f.write("\n")
f.write("-"*81)
f.write("\n")
f.write("\n")
f.close()
print("[###] ALL IMPORTANT DATA (along with search history) HAS SAVED IN 'port_scanned.txt' [###]\n")
