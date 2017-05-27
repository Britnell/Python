#---

import printer

serialport = printer.ThermalPrinter.SERIALPORT

print "Printer on : ", serialport
P = printer.ThermalPrinter(serialport=serialport)


def Text(text):
	P.print_text(text)

def Format(text):
	P.print_markup(text)
	# 1. char style
	# 2. char justification#
	# 3. char ' ' space

def Nl():
	P.print_text('\n')

