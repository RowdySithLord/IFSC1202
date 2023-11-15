class Student:
    def __init__(self, firstname, lastname, tnumber, scores):
        self.FirstName = firstname
        self.LastName = lastname
        self.TNumber = tnumber
        self.Grades = [int(score) if score != '' else 0 for score in scores]

    def RunningAverage(self):
        non_blank_scores = [score for score in self.Grades if score != 0]
        return sum(non_blank_scores) / len(non_blank_scores)

    def TotalAverage(self):
        return sum(self.Grades) / len(self.Grades)

    def LetterGrade(self):
        average = self.TotalAverage()
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'

with open('10.Project Student Scores.txt', 'r') as file:
    for line in file:
        data = line.strip().split(',')
        student = Student(data[0], data[1], data[2], data[3:])
        print(f"Student: {student.FirstName} {student.LastName}")
        print(f"Running Average: {student.RunningAverage()}")
        print(f"Total Average: {student.TotalAverage()}")
        print(f"Letter Grade: {student.LetterGrade()}\n")

