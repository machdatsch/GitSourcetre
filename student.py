from module import *
from moduleElement import *

print("habsch")
class Student(object):

    def __init__(self, name):
        ######## CODE MISSING HERE
        self.name = name
        self.modules = []
        self.grades = {}

    def add_module(self,module):
        ######## CODE MISSING HERE
        self.modules.append(module)
        self.grades.update({module:module.get_grade()})

    def get_list_modules(self):
        ######## CODE MISSING HERE
        print("Modules of Student %s" %self.name)
        for module in self.modules:
            print('\t', str(module)[8:])
    def get_grades(self):
        ######## CODE MISSING HERE
        print("Grades of Student %s" % self.name)
        for module in self.grades:
            print('\t', str(module)[8:] + ':', self.grades[module])


### test cases ###

me = Student("FirstName LastName")
me.add_module(info1)
me.get_list_modules()
# expected output:
# Modules of Student FirstName LastName:
#	Info 1

me.get_grades()
# expected output:
# Grades of Student FirstName LastName:
#	Info 1: 6
