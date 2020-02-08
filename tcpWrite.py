#!/usr/bin/env python
# -*- coding: utf_8 -*-

import modbus_tk.defines as cst
from modbus_tk import modbus_tcp

def main():
	master = modbus_tcp.TcpMaster(host = '192.168.0.211', port = 502)
	master.set_timeout(5.0)
	master.set_verbose(True)
	print('=> ',master)
	li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	r = master.execute( 1, cst.WRITE_MULTIPLE_REGISTERS, starting_address = 0, output_value = li )

if __name__ == "__main__":
	main()



