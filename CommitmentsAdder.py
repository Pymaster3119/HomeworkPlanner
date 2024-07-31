from tkinter import *
from tkcalendar import Calendar
import datetime
import pickle
from tkinter import messagebox
import Main

name = "Add Commitments"

#Create Commitment
def saveCommitments():
    commitmentlist = []  
    with open("commitmentslist", "rb") as listfile:
        commitmentlist = pickle.load(listfile)
    commitmentlist.append(Main.Commitment(startdate, enddate, starttime, duration, name, reason, weekdayvars))
    with open("commitmentslist", "wb") as listfile:
        pickle.dump(commitmentlist, listfile)
    messagebox.showinfo(message="Commitment posted!")


def createApp(root):
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
    Label(root, text='What is the name of your commitment?').pack()
    name = StringVar()
    Entry(root, textvariable=name).pack()

    #Reason
    Label(root, text='What is the club/reason you are commiting for?').pack()
    reason = StringVar()
    Entry(root, textvariable=reason).pack()

    #Starttime
    Label(root, text='When does it start?:').pack()
    starttime = StringVar()
    Entry(root, textvariable=starttime).pack()

    #Length
    Label(root, text='How long is it?:').pack()
    duration = StringVar()
    Entry(root, textvariable=duration).pack()

    #Dates
    Label(root, text='What days of the week will this be?:').pack()
    tempframe = Frame(root)
    tempframe.pack()
    weekdayvars = []
    for idx, weekday in enumerate(Main.WEEKDAYS):
        variable = BooleanVar(tempframe, False)
        weekdayvars.append(variable)
        Checkbutton(tempframe, text=weekday, variable=variable).grid(row=0, column=idx)
    Button(root, text="Save Commitment", command=saveCommitments).pack()


if __name__ == "__main__":
    root = Tk()
    createApp(root)
    root.mainloop()
