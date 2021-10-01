import paramiko
from os import system

arquivo = open('Arquivo de IPs.txt', 'w')
arquivo.write('')

ip = input('Digite o(s) IP(s):').split(' ')
with open ('Arquivo de IPs.txt', 'a') as AIP:
    for i in ip:
        AIP.write(f'{i}\n')

for qtd in ip:
    system('python3 SSH.py &')
