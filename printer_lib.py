#---

import printer

serialport = printer.ThermalPrinter.SERIALPORT

print "Printer on : ", serialport
P = printer.ThermalPrinter(serialport=serialport)


def Text(text, nl=True):
	P.print_text(text)
	# default, add new line at the end 
	if nl:
		Nl()

def Format(text):
	P.print_markup(text)
	# 1. char style
	# 2. char justification#
	# 3. char ' ' space

def Nl():
	P.print_text('\n')

def Line():
	Nl()
	P.print_text('_'*32)
	Nl()

def Image(img_path):
	from PIL import Image
	img = Image.open(img_path)
	data = list(img.getdata())
	w, h = img.size
	P.print_bitmap(data, w, h )	



# E o File