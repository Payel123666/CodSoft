class student:
    def __init__(self):
        self.student_name=input("Enter the student name: ")
        self.roll=input("Enter the roll number: ")
        self.phy=int(input("Enter the marks in Physics: "))
        self.che=int(input("Enter the marks in chemistry: "))
        print("\n")
        
    def info(self):
        print(f"The name of the student is {self.student_name}.")
        print(f"Roll number of {self.student_name} is {self.roll}.")
        print(f"Marks of {self.student_name} in Physice is {self.phy}.")
        
    def avg(self):
        self.avg=(self.phy+self.che)/2
        print(f"Total average marks of {self.student_name} in Physics and Chemistry is {self.avg}.")
        
    C1= student()
    C1.info()
    C1.avg()