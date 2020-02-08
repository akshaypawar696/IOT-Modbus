# -*- coding: utf_8 -*-

import sys
from modbus_tk import modbus_rtu
import serial
import modbus_tk.defines as cst


def main():
	master = modbus_rtu.RtuMaster(serial.Serial(port='/dev/ttyUSB0',bytesize=8,parity='N',baudrate=9600))
	master.set_timeout(5)
	master.set_verbose(True)	
	li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, starting_address=0, output_value=li)
if __name__ == "__main__":
	main()
