#You can import tkinter library (Use capital letter for python 2.7):

import Tkinter as tk

#Now create a new command button called "toggle" in order to create the effect of "toggle" when you press playing on the relief property (sunken or raised) :

def toggle():

    if toggle_btn.config('relief')[-1] == 'sunken':
        toggle_btn.config(relief="raised", text="Off")
    else:
        toggle_btn.config(relief="sunken", text="On")
        
root = tk.Tk()
#At the end apply this behaviour on your button:
toggle_btn = tk.Button(text="Off", width=12, relief="raised", command=toggle)
toggle_btn.pack(pady=5)

root.mainloop()
