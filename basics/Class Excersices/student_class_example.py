class Student:
    def __init__(self, name, list_of_marks):
        self.name = name
        self.list_of_marks = list_of_marks

    def get_number_of_marks(self):
        return len(self.list_of_marks)

    def get_sum_of_marks(self):
        return sum(self.list_of_marks)

    def determine_max_marks_of_student(self):
        return max(self.list_of_marks)

    def determine_min_marks_of_student(self):
        return min(self.list_of_marks)

    def determine_average_marks_of_student(self):
        return self.get_sum_of_marks() / self.get_number_of_marks()

    def add_marks(self, marks):
        self.list_of_marks.append(marks)

    def remove_marks_at_index(self, index):
        del self.list_of_marks[index]

    def print_details(self):
        print('\n Student :', self.name, '\n Student Total Marks:', self.get_sum_of_marks(),
              '\n Maximum Marks Obtained:', self.determine_max_marks_of_student()
              , '\n Minimum Marks Obtained:', self.determine_min_marks_of_student(),
              '\n Average Marks of the student:', self.determine_average_marks_of_student())
        print(' Mark List:')
        for mark in self.list_of_marks:
            print(' ', mark, end=' ')

lalit = Student('Lalit', [90, 98, 95, 65])
lalit.print_details()

lalit.add_marks(75)
lalit.print_details()

lalit.remove_marks_at_index(3)
lalit.print_details()

