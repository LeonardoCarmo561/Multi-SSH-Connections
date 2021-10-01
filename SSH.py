import paramiko

with open ('Arquivo de IPs.txt','r') as AIP:
    txt = AIP.readlines()
    print(txt)
    IP = txt[0]
    txt.remove(IP)
    IP = str(IP.replace('\n',''))


a = str()


with open ('Arquivo de IPs.txt', 'w') as AIP:
    for linha in txt:
        a = f'{a}{linha}'
    AIP.write(f'{a}')


ssh = paramiko.SSHClient()
username = 'root'
password = 'PrintRJ45'
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=IP, username=username, password=password)
with open ('script.txt', 'r') as script:
    for code in script.readlines():
        stdin, stdout, stderr = ssh.exec_command(f'{code}')
        stdin.close()
        for line in stdout.readlines():
            print(line.replace('\n',''))

