'''
Decorator is a function which accept the function name as paramenter.
And it has an inner function which collects arguments passed to the function
'''
import time
def calc_time(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        res=func(*args,**kwargs)
        end = time.time()
        print(func.__name__+" function took : ", (end - start) * 1000)
        return res
    return wrapper

@calc_time
def squareIt(list1):
    result=[]
    for x in list1:
        result.append(x**2)
    return result

@calc_time
def cubeIt(list1):
    result=[]
    for x in list1:
        result.append(x**3)
    return result

mylist=list(range(1,100001))
squareIt(mylist)
cubeIt(mylist)