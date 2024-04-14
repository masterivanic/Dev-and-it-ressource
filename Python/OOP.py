"""
    Compose Classes Instead of Nesting Many
    Levels of Built-in Types
"""

from collections import defaultdict
from collections import namedtuple

Grade = namedtuple('Grade', ('score', 'weight'))
    
class Subject:
    def __init__(self) -> None:
        self._grades = []

    def report_grade(self, score, weight):
        self._grades.append(Grade(score, weight))

    def average_grade(self):
        total, toal_weight = 0,0
        for grade in self._grades:
            total += grade.score * grade.weight
            toal_weight += grade.weight
        return total / toal_weight
    
class Student:
    def __init__(self) -> None:
        self._subjects = defaultdict(Subject)

    def get_subject(self, name):
        return self._subjects[name]
    
    def average_grade(self):
        total, count = 0, 0
        for subject in self._subjects.values():
            total += subject.average_grade()
            count += 1
        return total / count
    
class GradeBook:
    def __init__(self) -> None:
        self._students = defaultdict(Student)

    def get_student(self, name):
        return self._students[name]
    
class WeightedGradebook:

    def __init__(self) -> None:
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = defaultdict(list)

    def report_grade(self, name, subject, score, weight):
        by_subject = self._grades[name]
        grade_list = by_subject[subject]
        grade_list.append((score, weight))

    def average_grade(self, name):
        by_subject = self._grades[name]
        score_sum, score_count = 0,0
        for subject, scores in by_subject.items():
            subject_avg, total_weight = 0,0
            for score, weight in scores:
                subject_avg += score * weight
                total_weight += weight
            score_sum += subject_avg / total_weight
            score_count += 1
        return score_sum / score_count


if __name__ == '__main__':
    book = GradeBook()
    ivan_student = book.get_student('Ivan')
    math_note = ivan_student.get_subject('Math')
    math_note.report_grade(75, 0.05)
    math_note.report_grade(65, 0.15)
    math_note.report_grade(70, 0.80)
    gym = ivan_student.get_subject('Gym')
    gym.report_grade(100, 0.40)
    gym.report_grade(85, 0.60)
    print(ivan_student.average_grade())
   





