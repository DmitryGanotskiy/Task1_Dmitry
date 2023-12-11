from tkinter import *
from Uni import Uni
from Student import Student

class Tkinter:
    def __init__(self):
        self.currentHeight = 70
        self.entries = []
        self.marks =[]
        self.students = []
        self.uni = Uni(self)
        self.SetUp()
        self.CreateElements()

    def SetUp(self):
        self.tk = Tk()
        self.tk.geometry("800x500")
        self.tk.minsize(800, 500)
        self.tk.maxsize(800, 500)
        self.tk.title("Grades")

    def CreateElements(self):
        Canvas(self.tk, height = 470, width = 250, bg="black").place(x=10, y=60)
        Canvas(self.tk, height=40, width=400, bg="black").place(x=340, y=60)

        Label(text="Enter your subjects and grades", fg="black", bg="gray", width="25", height="1").pack()
        Label(text="Courses:").place(x=30, y=70)
        Button(self.tk, text="+", width="5", bg="gray", command=self.AddEntry).place(x=30, y=100)
        Button(self.tk, text="send", width="5", bg="gray", command=self._Dict).place(x=30, y=150)
        Button(self.tk, text="Average", width="5", bg="gray", command=self.uni.Average).place(x=350, y=70)
        Button(self.tk, text="Table", width="5", bg="gray", command=self.uni.Table).place(x=460, y=70)
        Button(self.tk, text="Edit", width="5", bg="gray", command=self.uni.Edit).place(x=580, y=70)
        Button(self.tk, text="Docs", width="5", bg="gray", command=self.uni.Docs).place(x=680, y=70)

    def AddEntry(self):
        course = Entry(self.tk, width=20, fg='black', font=('Arial', 10))
        course.place(x=100, y=self.currentHeight)
        mark = Scale(self.tk, bg="gray", variable=DoubleVar(), from_=1, to=50, orient=HORIZONTAL)
        mark.place(x=100, y=self.currentHeight+20)
        self.currentHeight += 80
        self.marks.append(mark)
        self.entries.append(course)

    def _Dict(self):
        for i in range(len(self.entries)):
               if self.entries[i] != "":
                   self.students.append(Student(self.entries[i].get(), self.marks[i].get()))

    def run(self):
        self.tk.mainloop()