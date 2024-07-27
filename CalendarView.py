from tkinter import *
from tkcalendar import Calendar
import datetime
import pickle
from tkinter import messagebox
import Main
import re
import calendar
import math
root = Tk()

# Clean up the assignments
datepattern = r'(\d{1,2})/(\d{2})/(\d{2})'
today = datetime.datetime.today()

assignmentlist = []
with open("assignmentslist", "rb") as listfile:
    assignmentlist = pickle.load(listfile)
    for assignment in assignmentlist[:]: 
        match = re.match(datepattern, assignment.enddate)
        if match:
            month = int(match.group(1))
            day = int(match.group(2))
            year = int(match.group(3)) + 2000 
            if datetime.datetime(year, month, day) < today:
                assignmentlist.remove(assignment)

with open("assignmentslist", "wb") as listfile:
    pickle.dump(assignmentlist, listfile)

#Create colors for each class
colors = {}
colorindex = 0
for assignment in assignmentlist:
    if not assignment.subject in colors.keys():
        colors[assignment.subject] = Main.COLORS[colorindex]
        colorindex += 1

print(colors)

#Create the callendar basic UI
class callendarObject():
    def __init__(self, parent, date):
        self.frame = Frame(parent)
        self.date = date
        weekday = date.weekday()
        firstweekday, firstdayofmonth = calendar.monthrange(date.year, date.month)
        self.frame.grid(row = math.floor((date.day + firstweekday - 1) / 7) + 1, column = weekday)
        self.canvas = Canvas(self.frame, width=60, height=60)
        self.canvas.grid(row=0, column=1)
        self.classes = []
        Label(self.frame, text=self.date.date().day).grid(row=0, column=0)

    def add(self, assignment):
        self.canvas.create_rectangle(0, len(self.classes) * 10, 60, len(self.classes) * 10 + 5, fill = colors[assignment.subject])
callendarFrame = Frame(root)
callendarFrame.pack()
def createcallendar(year, month):
    global callendarFrame
    for child in callendarFrame.winfo_children():
        child.destroy()
    date = datetime.datetime(year, month, 1)
    temp, numdays = calendar.monthrange(date.year, date.month)
    for i in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]:
        Label(callendarFrame, text=i).grid(row=0, column=["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"].index(i))
    for i in range(numdays):
        date = datetime.datetime(date.year, date.month, i + 1)
        callendarObject(callendarFrame, date)

#Add assignments
for assignment in assignmentlist:
    print(assignment.startdate)
    print(type(assignment.startdate))
    for date in Main.get_dates_between(assignment.startdate, assignment.enddate):
        print(date)

#Create the callendar date selection framework
createcallendar(today.year, today.month)
year = StringVar(value=str(today.year))
month = StringVar(value=str(today.month))
Entry(root, textvariable=year).pack()
Entry(root, textvariable=month).pack()
year.trace_add('write',lambda a, b, c: createcallendar(int(year.get()), int(month.get())))
month.trace_add('write',lambda a, b, c: createcallendar(int(year.get()), int(month.get())))
root.mainloop()
