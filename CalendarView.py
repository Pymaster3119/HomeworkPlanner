from tkinter import *
from tkcalendar import Calendar
import datetime
import pickle
from tkinter import messagebox
import Main
import re

root = Tk()

#Clean up the assignments
datepattern = r"\b(1[0-2]|[1-9])/([1-9]|[12][0-9]|3[01])/\d{2}\b"
today = datetime.datetime.today()
with open("assignmentslist", "rb") as listfile:
    assignmentlist = pickle.load(listfile)
    for assignment in assignmentlist:
        match = re.match(datepattern, assignment.enddate)
        if datetime.datetime(int("20" + match.group(3)), int(match.group(2)), int(match.group(1))) < today.date():
            assignmentlist.remove(assignment)


#TODO: Create my own callendar to display this

root.mainloop()
