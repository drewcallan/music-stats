from Tkinter import *
import tkMessageBox, Tkconstants, tkFileDialog

def callback():
	print "Call from Callback"
def about():
	print "About the Program"
def team():
	print "Team Members"
def version():
	print "Current Version: 1.0.1"

def info(title, text):
	tkMessageBox.showinfo(title, text)

class App:
	def __init__(self, master):
		frame = Frame(master, width=600, height=400)
		frame.pack(padx=10)
		
		photo = PhotoImage(file="\project\images\logo.gif")
		lPhoto = Label(frame, image=photo)
		lPhoto.image=photo
		lPhoto.pack(side=TOP)

		
		#Label(master, text="Directory: ").grid(row=0)
		tText       = Label (frame, text="\n Music Stat App!\n").pack(side=TOP)
		self.new    = Button(frame, text="New", padx=35, pady=2, command=self.new).pack(side=LEFT)
		self.hello  = Button(frame, text="Hello", padx=30, pady=2, command=self.hi).pack(side=LEFT)
		self.askdir = Button(frame, text="Select Directory", padx=10, pady=2, command=self.askdir).pack(side=LEFT)
		self.button = Button(frame, text="Quit", padx=30, pady=2, fg="red", bg="PeachPuff", command=frame.quit).pack(side=LEFT)
		bText       = Label (frame, text="\n\n").pack(side=BOTTOM)
		
		#self.warn = Button(frame, text="Warn", command=warning("Sample", "Sample Warning"))
		#self.warn.pack(side=LEFT)
		
		self.dir_opt = options = {}
		options['initialdir'] = 'C:\\'
		options['mustexist'] = False
		options['parent'] = root
		options['title'] = 'Select your music folder'
		
	def new(self):
		top = Toplevel()
		top.title("Popup")
		top.button = Button(top, text="Exit", command=top.destroy)
		top.button.pack()
		
	def hi(self):
		print "Hello, World"

	def askdir(self):
		"""Returns a selected directoryname."""
		dirName = tkFileDialog.askdirectory(**self.dir_opt)
		print dirName
		return dirName
		
root = Tk()

app = App(root)

menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=callback)
filemenu.add_command(label="Open...", command=callback)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=about)
helpmenu.add_command(label="Team...", command=team)
helpmenu.add_command(label="Version...", command=version)

root.mainloop()