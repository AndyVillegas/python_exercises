import threading
import subprocess

def ping_to_ip(ip):
    completed_proccess = subprocess.run(['ping','-n','1','-w','3000',ip], stdout=subprocess.PIPE)
    if(completed_proccess.returncode == 0 and b"TTL" in completed_proccess.stdout):
        discovered_hosts.append(ip)

ip_base = input("Input your IP: ")
partial_ip = ".".join(ip_base.split(".")[0:3])
threads = []
discovered_hosts = []
for i in range(1, 255):
    ip = partial_ip + "." + str(i)
    thread = threading.Thread(target=ping_to_ip, args=(ip,))
    thread.start()
    threads.append(thread)
 
for thread in threads:
    thread.join()
    if(thread is threads[-1]):
        print(discovered_hosts)
