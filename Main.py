class Assignment():
    def __init__(self, startdate, enddate, workunits, difficulty, name, subject):
        self.startdate = startdate.get_date()
        self.enddate = enddate.get_date()
        self.assignmentsize = int(workunits.get())
        self.difficulty = int(difficulty.get())
        self.name = name.get()
        self.subject = subject.get()