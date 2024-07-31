import datetime
import tkinter as tk
from tkinter import ttk
import pickle
import HomeworkAdder
import CommitmentsAdder
import AssignmentViewer
import ConfigEditor
import CalendarView
import tkscrolledframe

class Assignment():
    def __init__(self, startdate, enddate, workunits, difficulty, name, subject, time, bypass = False):
        if not bypass:
            self.startdate = startdate.get_date()
            self.enddate = enddate.get_date()
        else:
            self.startdate = startdate
            self.enddate = enddate
        self.assignmentsize = int(workunits.get())
        self.difficulty = int(difficulty.get())
        self.name = name.get()
        self.subject = subject.get()
        self.time = time.get()

class Commitment:
    def __init__ (self, startdate, enddate, starttime, duration, name, reason, days):
        self.startdate = startdate.get_date()
        self.enddate = enddate.get_date()
        self.starttime = int(starttime.get())
        self.duration = int(duration.get())
        self.name = name.get()
        self.reason = reason.get()
        self.days = []
        for i in days:
            self.days.append(i.get())

ScrollableFrame = tkscrolledframe.ScrolledFrame

    
COLORS = [
    "#FF0000",  # Red
    "#00FF00",  # Green
    "#0000FF",  # Blue
    "#FFFF00",  # Yellow
    "#FF00FF",  # Magenta
    "#00FFFF",  # Cyan
    "#FFA500",  # Orange
    "#800080",  # Purple
    "#00FF00",  # Lime
    "#FFC0CB",  # Pink
    "#A52A2A",  # Brown
    "#000080",  # Navy
    "#008080",  # Teal
    "#808000",  # Olive
    "#800000",  # Maroon
    "#D3D3D3",  # Light Gray
    "#A9A9A9",  # Dark Gray
    "#FFD700",  # Gold
    "#FF7F50",  # Coral
    "#40E0D0"   # Turquoise
]

WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def get_dates_between(date1_str, date2_str):
    # Convert string dates to datetime.date objects
    date1 = datetime.datetime.strptime(date1_str, "%m/%d/%y").date()
    date2 = datetime.datetime.strptime(date2_str, "%m/%d/%y").date()

    # Calculate the delta and generate the list of dates
    delta = date2 - date1
    all_dates = [date1 + datetime.timedelta(days=i) for i in range(delta.days + 1)]
    return all_dates

def openapp(app):
   top = tk.Toplevel(root)
   top.title(app.name)
   app.createApp(top) 

def remind():
    print("Hi")
    root.after(1, remind)

if __name__ == "__main__":
    root = tk.Tk()
    tk.Button(root, text="Add Homework", command=lambda:openapp(HomeworkAdder)).pack()
    tk.Button(root, text="Add Commitments", command=lambda:openapp(CommitmentsAdder)).pack()
    tk.Button(root, text="View Assignments and Commitments", command=lambda:openapp(AssignmentViewer)).pack()
    tk.Button(root, text="View Callendar", command=lambda:openapp(CalendarView)).pack()
    tk.Button(root, text="Edit Configuration", command=lambda:openapp(ConfigEditor)).pack()
    root.after(1, remind)
    root.mainloop()