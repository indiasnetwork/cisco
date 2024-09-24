import paramiko
import time
import os


def Device(ip):
     try:
          ssh = paramiko.SSHClient()
          ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
          ssh.connect(ip,port='22',username='YourUser',password='YourPass')
          conn = ssh.invoke_shell()
          output = conn.recv(6655000000)
          time.sleep(2)
          conn.send("terminal length 0\n")
          conn.send("sh runn\n")
          time.sleep(5)
          conn.send("sh ip int brief\n")
	      time.sleep(2)
          conn.send("sh vtp status\n")
          time.sleep(3)
          conn.send("sh flash\n")
          time.sleep(2)
          conn.send("sh ver\n")
          time.sleep(2)
          conn.send("sh boot\n")
          time.sleep(2)
          conn.send("wr\n")
          time.sleep(2)
          time.sleep(2)
          if conn.recv_ready():
               output = conn.recv(6555555500)
          print(output)


	      os.chdir("C:\\Users\\RGolla\\Documents\\backup\\")
          f = open(ip+".txt", 'a')
          f.write(output)
          f.close()             

     except paramiko.AuthenticationException:
           print(ip+" password wrong")      


Device("172.20.20.10")

