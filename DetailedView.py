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
import math

import tkinter as tk
from tkinter import ttk
from datetime import datetime

def detailedview(top, widget):
    frame = ttk.Frame(top)
    frame.pack(fill="both", expand=True)
    
    #Create header
    tk.Label(frame, text=widget.date.date()).grid(row=0, column=0, sticky="ew")
    tk.Label(frame, text="Assignments:").grid(row=1, column=0, sticky="ew")
    
    #Create assignments
    assignmentframes = Main.ScrollableFrame(frame)
    assignmentframes.grid(row=2, column=0, sticky="nsew")
    assignmentframes.scrollable_frame.grid_rowconfigure(0, weight=1)
    assignmentframes.scrollable_frame.grid_columnconfigure(0, weight=1)
    for idx, assignment in enumerate(widget.assignments):
        tempframe = ttk.Frame(assignmentframes.scrollable_frame)
        tempframe.grid(row=idx, column=0, padx=10, pady=5, sticky="ew")
        tk.Label(tempframe, text="Name: " + assignment.name).grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        tk.Label(tempframe, text="Class: " + assignment.subject).grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        tk.Label(tempframe, text="Difficulty: " + str(assignment.difficulty)).grid(row=0, column=2, padx=5, pady=5, sticky="ew")
        tk.Label(tempframe, text="Size: " + str(assignment.assignmentsize)).grid(row=0, column=3, padx=5, pady=5, sticky="ew")
        for col in range(4):
            tempframe.grid_columnconfigure(col, weight=1)

    #Create Commitments
    tk.Label(frame, text="Commitments:").grid(row=3, column=0, sticky="ew")
    commitmentframes = Main.ScrollableFrame(frame)
    commitmentframes.grid(row=4, column=0, sticky="nsew")
    commitmentframes.scrollable_frame.grid_rowconfigure(0, weight=1)
    commitmentframes.scrollable_frame.grid_columnconfigure(0, weight=1)
    for idx, commitment in enumerate(widget.commitments):
        tempframe = ttk.Frame(commitmentframes.scrollable_frame)
        tempframe.grid(row=idx, column=0, padx=10, pady=5, sticky="ew")
        tk.Label(tempframe, text="Name: " + commitment.name).grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        tk.Label(tempframe, text="Reason: " + commitment.reason).grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        tk.Label(tempframe, text="Starttime: " + str(commitment.starttime)).grid(row=0, column=2, padx=5, pady=5, sticky="ew")
        tk.Label(tempframe, text="Duration: " + str(commitment.duration)).grid(row=0, column=3, padx=5, pady=5, sticky="ew")
        for col in range(4):
            tempframe.grid_columnconfigure(col, weight=1)

    

    #Display schedule
    tk.Label(frame, text="Schedule:").grid (row=5,column=0)
    scheduleframes = Main.ScrollableFrame(frame)
    scheduleframes.grid(row=6, column=0, sticky="nsew")
    scheduleframes.scrollable_frame.grid_rowconfigure(0, weight=1)
    scheduleframes.scrollable_frame.grid_columnconfigure(0, weight=1)
    currenttime = 180
    timeline = createSchedule(widget.assignments, widget.commitments)
    for idx,i in enumerate(timeline):
        tempframe = ttk.Frame(scheduleframes.scrollable_frame)
        tempframe.grid(row=idx, column=0, padx = 10, pady=5, sticky="ew")
        tk.Label(tempframe,text=str(math.floor(currenttime/60)) + ":" + str(currenttime % 60)).grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        currenttime += i[1]
        tk.Label(tempframe,text=str(math.floor(currenttime/60)) + ":" + str(currenttime % 60)).grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        if isinstance(i[0], str):
            tk.Label(tempframe,text=i[0]).grid(row=0, column=2, padx=5, pady=5, sticky="ew")
        elif isinstance(i[0], Main.Assignment):
            tk.Label(tempframe,text=i[0].name).grid(row=0, column=2, padx=5, pady=5, sticky="ew")
            tk.Label(tempframe,text=i[0].difficulty).grid(row=0, column=3, padx=5, pady=5, sticky="ew")
        elif isinstance(i[0], Main.Commitment):
            tk.Label(tempframe,text=i[0].name).grid(row=0, column=2, padx=5, pady=5, sticky="ew")
            tk.Label(tempframe,text=i[0].reason).grid(row=0, column=3, padx=5, pady=5, sticky="ew")
            tk.Label(tempframe,text=i[0].duration).grid(row=0, column=4, padx=5, pady=5, sticky="ew")
        
def createSchedule(assignments, commitments, breaktime = 15, workperiods = 30):
    #Create schedule
    timeline = []
    totaltime = 0
    #Working from hardest to easiest so that workload becomes easier as time goes on
    sorted_assignments = sorted(assignments, key=lambda x: x.difficulty, reverse=True)
    for assignment in sorted_assignments:
        numdays = datetime.strptime(assignment.enddate, "%m/%d/%y").date() - datetime.strptime(assignment.startdate, "%m/%d/%y").date()
        numdays = numdays.days
        timeonassignment = 0
        while timeonassignment < math.ceil(int(assignment.time)/numdays):
            interruptingCommitment = None
            for commitment in commitments:
                print(commitment.starttime)
                if totaltime >= int(commitment.starttime) and totaltime <= int(commitment.starttime) + int(commitment.duration):
                    interruptingCommitment = commitment
            
            if interruptingCommitment != None:
                if not totaltime - interruptingCommitment.starttime == 0:
                    timeline.append((assignment, totaltime - interruptingCommitment.starttime))
                timeline.append((interruptingCommitment, interruptingCommitment.duration))
                timeline.append((assignment, workperiods - (totaltime - interruptingCommitment.starttime)))
                timeonassignment += workperiods
                totaltime += workperiods + interruptingCommitment.duration
            else:
                timeline.append((assignment, workperiods))
                timeline.append(("break", breaktime))
                timeonassignment += workperiods
                totaltime += workperiods