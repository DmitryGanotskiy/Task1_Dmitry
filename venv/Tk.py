from tkinter import *
from Uni import Uni
from Student import Student

#basic setup 
class Tkinter:
    def __init__(self):
        self.currentHeight = 70
        self.entries = []
        self.marks =[]
        self.students = []
        self.uni = Uni(self)
        self._SetUp()
        self._CreateElements()

#create main form
    def _SetUp(self):
        self.tk = Tk()
        self.tk.configure(bg="gray")
        self.tk.geometry("800x500")
        self.tk.minsize(800, 500)
        self.tk.maxsize(800, 500)
        self.tk.title("Grades")

#create elements
    def _CreateElements(self):
        Canvas(self.tk, height = 470, width = 250, bg="black").place(x=10, y=60)
        Canvas(self.tk, height=40, width=400, bg="black").place(x=340, y=60)

        Label(text="Enter your subjects and grades", fg="black", bg="gray", width="25", height="1").pack()
        Label(text="Courses:").place(x=30, y=70)
        Button(self.tk, text="+", width="5", bg="gray", command=self._AddEntry).place(x=30, y=100)
        Button(self.tk, text="send", width="5", bg="gray", command=self._Dict).place(x=30, y=150)
        Button(self.tk, text="Average", width="5", bg="gray", command=self.uni.Average).place(x=350, y=70)
        Button(self.tk, text="Table", width="5", bg="gray", command=self.uni.Table).place(x=460, y=70)
        Button(self.tk, text="Edit", width="5", bg="gray", command=self.uni.Edit).place(x=580, y=70)
        Button(self.tk, text="Delete", width="5", bg="gray", command=self.uni.Delete).place(x=680, y=70)

#add text forms and scroll bars fpr user to input their data
    def _AddEntry(self):
        if len(self.marks) <= 4 and len(self.entries) <= 4 and len(self.students)<=4:
            course = Entry(self.tk, width=20, fg='black', font=('Arial', 10))
            course.place(x=100, y=self.currentHeight)
            mark = Scale(self.tk, bg="gray", variable=DoubleVar(), from_=1, to=50, orient=HORIZONTAL)
            mark.place(x=100, y=self.currentHeight+20)
            self.currentHeight += 80
            self.marks.append(mark)
            self.entries.append(course)
        else: pass

#put all the collected data to the Students list
    def _Dict(self):
        for i in range(len(self.entries)):
               if self.entries[i] != "":
                   self.students.append(Student(self.entries[i].get(), self.marks[i].get()))

        for i in self.entries:
            i.destroy()
        for i in self.marks:
            i.destroy()

        self.entries.clear()
        self.marks.clear()

        self.currentHeight = 70

#runs the program
    def run(self):
        self.tk.mainloop()