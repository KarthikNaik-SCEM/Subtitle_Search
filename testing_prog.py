from tkinter import *
from tkinter import ttk
import os, glob
from tkinter import messagebox
import Jellies
import re
import srt


root= Tk()
root.geometry("60x40")

def printf():
	global index 
	index= list_box.curselection()
	vid_name= list_box.get(index)
	os.startfile(vid_name)
	
def exit():
	sec_window.destroy()

def Search():
	global index

	if word_insert.get() in Jellies.new_lst:
		#print("yes")

		key = word_insert.get()
		file_1 = open('Test.srt','r')
		file_2 = open('standard_vid_sub.srt','r')
		file_3 = open('SPEECH RASHMIKA MANDANNA Dream BIG.srt','r')
		file_list=[file_1,file_2,file_3]
		index= list_box.curselection()
		f = file_list[index[0]-1].read()	
		subs = list(srt.parse(f))
		#print(subs)
		final_window = Tk()
		final_window.title("the subtitle time stamps")

		for sub in subs:
			if key in sub.content:
				
				Label(final_window, text= "from "+str(sub.start) + " to "+ str(sub.end) +" - "+ sub.content).pack()
				#print(sub.start, sub.end, sub.content)
			
		#print("hello")
			#if key in subs
		#print(subs[0].content)
		#print(subs[0].start)
		# for line in file.readlines():
		#     # if re.search(r'^%s'%key, line, re.I):
		#     if key in line:

		#         print(line)
	else:
		 err_label= Label(sub_window, text= "unfortunatly " + word_insert.get() +" does not exist")
		 err_label.grid(row=2,column=0)

	#sub_window.destroy()

def open_sW():
	global word_insert
	global sub_window
	sub_window= Tk()
	label_prompt=Label(sub_window, text="enter the word:")
	word_insert= Entry(sub_window, width=30)
	search_button= Button(sub_window,text="search", width=20, command= Search)


	label_prompt.grid(row=0, column=0)
	word_insert.grid(row=0,column=1)
	search_button.grid(row=1, column=0, columnspan=2)

def open_another():
	response= messagebox.askyesno("prompt", "want to search for a word from the subtitle?" )
	if response==1:
		open_sW()
	if response==0:
		printf()

def open_video():

	global list_box
	global sec_window
	sec_window= Tk()
	sec_window.title("videos")
	sec_window.geometry("180x250")
	list_box= Listbox(sec_window)
	videos_list= glob.glob("*mp4")

	for video in videos_list:
		list_box.insert(END, video)

	select_b= Button(sec_window, text="select", command=open_another)
	cancel_b=Button(sec_window,text="cancel", command= exit)

	

	list_box.grid(row=0, column=0, columnspan=1,padx=30, pady=10)
	select_b.grid(row=1, column=0)
	cancel_b.grid(row=2, column=0)

b_1= Button(root, text= "click here for video list", command= open_video)

def start_video():
	pass

b_1.pack()
root.mainloop()