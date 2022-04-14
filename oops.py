class Employee:
    hike=1.1
    def __init__(self,fname,lname,pay):
        self.fname=fname
        self.lname=lname
        self.sal=pay
        self.email=self.fname+'.'+self.lname+'@capgemini.com'

    def fullname(self):
        return "{} {}".format(self.fname,self.lname)

    def appraisal(self):
        self.sal=int(self.sal*self.hike)

emp_1=Employee('Raghul','Ramesh',50000)
emp_2=Employee('Levin','Lenus',60000)

emp_1.hike=2
print("Current Salary:",emp_1.sal)
emp_1.appraisal()
print("Revised Salary:",emp_1.sal)

print("Current Salary:",emp_2.sal)
emp_2.appraisal()
print("Revised Salary:",emp_2.sal)