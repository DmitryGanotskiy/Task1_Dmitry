from tkinter import *
from tkPDFViewer import tkPDFViewer as pdf 

class Uni:
    def __init__(self, tk):
        self.root = tk
        self.courses = []
        self.marks = []

    def Table(self):
        self.canvasTable = Canvas(self.root.tk, height=300, width=400, bg="black")
        self.canvasTable.place(x=340, y=100)

        header = ["Id", "Subject", "Mark"]
        colWidth = 150

        self.canvasTable.create_text(200, 10, text="Grades", fill="white")

        for col, text in enumerate(header):
            self.canvasTable.create_text(colWidth * col + colWidth // 2, 30, text=text, fill="white")

        for i, student in enumerate(self.root.students):
            self.canvasTable.create_text(75, 30 * (i + 2), text=str(i+1), fill="white")
            self.canvasTable.create_text(220, 30 * (i + 2), text=student.course, fill="white")
            self.canvasTable.create_text(370, 30 * (i + 2), text=str(student.mark), fill="white")

    def Average(self):
        self.canvasMark = Canvas(self.root.tk, height=300, width=400, bg="black")
        self.canvasMark.place(x=340, y=100)
        if self.root.students and len(self.root.students) >= 2:
            marks = [student.mark for student in self.root.students]
            average_mark = abs(sum(marks) / len(marks))
            self.canvasMark.create_text(200, 150, text=f"Average Mark: {average_mark}", fill="white")
        else: self.canvasMark.create_text(200, 150, text="Minimum two students", fill="white")

    def _EditStudents(self):
        for i in range(len(self.courses)):
            if self.courses[i] != "":
                self.root.students[i].Update(str(self.courses[i].get()), int(self.marks[i].get()))
        if self.frame:
            self.frame.destroy()
            self.frame = None
            self.courses.clear()
            self.marks.clear()

    def Edit(self):
        self.frame = Frame(self.root.tk)
        self.frame.place(x=340, y=100)

        for row, student in enumerate(self.root.students):
            courseEntry = Entry(self.frame, width=15, fg='black', font=('Arial', 12))
            courseEntry.grid(row=row, column=0, padx=(10, 5), pady=10, ipady=3)
            courseEntry.insert(END, student.course)
            self.courses.append(courseEntry)

            markEntry = Entry(self.frame, width=15, fg='black', font=('Arial', 12))
            markEntry.grid(row=row, column=1, padx=(5, 10), pady=10, ipady=3)
            markEntry.insert(END, str(student.mark))
            self.marks.append(markEntry)

        Button(self.root.tk, text="Edit", width="5", bg="gray", command=self._EditStudents).place(x=340, y=400)

    def Docs(self):
        pass