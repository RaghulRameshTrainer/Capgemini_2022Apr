from threading import *
from time import sleep
class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)

class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)

t1=Hi()
t2=Hello()

t1.start()
t2.start()

t1.join()
t2.join()

print("--COMPLETED--")