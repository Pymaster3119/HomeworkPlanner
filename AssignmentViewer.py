from tkinter import *
from tkcalendar import Calendar
import datetime
import pickle
from tkinter import messagebox
import Main

root = Tk()

assignmentlist = []
with open("assignmentslist", "rb") as listfile:
    assignmentlist = pickle.load(listfile)

mainframe = Main.ScrollableFrame(root)
mainframe.grid(row=6, column=0, sticky="nsew")
mainframe.scrollable_frame.grid_rowconfigure(0, weight=1)
mainframe.scrollable_frame.grid_columnconfigure(0, weight=1)
for idx,i in enumerate(assignmentlist):
    tempframe = Frame(mainframe.scrollable_frame)
    

root.mainloop()