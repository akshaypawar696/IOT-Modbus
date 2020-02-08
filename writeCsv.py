
# -*- coding: utf_8 -*-
import re
import sys
import csv
import time
import serial
import threading
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu

def hold(slaveId, reg, startAdd, length):
	global master
	data = master.execute(slaveId, reg, startAdd, length)

	newli = [time.ctime()]
	for i in range(length - startAdd):
		newli.append(data[i])
	writer.writerow(newli)
	print('newli',newli)


global master
master = modbus_rtu.RtuMaster(serial.Serial(port='/dev/ttyUSB1',bytesize=8,parity='N',baudrate=9600))
master.set_timeout(5)
master.set_verbose(True)

slaveId = int(input('Enter slave Id : ')) 
reg = int(input('Enter reg Type : ')) 
startAdd = int(input('Enter Starting address : ')) 
length = int(input('Enter length : '))

filename = time.ctime()
filename = re.sub('[^1234567890 ]+', '',filename)
filename = filename.replace(" ","")

f = open(filename + ".csv", 'w', encoding = 'utf-8')
writer = csv.writer(f)

li = ['Time']
for i in range(startAdd, length):
	li.append('holding'+str(i))

writer.writerow(li)
final = 0

while True:
	if final<20:
		thread1 = threading.Thread(target = hold, args=(slaveId, reg, startAdd, length,))
		thread1.start()
		thread1.join() 
		time.sleep(2)
		final += 2
	else:
		f.close()
		print('script stop')
		break


































