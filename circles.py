import math
def circle_area(r):
    if r<0:
        raise ValueError("The radius cannot be negative")
    if type(r) not in [int,float]:
        raise TypeError("The radius must be a non-negative real number!")
    return math.pi*(r**2)

# radi=[2,0,-3,2+5j,True,"chennai"]
#
# for r in radi:
#     A=circle_area(r)
#     print("Area of circle with r={} is : {}".format(r,A))

