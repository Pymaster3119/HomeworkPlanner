from tkinter import *
from tkcalendar import Calendar
import datetime
import pickle
from tkinter import messagebox
import Main
import re
import calendar
import math
import DetailedView

name = "View Callendar"

# Clean up the assignments
datepattern = r'(\d{1,2})/(\d{2})/(\d{2})'
today = datetime.datetime.today()

def load():
    assignmentlist = []
    commitmentlist = []
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

    with open("commitmentslist", "rb") as listfile:
        commitmentlist = pickle.load(listfile)
        for commitment in commitmentlist[:]: 
            match = re.match(datepattern, commitment.enddate)
            if match:
                month = int(match.group(1))
                day = int(match.group(2))
                year = int(match.group(3)) + 2000 
                if datetime.datetime(year, month, day) < today:
                    commitmentlist.remove(commitment)
            if isinstance(commitment, Main.Assignment):
                commitmentlist.remove(commitment)

    with open("commitmentslist", "wb") as listfile:
        pickle.dump(commitmentlist, listfile)
    return assignmentlist, commitmentlist

#Create the callendar basic UI object
class callendarObject():
    def __init__(self, parent, date, colors,root):
        self.frame = Frame(parent)
        self.date = date
        weekday = date.weekday()
        firstweekday, firstdayofmonth = calendar.monthrange(date.year, date.month)
        self.frame.grid(row = math.floor((date.day + firstweekday - 1) / 7) + 1, column = weekday)
        self.assignmentcanvas = Canvas(self.frame, width=60, height=60)
        self.assignmentcanvas.grid(row=1, column=0)
        self.commitmentcanvas = Canvas(self.frame, width=60, height=60)
        self.commitmentcanvas.grid(row=2, column=0)
        self.assignments = []
        self.commitments = []
        Label(self.frame, text=self.date.date().day).grid(row=0, column=0)
        Button(self.frame, text = "View", command= self.detailedview).grid(row=2, column=0)
        self.colors = colors
        self.root = root

    def addassignment(self, assignment):
        self.assignmentcanvas.create_rectangle(0, len(self.assignments) * 10, 60, len(self.assignments) * 10 + 5, fill = self.colors[assignment.subject])
        self.assignments.append(assignment)

    def addcommitment(self, commitment):
        print("Here")
        self.commitmentcanvas.create_rectangle(0, len(self.commitments) * 10, 60, len(self.commitments) * 10 + 5, fill = self.colors[commitment.reason])
        self.commitments.append(commitment)
    def detailedview(self):
        top = Toplevel(self.root)
        top.title("Detailed View")
        DetailedView.detailedview(top, self)

def createcallendar(year, month, callendarFrame, callendarobjects, assignmentlist, commitmentlist, colors, root):
        for child in callendarFrame.winfo_children():
            child.destroy()
        date = datetime.datetime(year, month, 1)
        temp, numdays = calendar.monthrange(date.year, date.month)
        for i in Main.WEEKDAYS:
            Label(callendarFrame, text=i).grid(row=0, column=Main.WEEKDAYS.index(i))
        for i in range(numdays):
            date = datetime.datetime(date.year, date.month, i + 1)
            callendarobjects.append(callendarObject(callendarFrame, date, colors, root))

        #Add assignments
        for assignment in assignmentlist:
            for date in Main.get_dates_between(assignment.startdate, assignment.enddate):
                if date.year == year and date.month == month:
                    callendarobjects[date.day - 1].addassignment(assignment)
        #Add commitments
        for commitment in commitmentlist:
            for date in Main.get_dates_between(commitment.startdate, commitment.enddate):
                if date.year == year and date.month == month and commitment.days[date.weekday()]:
                    callendarobjects[date.day - 1].addcommitment(commitment)

def createApp(root):
    #Create colors for each class
    assignmentlist, commitmentlist = load()
    colors = {}
    colorindex = 0
    for assignment in assignmentlist:
        if not assignment.subject in colors.keys():
            colors[assignment.subject] = Main.COLORS[colorindex]
            colorindex += 1

    for commitment in commitmentlist:
        if not commitment.reason in colors.keys():
            colors[commitment.reason] = Main.COLORS[colorindex]
            colorindex += 1

    print(colors)


    #Create the callendar objects
    callendarFrame = Frame(root)
    callendarFrame.pack()
    callendarobjects = []
                

    #Create the callendar date selection framework
    createcallendar(today.year, today.month, callendarFrame, callendarobjects, assignmentlist, commitmentlist, colors, root)
    year = StringVar(value=str(today.year))
    month = StringVar(value=str(today.month))
    Entry(root, textvariable=year).pack()
    Entry(root, textvariable=month).pack()
    year.trace_add('write',lambda a, b, c: createcallendar(int(year.get()), int(month.get()), callendarFrame, callendarobjects, assignmentlist, commitmentlist, colors, root))
    month.trace_add('write',lambda a, b, c: createcallendar(int(year.get()), int(month.get()), callendarFrame, callendarobjects, assignmentlist, commitmentlist, colors, root))

if __name__ == "__main__":
    root = Tk()
    createApp(root)
    root.mainloop()
