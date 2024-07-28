import re
from tkinter import *
import Main

with open("config.txt", "r") as txt:
    text = txt.read()
    pattern = r"Starttimes:\s\[\s*(?P<int1>\d+),\s*(?P<int2>\d+),\s*(?P<int3>\d+),\s*(?P<int4>\d+),\s*(?P<int5>\d+),\s*(?P<int6>\d+),\s*(?P<int7>\d+)\s*\]\s*Workperiods:\s*(?P<workperiods>\d+)\s*Breakperiods:\s*(?P<breakperiods>\d+)"
    match = re.match(pattern, text)
    if match:
        starttimes = []
        for i in range(1,8):
            starttimes.append(int(match.group(i)))
        workperiods = match.group(8)
        breakperiods = match.group(9)
    else:
        print("no match")

root = Tk()
frame = Frame(root)
frame.pack()
workperiodsvar = IntVar(frame, workperiods)
breakperiodsvar = IntVar(frame, breakperiods)
Label(frame, text="How long is your ideal work periods?").grid(row=0, column=0)
Label(frame, text="How long is your ideal break periods?").grid(row=0, column=1)
Entry(frame, textvariable=workperiodsvar).grid(row=1, column=0)
Entry(frame, textvariable=breakperiodsvar).grid(row=1, column=1)
for idx, i in enumerate(Main.WEEKDAYS):
    Label(frame, text="When does your day start on " + i + "?").grid(row=2, column=idx)
    var = IntVar(frame, starttimes[idx])
    Entry(frame, textvariable=var).grid(row=3, column=idx)

def save():
    print(str(starttimes))
    with open("config.txt", "w") as txt:
        txt.write("Starttimes: " + str(starttimes) + "\nWorkperiods: " + workperiods + "\nBreakperiods: " + breakperiods)
    root.destroy()
root.protocol("WM_DELETE_WINDOW", save)
root.mainloop()