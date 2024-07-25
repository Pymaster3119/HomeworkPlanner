from tkinter import *
from tkcalendar import Calendar
import datetime
import pickle
from tkinter import messagebox
import Main

root = Tk()

#Start Date
Label(root, text="Starting Date:").pack()
today = datetime.datetime.today()
startdate = Calendar(root, year = today.year, month = today.month, day = today.day, weekendforeground = "black", firstweekday = "monday", showothermonthdays = False)
startdate.pack(pady = 20)

#End Date
Label(root, text="Ending Date:").pack()
today = datetime.datetime.today()
enddate = Calendar(root, year = today.year, month = today.month, day = today.day, weekendforeground = "black", firstweekday = "monday", showothermonthdays = False)
enddate.pack(pady = 20)

#Name
Label(root, text='What is the name of your assignment?').pack()
name = StringVar()
Entry(root, textvariable=name).pack()

#Subject
Label(root, text='What is the subject of your assignment?').pack()
subject = StringVar()
Entry(root, textvariable=subject).pack()

#Work Units
Label(root, text='How many "units" of work is there?:').pack()
workunits = StringVar()
Entry(root, textvariable=workunits).pack()

#Difficulty
Label(root, text='On a scale of 1-10, how difficult is the assignment?:').pack()
difficulty = StringVar()
Entry(root, textvariable=difficulty).pack()

#Create Assignment
def saveAssignments():
    assignmentlist = []
    with open("assignmentslist", "rb") as listfile:
        assignmentlist = pickle.load(listfile)
    assignmentlist.append(Main.Assignment(startdate, enddate, workunits, difficulty, name, subject))
    with open("assignmentslist", "wb") as listfile:
        pickle.dump(assignmentlist, listfile)
    messagebox.showinfo(message="Assignment posted!")


Button(root, text="Save Assignment", command=saveAssignments).pack()

root.mainloop()
