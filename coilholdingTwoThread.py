# -*- coding: utf_8 -*-
import re
import sys
import time
import serial
import threading
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu

def hold(slaveId, reg, startAdd, length):
	global master
	r = master.execute(slaveId, reg, startAdd, length)
	data = str(list(r))

	if reg == 1:
		print('1=>',time.ctime() + data)
		f.write('Coils => ' +time.ctime() + "=>" + data)
		f.write("\n")	
	elif reg ==3:
		print('2=>',time.ctime() + data)
		f.write('Holding => ' +time.ctime() + "=>" + data)
		f.write("\n")	
		

global master
master = modbus_rtu.RtuMaster(serial.Serial(port='/dev/ttyUSB0',bytesize=8,parity='N',baudrate=9600))
master.set_timeout(5)
master.set_verbose(True)

slaveId = int(input('Enter slave Id : ')) 
reg = int(input('Enter reg Type : ')) 
startAdd = int(input('Enter Starting address : ')) 
length = int(input('Enter length : '))

slaveId2 = int(input('Enter slave Id : ')) 
reg2 = int(input('Enter reg Type : ')) 
startAdd2 = int(input('Enter Starting address : ')) 
length2 = int(input('Enter length : '))
filename = "Log " +time.ctime()
filename = re.sub('[^1234567890 ]+', '',filename)
filename = filename.replace(" ","")
f = open(filename + ".txt",'w', encoding = 'utf-8')
f.write("Time: "+time.ctime() + "\n")
final = 0

while True:
	if final<=100:
		thread1 = threading.Thread(target = hold, args=(slaveId, reg, startAdd, length,))
		thread2 = threading.Thread(target = hold, args=(slaveId2, reg2, startAdd2, length2,))
	
		thread1.start()		
		time.sleep(5)
		thread2.start()
		time.sleep(3)		
		thread1.join() 
		thread2.join()

		final += 2
	else:
		f.close()
		print('script stop')
		break














