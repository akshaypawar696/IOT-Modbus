# -*- coding: utf_8 -*-

import sys
from modbus_tk import modbus_rtu
import serial
import modbus_tk.defines as cst


def main():
	print('inside main')
	master = modbus_rtu.RtuMaster(serial.Serial(port='/dev/ttyUSB0',bytesize=8,parity='N',baudrate=9600))
	master.set_timeout(5)
	master.set_verbose(True)	
	r = master.execute(1, cst.HOLDING_REGISTERS, 0, 10)	
	print(r)
	one = r[0]
	print('#############')
	print(one)
	print(type(one))

if __name__ == "__main__":
	main()
