#!/usr/bin/python
import subprocess

DB = []
theFile = open("IPs_Found.txt","a")
for brier_creek in range(30,40): 
  address = "192.168.1." + str(brier_creek)
  res = subprocess.call(['ping', '-c', '3', address])
  if res == 0:
    print("ping to", address,"OK")
    DB.append(address) 
    theFile.write(address)  
  elif res == 2:
    print("no responce from", address)
  else:
    print("ping to", address, "failed!")
print("Table")
print("***************")
for result in range(0,len(DB)):
  print(DB[result])
theFile.close()
