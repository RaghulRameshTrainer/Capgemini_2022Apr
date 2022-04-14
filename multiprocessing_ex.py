import multiprocessing
from time import sleep

def calc_square(nums):
    for n in nums:
        print('square',(n*n))
        sleep(1)

def calc_cube(nums):
    for n in nums:
        print('cube',(n*n*n))
        sleep(1)

if __name__=="__main__":
    mylist=[1,2,3,4,5]
    p1=multiprocessing.Process(target=calc_square,args=(mylist,))
    p2=multiprocessing.Process(target=calc_cube,args=(mylist,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("DoNe")