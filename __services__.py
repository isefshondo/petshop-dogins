from tkinter import *

servicesInterface = Tk()

# Main Configuration
taskBarHeight = 40

servicesInterface.resizable(False, False)

width_screen = servicesInterface.winfo_screenwidth()
height_screen = servicesInterface.winfo_screenheight() - taskBarHeight
width = int((width_screen * 87) / 100)
height = int((height_screen * 70) / 100)
posx = (width_screen / 2) - (width / 2)
posy = (height_screen / 2) - (height / 2)

servicesInterface.maxsize(width, height)
servicesInterface.minsize(width, height)

servicesInterface.geometry("%dx%d+%d+%d" % (width, height, posx, posy))

servicesInterface.mainloop()