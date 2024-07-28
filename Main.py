import datetime
import tkinter as tk
from tkinter import ttk
import pickle

class Assignment():
    def __init__(self, startdate, enddate, workunits, difficulty, name, subject, time):
        self.startdate = startdate.get_date()
        self.enddate = enddate.get_date()
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

class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        
        self.canvas = tk.Canvas(self)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )
        
        self.canvas_window = self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        self.canvas.configure(yscrollcommand=scrollbar.set)
        
        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.scrollable_frame.bind("<Configure>", self._on_frame_configure)
        self.canvas.bind('<Configure>', self._on_canvas_configure)

    def _on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        self.canvas.itemconfig(self.canvas_window, width=self.scrollable_frame.winfo_reqwidth())

    def _on_canvas_configure(self, event):
        if self.scrollable_frame.winfo_reqwidth() != self.canvas.winfo_width():
            self.canvas.itemconfig(self.canvas_window, width=self.canvas.winfo_width())
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

if __name__ == "__main__":
    assignmentlist = []
    listname = input("What list do you want to remove?: ")
    with open(listname, "wb") as listfile:
        pickle.dump(assignmentlist, listfile)