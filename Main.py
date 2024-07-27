import datetime
import tkinter as tk
from tkinter import ttk

class Assignment():
    def __init__(self, startdate, enddate, workunits, difficulty, name, subject):
        self.startdate = startdate.get_date()
        self.enddate = enddate.get_date()
        self.assignmentsize = int(workunits.get())
        self.difficulty = int(difficulty.get())
        self.name = name.get()
        self.subject = subject.get()

# HELP HELP HELP HELP HELP HELP HELP HELP HELP HELP HELP HELP HELP HELP HELP HELP HELP HELP HELP HELP HELP HELP HELP HELP HELP HELP HELP HELP HELP HELP HELP HELP 
class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        
        canvas = tk.Canvas(self)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )
        
        self.canvas_window = canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Ensure the scrollable frame expands to fill the canvas width
        self.scrollable_frame.bind("<Configure>", self.on_frame_configure)

    def on_frame_configure(self, event):
        # Update the canvas width to match the width of the scrollable frame
        canvas_width = event.width
        self.canvas.itemconfig(self.canvas_window, width=canvas_width)
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

def get_dates_between(date1_str, date2_str):
    # Convert string dates to datetime.date objects
    date1 = datetime.datetime.strptime(date1_str, "%m/%d/%y").date()
    date2 = datetime.datetime.strptime(date2_str, "%m/%d/%y").date()

    # Calculate the delta and generate the list of dates
    delta = date2 - date1
    all_dates = [date1 + datetime.timedelta(days=i) for i in range(delta.days + 1)]
    return all_dates
