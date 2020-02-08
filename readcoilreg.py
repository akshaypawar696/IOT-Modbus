#!/usr/bin/env python
# -*- coding: utf_8 -*-

import serial
import modbus_tk.defines as cst
from modbus_tk import modbus_tcp

def main():
	master = modbus_tcp.TcpMaster(host = '192.168.0.202', port = 502)
	master.set_timeout(5.0)
	master.set_verbose(True)
	#r = master.execute(1, cst.READ_COIL_REGISTERS, 0, 10)
	r = master.execute(1, 3, 0, 10)
	print(r)

if __name__ == "__main__":
	main()



