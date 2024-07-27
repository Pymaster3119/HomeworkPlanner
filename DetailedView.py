import tkinter as tk
from tkcalendar import Calendar
import datetime
import pickle
from tkinter import messagebox
import re
import calendar
import math
import Main
from tkinter import ttk

def detailedview(top, widget):
    frame = ttk.Frame(top)
    frame.pack(fill="both", expand=True)
    
    #Create header
    tk.Label(frame, text=widget.date.date()).grid(row=0, column=0)
    tk.Label(frame, text="Assignments:").grid(row=1, column=0)
    
    #Place all assignments
    assignmentframes = Main.ScrollableFrame(frame)
    assignmentframes.grid(row=2, column=0, sticky="nsew")
    for assignment in widget.assignments:
        tempframe = ttk.Frame(assignmentframes.scrollable_frame)
        tempframe.pack(fill="x", expand=True)
        tk.Label(tempframe, text="Name: " + assignment.name).grid(row=0, column=0)
        tk.Label(tempframe, text="Class: " + assignment.subject).grid(row=0, column=1)
        tk.Label(tempframe, text="Difficulty: " + str(assignment.difficulty)).grid(row=0, column=2)
        tk.Label(tempframe, text="Size: " + str(assignment.assignmentsize)).grid(row=0, column=3)

    #Figure out schedule
    
    