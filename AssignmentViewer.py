from tkinter import *
from tkcalendar import Calendar
import datetime
import pickle
from tkinter import messagebox
import Main

name = "View Assignments and Commitments"


class AssignmentWidget():
    def __init__(self, assignment, idx, mainframe, root):
        self.tempframe = Frame(mainframe.scrollable_frame)
        self.tempframe.grid(row=idx, column=0, padx = 10, pady=5, sticky="ew")
        self.namevar = StringVar(root, assignment.name)
        self.startdatevar = StringVar(root, assignment.startdate)
        self.enddatevar = StringVar(root, assignment.enddate)
        self.subjectvar = StringVar(root, assignment.subject)
        self.difficultyvar = IntVar(root, assignment.difficulty)
        self.workvar = IntVar(root, assignment.assignmentsize)
        self.timevar = IntVar(root, assignment.time)
        Entry(self.tempframe,textvariable=self.namevar).grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        Entry(self.tempframe,textvariable=self.subjectvar).grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        Entry(self.tempframe,textvariable=self.startdatevar).grid(row=0, column=2, padx=5, pady=5, sticky="ew")
        Entry(self.tempframe,textvariable=self.enddatevar).grid(row=0, column=3, padx=5, pady=5, sticky="ew")
        Entry(self.tempframe,textvariable=self.difficultyvar).grid(row=0, column=4, padx=5, pady=5, sticky="ew")
        Entry(self.tempframe,textvariable=self.timevar).grid(row=0, column=5, padx=5, pady=5, sticky="ew")
        Entry(self.tempframe,textvariable=self.workvar).grid(row=0, column=6, padx=5, pady=5, sticky="ew")
        Button(self.tempframe, text = "x", command=lambda:deleteAssignment(self)).grid(row=0, column=7, padx=5, pady=5, sticky="ew")
    def compress(self):
        return Main.Assignment(self.startdatevar.get(), self.enddatevar.get(), self.workvar, self.difficultyvar, self.namevar, self.subjectvar, self.timevar, bypass=True)
    
class CommitmentWidget():
    def __init__(self, commitment, idx, mainframe, root):
        self.tempframe = Frame(mainframe.scrollable_frame)
        self.tempframe.grid(row=idx, column=0, padx = 10, pady=5, sticky="ew")
        self.namevar = StringVar(root, commitment.name)
        self.startdatevar = StringVar(root, commitment.startdate)
        self.enddatevar = StringVar(root, commitment.enddate)
        self.subjectvar = StringVar(root, commitment.reason)
        self.difficultyvar = IntVar(root, commitment.starttime)
        self.workvar = IntVar(root, commitment.duration)
        Entry(self.tempframe,textvariable=self.namevar).grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        Entry(self.tempframe,textvariable=self.subjectvar).grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        Entry(self.tempframe,textvariable=self.startdatevar).grid(row=0, column=2, padx=5, pady=5, sticky="ew")
        Entry(self.tempframe,textvariable=self.enddatevar).grid(row=0, column=3, padx=5, pady=5, sticky="ew")
        Entry(self.tempframe,textvariable=self.difficultyvar).grid(row=0, column=4, padx=5, pady=5, sticky="ew")
        Entry(self.tempframe,textvariable=self.workvar).grid(row=0, column=6, padx=5, pady=5, sticky="ew")
        Button(self.tempframe, text = "x", command=lambda:deleteCommitment(self)).grid(row=0, column=7, padx=5, pady=5, sticky="ew")
    def compress(self):
        return Main.Assignment(self.startdatevar.get(), self.enddatevar.get(), self.workvar, self.difficultyvar, self.namevar, self.subjectvar, self.timevar, bypass=True)

assignments = []
commitments = []

def deleteAssignment(assignment):
    assignments.remove(assignment)
    assignment.tempframe.destroy()
def deleteCommitment(commitment):
    commitments.remove(commitment)
    commitment.tempframe.destroy()

def save(root):
    assignmentlist= []
    for assignment in assignments:
        assignmentlist.append(assignment.compress())
    with open("assignmentslist", "wb") as listfile:
        pickle.dump(assignmentlist, listfile)

    commitmentlist= []
    for commitment in commitments:
        commitmentlist.append(commitment.compress())
    with open("commitmentslist", "wb") as listfile:
        pickle.dump(commitmentlist, listfile)
    root.destroy()

def createApp(root):
    assignmentlist = []
    with open("assignmentslist", "rb") as listfile:
        assignmentlist = pickle.load(listfile)

    mainframe = Main.ScrollableFrame(root)
    mainframe.grid(row=1, column=0, sticky="nsew")
    mainframe.scrollable_frame.grid_rowconfigure(0, weight=1)
    mainframe.scrollable_frame.grid_columnconfigure(0, weight=1)
    
    for idx,i in enumerate(assignmentlist):
        assignments.append(AssignmentWidget(i, idx, mainframe, root))
    
    commitmentlist = []
    with open("commitmentslist", "rb") as listfile:
        commitmentlist = pickle.load(listfile)

    mainframe = Main.ScrollableFrame(root)
    mainframe.grid(row=3, column=0, sticky="nsew")
    mainframe.scrollable_frame.grid_rowconfigure(0, weight=1)
    mainframe.scrollable_frame.grid_columnconfigure(0, weight=1)
    
    for idx,i in enumerate(commitmentlist):
        commitments.append(CommitmentWidget(i, idx, mainframe, root))


    root.protocol("WM_DELETE_WINDOW", lambda:save(root))

if __name__ == "__main__":
    root = Tk()
    createApp(root)
    root.mainloop()