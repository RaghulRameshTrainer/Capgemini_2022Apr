import math
class Employee:
    hike=1.2
    def __init__(self,fname,lname,pay):
        self.fname=fname
        self.lname=lname
        self.sal=pay
        self.email=self.fname+'.'+self.lname+'@capgemini.com'

    def fullname(self):
        return "{} {}".format(self.fname,self.lname)

    def appraisal(self):
        self.sal=int(self.sal*self.hike)

    @classmethod
    def create_object(cls,str):
        fn,ln,amt=str.split("-")
        return cls(fn,ln,int(amt))   #Employee("Raghul","Ramesh",100000)

    @staticmethod
    def is_workingday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return "HOLIDAY!"
        return "WORKING DAY"

class Manager:
    def __init__(self,fname,lname,pay,buss_unit):
            self.buss_unit=buss_unit
            self.fname = fname
            self.lname = lname
            self.sal = pay
            self.email = self.fname + '.' + self.lname + '@capgemini.com'

    def fullname(self,title):
        self.title=title
        return "{} {} {}".format(self.title,self.fname,self.lname)

    def mymethod(self,*x):
        return math.prod(x)
"""
mgr_1=Manager('Bala','Murugan',10000,'Insurance')
mgr_2=Manager('Durga','Devi',20000,'Banking')

print(mgr_1.fullname("Mr"))
print(mgr_2.fullname("Miss"))
"""
class Developer(Employee,Manager):
    def fullname(self,title):
        return super(Employee,self).fullname(title)

dev_1=Developer('Dinesh','Kumar',20000)
dev_2=Developer('Ganesh','Senthil',30000)

print(dev_1.fullname('Mr'))
print(dev_2.fullname('Master'))










"""


str1="Raghul-Ramesh-100000"
str2="Levin-Lenus-200000"

emp_1=Employee.create_object(str1)
emp_2=Employee.create_object(str2)

import datetime
dy=datetime.date(2022,4,9)
print(Employee.is_workingday(dy))
# emp_1.hike=1.1
# print("Current Salary:",emp_1.sal)
# emp_1.appraisal()
# print("Revised Salary:",emp_1.sal)
#
# print("Current Salary:",emp_2.sal)
# emp_2.appraisal()
# print("Revised Salary:",emp_2.sal)
"""