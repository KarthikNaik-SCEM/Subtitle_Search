from tkinter import *
import os, glob

sec_window= Tk()
list_box= Listbox(sec_window)
videos_list= glob.glob("*mp4")

for video in videos_list:
	list_box.insert(END, video)
def pressed():
	print(list_box.curselection())
	
select_b= Button(sec_window, text="select", command= pressed)
cancel_b=Button(sec_window,text="cancel")



list_box.pack()
select_b.pack()
cancel_b.pack()
videos_list= glob.glob("*mp4")


sec_window.mainloop()