import random
import sys
import os
import time
import paramiko

paramiko.util.log_to_file('ssh.log') # sets up logging

ssh = paramiko.SSHClient() #create object for ssh

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('10.89.234.6', port=22,username="cisco", password="Tpslab03") ## ip address, port 22 is SSH, try telnet, username, password

remote_conn = ssh.invoke_shell()
output = remote_conn.recv(65535)
print(output)

remote_conn.send('cisco\n')
time.sleep(2)
remote_conn.send('Tpslab03\n')
time.sleep(2)

remote_conn.send('transfer download mode ftp\n')
time.sleep(2)
remote_conn.send('transfer download datatype code\n')
time.sleep(2)
remote_conn.send('transfer download serverip 100.64.61.6\n')
time.sleep(2)
remote_conn.send('transfer download filename AIR-CT5500-K9-8-3-102-0.aes\n')
time.sleep(2)
remote_conn.send('transfer download path FTP/code/83\n')
time.sleep(2)
remote_conn.send('transfer download username ftpuser\n')
time.sleep(2)
remote_conn.send('transfer download password ftp123\n')
time.sleep(2)
remote_conn.send('transfer download start\n')
time.sleep(2)
remote_conn.send('y')
time.sleep(120)
remote_conn.send('save config\n')
time.sleep(5)
remote_conn.send('y')
time.sleep(5)
remote_conn.send('reset system\n')
time.sleep(5)
remote_conn.send('y')
time.sleep(5)
output = remote_conn.recv(65535)
print output




#transfer download mode ftp
#transfer download datatype code
#transfer download serverip 100.64.62.6
#transfer download filename AIR-CT5500-K9-8-0-140-0.aes
#transfer download path FTP/code/80/
#transfer download username ftpuser
#transfer download password ftp123
#transfer download start
#y
#save config
#y , no enter
#reset system
#y, no enter
#end

#above is 8.0, we also need to do 8.3
