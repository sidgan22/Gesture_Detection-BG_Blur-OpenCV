import tkinter as tk
import os

def quit():
    global root
    root.quit()

def videoOpen():
    os.system('python video.py')
    print("Opening video program.")

def gestRecog():
    os.system('python recogGest.py')
    print("Opening gesture program.")

root = tk.Tk()
root.geometry("300x70")
root.title('MISHMASH')
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, 
                   
                   text="QUIT", 
                   fg="red",
                   bg="grey",
                   command=quit)
button.pack(side=tk.LEFT)
b1 = tk.Button(frame,
                   bg="grey",
                   text="VideoFilter",
                   command=videoOpen)
b1.pack(side=tk.LEFT)
b2 = tk.Button(frame,
                   bg="grey",
                   text="GestureRecogniser",
                   command=gestRecog)
b2.pack(side=tk.LEFT)

root.mainloop()