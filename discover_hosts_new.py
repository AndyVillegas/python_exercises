import concurrent.futures
import subprocess


ip_base = input("Input your IP: ")
partial_ip = ".".join(ip_base.split(".")[0:3])
discovered_hosts = []

def ping_to_ip(ip):
    completed_proccess = subprocess.run(['ping','-n','1','-w','3000',ip], stdout=subprocess.PIPE)
    if(completed_proccess.returncode == 0 and b"TTL" in completed_proccess.stdout):
        discovered_hosts.append(ip)

with concurrent.futures.ThreadPoolExecutor(max_workers=255) as executor:
    for i in range(1, 255):
        ip = partial_ip + "." + str(i)
        executor.submit(ping_to_ip, ip)
    executor.shutdown(wait=True)
    print(discovered_hosts)
