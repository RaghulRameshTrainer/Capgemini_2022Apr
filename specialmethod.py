class MyClass:
    def __init__(self,name,amount):
        self.name=name
        self.balance=amount

    def __str__(self):
        return "It is MyClass Object"

    def __add__(self,other):
        return self.balance+other.balance

    def __len__(self):
        return len(self.name)

obj1=MyClass("Raghul Ramesh",10000)
obj2=MyClass("Malini Sekar",20000)

print(len(obj1))
print(len(obj2))
