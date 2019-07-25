#import tkinter


#import tkinter
#import _tkinter     # import binaries

from tkinter import *
# themed widget modules
from tkinter import ttk

def TK_test():
    # ( import tkinter )
    tkinter._test()

def TK_hello():
    # ( import * )
    root = Tk()
    Label(root, text="Hello TKinter!").pack()
    root.mainloop()

def TK_widgets():
    root = Tk()
    # arguments : ( parent, additional param for configur. )
    button = ttk.Button(root, text='Click Me' )
    # Not visible yet, needs to know where to put it.
    button.pack()   # pack to place in window
    
    print( button['text'] )     # use [] to access
    button['text'] = 'Press Me'     # use [] to SET to change later

    button.config(text ='Push Me')  # alternate use config , 
    print( button.config() )        #uses dict to find all vars
    print(str(button))     # actual TK names for widgets
    print(str(root))        

    # PACK IN SAME LINE
    ttk.Label(root, text='Hello, TKinter!').pack()  # NOT storing the reference to label in variable. might not need a label anymore...
    
    root.mainloop()


#                                   **  Functions

# 1 - Test
# TK_test()

# 2 - Hello World
# TK_hello()

# 3 - Widgets
# TK_widgets()

# 4 - 2 buttons

# 5 Lesson window



class HelloApp:
    # two buttons that change label text
    def __init__(self, master):
        #- Label
        self.label = ttk.Label(master, text = "Hello, Tkinter!")
        self.label.grid(row = 0, column = 0, columnspan = 2)
        
        #-Buttons
        ttk.Button(master, text = "Texas",
                   command = self.texas_hello).grid(row = 1, column = 0)

        ttk.Button(master, text = "Hawaii",
                   command = self.hawaii_hello).grid(row = 1, column = 1)
        
        #-Text
        self.quote = ttk.Label(master, text = "Test")
        self.quote.grid(row=2, column=0, columnspan=2)

        self.quote['text']="Howdy DawwwwG dont ssweat mannn its allg ood in the hood wlets do what i do thwen di do whrn im doing"
        self.quote.config(wraplength = 80)
        self.quote.config(justify = CENTER)      # RIGHT LEFT
        self.quote.config(foreground='white', background='blue')
        self.quote.config(font = ('Courier', 14, 'bold') )       # 1. 'fontname' 2. fontsize, 3. [other]

        #-Photo
        self.ring = PhotoImage(file='C:\\Users\\thomas.britnell\\Pictures\\ring.gif')       #ring.gif')    #print.png') 
        #ring = PhotoImage(file='C:\\Users\\thomas.britnell\\Pictures\\print.png') 
        #quote.config(image= ring)
        self.quote.img = self.ring
        self.tiny = self.ring.subsample(2,2)

        self.quote.config(image = self.quote.img)
        self.quote.config(compound='text')
        self.quote.config(compound='center') #top bottom left right center
        #gif, png, ppm , e.g. use PIL

        #-Next button
        #TK.BUtton() gives original normal button, ttk is themed like windows
        self.next = ttk.Button(master, text='Just do it')
        self.next.grid(row=3, column=0, columnspan=2)
        self.next.config(command=self.next_func)
        #next.invoke()   # simmulates a button click
        
        #-Checkbutton
        self.check = ttk.Checkbutton(master, text='Hobbitses...')
        self.check.grid(row=4, column=0, columnspan=1)
        self.check2 = ttk.Checkbutton(master, text='Gharstly!')
        self.check2.grid(row=4, column=1, columnspan=1)
        self.check.config(command=self.check_func)  # attach func

        #-Variables
        # allows events for changes to Variables    # types : BooleanVar DoubleVar IntVar StringVar
        self.spam=StringVar()
        self.spam.set('facebook')
        #print( "spam is : ", self.spam.get() )
        self.check.config(variable=self.spam, onvalue='Bilbo', offvalue='Gollumn')
        
        #-Radiobuttons
        self.radio = StringVar()
        ttk.Radiobutton(master, variable=self.radio, text='BBC', value='BBC').grid(row=5, column=0)
        ttk.Radiobutton(master, variable=self.radio, text='Energy',value='Energy').grid(row=5, column=1)
        ttk.Radiobutton(master, variable=self.radio, text='Bayern3',value='Bayern3').grid(row=6, column=0)
        ttk.Radiobutton(master, variable=self.radio, text='FM4',value='FM4').grid(row=6, column=1)

        ttk.Label(master, text="Station:").grid(row=7, column=0)
        self.station = ttk.Label(master, textvariable=self.radio)
        self.station.grid(row=7, column=1)

        #-signle line
        self.entry = ttk.Entry(master,width=30) # size in characters
        self.entry.grid(row=8,column=0, columnspan=2)
        self.entry.insert(0, 'Enter your password')
        #self.entry.config(show='*')

        # no entry change function - later we can bind
        self.delB = ttk.Button(master, text="Delete" )
        self.delB.grid(row=9,column=0)
        self.delB.config(command=self.del_func)

        self.comB = ttk.Button(master, text="Bäm" )
        self.comB.grid(row=9,column=1)
        self.comB.config(command=self.com_func)

        #-combo box (number box)
        self.month = StringVar()
        self.combobox = ttk.Combobox(master, textvariable=self.month)
        self.combobox.config(values=('yi', 'er', 'san', 'si', 'wu', 'qi', 'ba', 'jiu', 'shi'))
        self.combobox.grid(row=10, column=1)
        ttk.Label(master, text="Ji sui?").grid(row=10,column=0)
        self.month.set('Choose age')
        #-spinbox
        #Spinbox is NOT in ttk themed, only standard
        self.year = StringVar()
        Spinbox(master, from_=2018, to=2022, textvariable=self.year).grid(row=11,column=1)
        #print(self.year.get(), self.month.get() )

        #-prograss Bars
        self.progS = 0
        self.progress = ttk.Progressbar(master, orient=HORIZONTAL, length=100)  # length in pixel
        # determinate or indeterminate
        self.progress.config(mode='indeterminate', maximum=32.0, value=2)
        self.progress.start()   # starts cycling back and forth
        #self.progress.stop()
        self.progress.grid(row=12, column=0)
        ttk.Button(master, command=self.prog_func, text='switch').grid(row=12,column=1)
        
        #-scale bar
        self.ping = DoubleVar()
        self.pong = ttk.Progressbar(master, orient=HORIZONTAL, length = 80)
        self.pong.config(variable=self.ping, mode='determinate', maximum=99.0, value=0)
        #self.pong.start()
        self.pong.grid(row=13, column=0, columnspan=2)
        self.paddle = ttk.Scale(master, orient=HORIZONTAL, length=250, variable=self.ping, from_=0.0, to=99.0)
        self.paddle.grid(row=14, column=0, columnspan=2)


    def texas_hello(self):
        self.label.config(text = 'Howdy, Tkinter!')
        self.quote.config(image=self.ring, compound=CENTER)
        if self.next.instate(['disabled']):
            self.next.state(['!disabled'])    
            print("Reenabled")


    def hawaii_hello(self):
        self.label.config(text = 'Aloha, Tkinter!')
        #self.next.img = self.tiny
        self.quote.config(image=self.tiny, compound=LEFT)
        

    def next_func(self):
        print('#NEXT!!')
        self.next.state(['disabled'])    
        print("button disabled: ", self.next.instate(['disabled']) ) 

    def check_func(self):
        print( "hobbit is : ", self.spam.get() )

    def del_func(self):
        #print(self.entry.get())
        #self.entry.delete(0,1)  # del furst
        self.entry.delete(0,END)  # del all
        #self.entry.delete()

    def com_func(self):
        entered = self.entry.get()  # get
        #self.entry.state(['disabled'])
        self.entry.state(['readonly'])
        self.entry.config(show='#')

    def prog_func(self):
        # self.progress.stop()
        if  self.progS==0:
            self.progress.config(mode='determinate')
            # self.progress.start()
            self.progS = 1
        else:
            self.progress.config(mode='indeterminate')
            self.progress.step(16.0)
            self.progS = 0

        #self.progress.config(value=28.0)
        #self.progress.step()
        #self.progress.step(6.0)

"""
root = Tk()
app = HelloApp(root)
root.mainloop()
"""



class FrameApp:
    # two buttons that change label text
    def __init__(self, master):
        window = TopLevel(master)
        # Frame 1
        self.frame = ttk.Frame(master)
        self.frame.pack()
        #self.frame.config(height=200, width=600)
        self.frame.config(relief=RAISED)        # FLAT      RAISED & SUNKEN    SOLID    RIDGE    GROOVE
        ttk.Button(self.frame, text='B1').grid()
        self.frame.config(padding=(20,12))   #(x,y)     # with padding frame loses W & H
        # Frame 2 label
        self.labF = ttk.LabelFrame(master,text='Configuration')    # PACKING into master    ( height=100,width=200, )
        self.labF.config(padding=(8,8))
        self.labF.pack()
        ttk.Button(self.labF, text='RESET').grid()

"""
# 6 Framed interface
fruit = Tk()
app2 = FrameApp(fruit)
fruit.mainloop()
"""


class WindowApp:
    def __init__(self, master):
        self.window = Toplevel(master)      # when created, default is 200x200
        self.window.title('Extra window')
        #-order
        self.window.lower()     # extra window behind
        #self.window.lift(master)    # lift above (other_window)
        #-hide
        #self.window.state('zoomed')     #extra window maximise
        #self.window.state('withdrawn')  # hide window. NO TASKBAR either
        #self.window.state('iconic') # hide but STILL IN TASKBAR
        #self.window.state('normal')      # 
        self.window.iconify()       # minimize
        self.window.deiconify()     # bring back
        #-size
        self.window.geometry('640x480+1900+10')
        #self.window.resizable(False, False) # resize (x,y)
        self.window.resizable(True, True) # resize (x,y)
        self.window.maxsize( 800,800)       # maximum (w,h)
        #self.window.destroy()   # only closes window
        master.destroy()        # destroys both since window is child

"""
                        **    run Code

"""

"""
root = Tk()
app3 = WindowApp(root)
root.mainloop()
"""

class PainApp:
    def __init__(self, master):
        self.paned = ttk.Panedwindow(master, orient=HORIZONTAL)   # VERTICAL   # HORIZONTAL
        self.paned.pack( fill=BOTH, expand=True)    # fill= expand W and H

        self.frame1 = ttk.Frame(self.paned, width=100, height=300, relief=SUNKEN)
        self.frame2 = ttk.Frame(self.paned, width=100, height=500, relief=SUNKEN)
        self.paned.add(self.frame1, weight=1)    # weight = scale when resizing
        self.paned.add(self.frame2, weight=4)

        self.frame3 = ttk.Frame(self.paned, width=50, height=50, relief=SUNKEN)
        self.paned.insert(1, self.frame3)       # weight = 0 means it doesnt increase
        self.paned.forget(0)        # does not destroy, still exists

"""
root = Tk()
app4 = PainApp(root)
root.mainloop()
"""

class TabApp:
    def __init__(self,master):
        notebook = ttk.Notebook(master)
        notebook.pack()
        frame1 = ttk.Frame(notebook)
        frame2 = ttk.Frame(notebook)
        notebook.add(frame1, text='Work')
        notebook.add(frame2, text='Play')
        #Butt
        ttk.Button(frame1, text='Clicker').pack()
        frame1.config(padding=(20,20))
        frame3 = ttk.Frame(notebook)
        notebook.insert(1,frame3, text='Pokemon')
        notebook.forget(1)  # NOT deleted
        notebook.add(frame3, text= 'N64')
        print("selected: ",notebook.index(notebook.select()) )  # gives ID -> convert to _int
        notebook.select(2)      # change active / shown tab
        #notebook.tab(1,state='disabled')    
        notebook.tab(2,state='hidden')
        notebook.tab(2,state='normal')
        print( notebook.tab(1,'text'))  # returns title

"""
root=Tk()
app5 = TabApp(root)
root.mainloop()
"""

class TextApp:
    def __init__(self,master):
        text = ttk.Text(master, width=400, height=400)
        text.pack()
        text.config(wrap = 'word')  # char none word
        # BASE modifier modifier
        # line.char = 4.2 (starting 1.0)
        #--Indices
        #linestart lineend
        # wordstart wordend
        
        whole = text.get('1.0','end')   #returns entire content
        first_line = text.get('1.0', '1.end')

        text.insert('1.0 + 2 lines', 'Inserted message')
        text.insert('1.0 + 2 lines lineend', '\n...MORE\n more\n more')

        # delete first char first line
        text.delete('1.0')  
        # delete first line, LEAVE NEW LINE
        text.delete('1.0', '1.0 lineend')       
        # delete line + NewLine
        text.delete('1.0', '3.0 lineend + 1 chars') 
        # REPLACE first line
        text.replace('1.0', '1.0 lineend', 'This is the first line.') 




root = Tk()
app6 = TextApp(root)
root.mainloop()



class Fest:
    def __init__(self, x):
        a = x
        print(a)
    def plus(self):
        a += a
        print(a)

#-- EoF