import re
from tkinter import *
import Main

name = "Edit Configuration"

def load():
    with open("config.txt", "r") as txt:
        text = txt.read()
        pattern = r"Starttimes:\s\[\s*(?P<int1>\d+),\s*(?P<int2>\d+),\s*(?P<int3>\d+),\s*(?P<int4>\d+),\s*(?P<int5>\d+),\s*(?P<int6>\d+),\s*(?P<int7>\d+)\s*\]\s*Workperiods:\s*(?P<workperiods>\d+)\s*Breakperiods:\s*(?P<breakperiods>\d+)"
        match = re.match(pattern, text)
        if match:
            starttimes = []
            for i in range(1,8):
                starttimes.append(int(match.group(i)))
            workperiods = int(match.group(8))
            breakperiods = int(match.group(9))
            return workperiods, breakperiods, starttimes
        else:
            print("no match")

def save(starttimes, workperiods, breakperiods, root):
    starttimelist = []
    for x in starttimes:
        starttimelist.append(x.get())
    print(str(starttimes))
    with open("config.txt", "w") as txt:
        txt.write("Starttimes: " + str(starttimelist) + "\nWorkperiods: " + str(workperiods) + "\nBreakperiods: " + str(breakperiods))
    root.destroy()

def createApp(root):
    frame = Frame(root)
    frame.pack()
    workperiods, breakperiods, starttimes = load()
    workperiodsvar = IntVar(frame, workperiods)
    breakperiodsvar = IntVar(frame, breakperiods)
    Label(frame, text="How long is your ideal work periods?").grid(row=0, column=0)
    Label(frame, text="How long is your ideal break periods?").grid(row=0, column=1)
    Entry(frame, textvariable=workperiodsvar).grid(row=1, column=0)
    Entry(frame, textvariable=breakperiodsvar).grid(row=1, column=1)
    starttimevars = []
    for idx, i in enumerate(Main.WEEKDAYS):
        Label(frame, text="When does your day start on " + i + "?").grid(row=2, column=idx)
        var = IntVar(frame, starttimes[idx])
        Entry(frame, textvariable=var).grid(row=3, column=idx)
        starttimevars.append(var)
    root.protocol("WM_DELETE_WINDOW", lambda: save(starttimevars, workperiodsvar.get(), breakperiodsvar.get(), root))

if __name__ == "__main__":
    root = Tk()
    createApp(root)
    root.mainloop()