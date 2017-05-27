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
	import PIL
	img = PIL.Image.open(img_path)
	data = list(img.getdata())
	w, h = img.size
	P.print_bitmap(data, w, h, True )	

def Resize_Save(img_name, img_path=''):
	import PIL
	width = 328
	img = PIL.Image.open(img_path +img_name)
	w, h = img.size

	ratio = width / float(w)
	height = int( float(h) * float(ratio) )
	img_fit = img.resize((width, height), Image.ANTIALIAS)
	
	img_fit.save( img_path+'resized_'+img_name )


# E o File