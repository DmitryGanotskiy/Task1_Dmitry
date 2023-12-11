from tkinter import *

class Uni:
    def __init__(self, tk):
        self.tk = tk
    def Table(self):
        pass
    def Average(self):
        pass

class Student:
    def __init__(self, name, value):
        self.course = str(name)
        self.mark = int(value)

class Tkinter:
    def __init__(self):
        self.SetUp()
        self.CreateElements()
        self.currentHeight = 70
        self.entries = []
        self.marks =[]
        self.students = []

    def SetUp(self):
        self.tk = Tk()
        self.tk.geometry("800x500")
        self.tk.title("Grades")

    def CreateElements(self):
        Label(text="Enter your subjects and grades", fg="black", bg="gray", width="25", height="1").pack()
        Label(text="Courses:").place(x=15, y=70)
        Button(self.tk, text="+", width="5", bg="gray", command=self.AddEntry).place(x=15, y=100)
        Button(self.tk, text="send", width="5", bg="gray", command=self.Dict).place(x=15, y=150)

    def AddEntry(self):
        course = Entry(self.tk, width=20, fg='black', font=('Arial', 10))
        course.place(x=100, y=self.currentHeight)
        mark = Scale(self.tk, bg="gray", variable=DoubleVar(), from_=1, to=50, orient=HORIZONTAL)
        mark.place(x=100, y=self.currentHeight+20)
        self.currentHeight += 80
        self.marks.append(mark)
        self.entries.append(course)

    def Dict(self):
        for i in range(len(self.entries)):
               self.students.append(Student(self.entries[i].get(), self.marks[i].get()))



tk = Tkinter()
tk.tk.mainloop()
uni = Uni(tk)


"""
        for i in range(3):
            for j in range(5):
                self.entry = Entry(tk, width=20, fg='black',
                                       font=('Arial', 16))
                self.entry.grid(row=i, column=j, padx=5,pady=10,ipady=3)"""