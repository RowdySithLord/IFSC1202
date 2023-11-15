class Student:
    def __init__(self, FirstName, LastName, TNumber):
        self.FirstName = FirstName
        self.LastName = LastName
        self.TNumber = TNumber
        self.scores = []

class StudentList:
    def __init__(self):
        self.Studentlist = []

    def add_student(self, FirstName, LastName, TNumber):
        student = Student(FirstName, LastName, TNumber)
        self.Studentlist.append(student)

    def find_student(self, TNumber):
        for i, student in enumerate(self.Studentlist):
            if student.TNumber == TNumber:
                return i
        return -1

    def print_student_list(self):
        for student in self.Studentlist:
            print(f"FirstName: {student.FirstName}, LastName: {student.LastName}, TNumber: {student.TNumber}, Scores: {student.scores}")

    def add_student_from_file(self, filename):
        with open('11.Project Students.txt', 'r') as file:
            for line in file:
                FirstName, LastName, TNumber = line.strip().split(',')
                self.add_student(FirstName, LastName, TNumber)

    def add_scores_from_file(self, filename):
        with open('11.Project Scores.txt', 'r') as file:
            for line in file:
                TNumber, score = line.strip().split(',')
                index = self.find_student(TNumber)
                if index != -1:
                    self.Studentlist[index].scores.append(score)

# Main Program
student_list = StudentList()
student_list.add_student_from_file('11.Project Students.txt')
student_list.add_scores_from_file('11.Project Scores.txt')
student_list.print_student_list()
