import datetime
import tkinter as tk

class Assignment():
    def __init__(self, startdate, enddate, workunits, difficulty, name, subject):
        self.startdate = startdate.get_date()
        self.enddate = enddate.get_date()
        self.assignmentsize = int(workunits.get())
        self.difficulty = int(difficulty.get())
        self.name = name.get()
        self.subject = subject.get()

class ScrollableFrame(tk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        
        canvas = tk.Canvas(self)
        scrollbar = tk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = tk.Frame(canvas)
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )
        
        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="w")
        
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

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
