age=37   #global variable

def callme():
    global age
    age=100   #local variable
    print("age inside the fucntion is :",age)   #100

print("age before the function call :",age) #37
callme()
print("age after the function call: ",age)  #37