#---

# Import py-thermal-printer library
# Py Thermal Printer : github.com/luopio/py-thermal-printer
import printer

serialport = printer.ThermalPrinter.SERIALPORT

try:
	Printer = printer.ThermalPrinter(serialport=serialport)
	print "Printer on : ", serialport
except:
	print "Printer not connected (to right serial port)"

def Text( text, Format=None, nl=True):

	if Format is None:
		Printer.print_text(text)
	else:
		Printer.print_markup(Format+" "+text)
	# default, add new line at the end
	if nl:
		Nl()


def Format(text):
	Printer.print_markup(text)
	# 1. char style
	#	 (n=normal, b=bold, u=underline, i=inverse, f=font B)
	# 2. char justification#
	#	 (l=left, c=centre, r=right)
	# 3. char ' ' space
	#

def Nl():
	Printer.print_text('\n')

def Line():
	Nl()
	Printer.print_text('_'*32)
	Nl()

printer_width = 384

def Image(img_path):
	import PIL
	img = PIL.Image.open(img_path)
	data = list(img.getdata())
	w, h = img.size
	Printer.print_bitmap(data, w, h, True )

# turns : data/img.png
# into	: data/rsz_img.png
def rename_img(img_path):
	slash = img_path.rfind('/')
	if slash is -1:
		# no folder path, only name
		return 'rsz_'+img_path
	else:
		# slash as position x
		return img_path[:slash+1]+'rsz_'+img_path[slash+1:]


def Resize_Test(img_path):
	from PIL import Image
	width = printer_width
	img = Image.open(img_path )
	w, h = img.size

	ratio = width / float(w)
	height = int( float(h) * float(ratio) )
	img_fit = img.resize((width, height), Image.ANTIALIAS)

	new_path = rename_img(img_path)
	img_fit.save( new_path )
	return new_path


def Resize_to(img_path, width):
	from PIL import Image

	img = Image.open(img_path )
	w, h = img.size

	ratio = width / float(w)
	height = int( float(h) * float(ratio) )
	img_fit = img.resize((width, height), Image.ANTIALIAS)

	new_path = rename_img(img_path)
	img_fit.save( new_path )
	return new_path

# E o File
