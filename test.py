# coding: utf-8
#
import tkinter
import time
#
file_ = open("timer.txt", "w")
#
def close():
    file_.close()
    root.destroy()
#
def allert():
    tpl = tkinter.Toplevel()
    text = tkinter.Label(tpl, text="Timer Allert!", bg="red")
    text.pack()
#
def set_data_to_file(event):
    file_.write(timer["text"] + "\n")
    timer.after(10000, allert)
#
def go_timer():
    timer["text"] = "{3:02d}:{4:02d}:{5:02d}".format(*time.localtime())
    timer.after(1000, go_timer)
#
root = tkinter.Tk()
root.focus_force()
root.protocol("WM_DELETE_WINDOW", close)
#
timer = tkinter.Label(root, font="Arial, 40")
timer.pack()
timer.after(0, go_timer)
button = tkinter.Button(root, text="Save to file")
button.pack()
button.bind("<Button-1>", set_data_to_file)
#
root.mainloop()