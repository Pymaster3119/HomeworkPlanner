from tkinter import *
from tkcalendar import Calendar
import datetime
import pickle
from tkinter import messagebox
import re
import calendar
import math
import Main

def detailedview(top, widget):
    frame = Frame(top)
    frame.pack()
    Label(frame, text=widget.date.date()).grid(row=0, column=0, columnspan=100)
    Label(frame, text="Assignments:").grid(row=1, column=0, columnspan=100)
    assignmentframes = Main.ScrollableFrame(frame)
    assignmentframes.grid (row = 2, column=0, sticky="w")
    for assignment in widget.assignments:
        tempframe = Frame(assignmentframes)
        tempframe.pack(anchor = "w")
        Label(tempframe, text="Name:" + assignment.name).grid(row=0, column=0)
        Label(tempframe, text="Class:" + assignment.subject).grid(row=0, column=1)
        Label(tempframe, text="Difficulty:" + str(assignment.difficulty)).grid(row=0, column=2)
        Label(tempframe, text="Size:" + str(assignment.assignmentsize)).grid(row=0, column=3)

    