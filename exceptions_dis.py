'''
4 exception clauses are available
try
except
else
finally
'''

try:
    with open("days.txt",'r') as rf:
        print(rf.readline())
    #res=2+"three"
    #myfun(5,6)
    age=int(input("Enter your age: "))
    if age<0 or age>100:
        raise ValueError('Age should between 0 to 100')
    print("age enetered is :",age)
except FileNotFoundError as e:
    print("Received File not found exception: ",e)
except TypeError as e:
    print("There is a type error:", e)
except ValueError as e:
    print("Incorrect age entered seems!", e)
except Exception as e:
    print("Caught by default exception,",e)
else:
    print("No Exception Hence else block has run!")
finally:
    print("I am from finally block and run always!")

print("I am from out of try and except code!")