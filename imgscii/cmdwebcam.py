import tkinter
from imgscii import printscii
from VideoCapture import Device

cam = Device()
frame = tkinter.Tk()
frame.geometry('800x800')
display = tkinter.Label(frame, text='')
input('Begin display?')

while True:
    try:
        image = cam.getImage()
        printscii(image, display)
        del image
       
    except KeyboardInterrupt:
        del cam
        break
