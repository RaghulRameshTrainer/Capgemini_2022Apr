from abc import ABC , abstractmethod
class Car(ABC):
    @abstractmethod
    def belt(self):
        pass
    @abstractmethod
    def seats(self):
        pass
    @abstractmethod
    def engine(self):
        pass
    @abstractmethod
    def tyre(self):
        pass

    def price(self,model):
        if model == 'EcoSport':
            print("Price:",1600000)
        elif model == "Aspire":
            print("Price:",1000000)
        elif model == "Figo":
            print("price:",900000)
        else:
            print("Please visit showroom!")

class Fiesta(Car):
    def __init__(self,make,model_year):
        self.make=make
        self.my=model_year

    def belt(self):
        self.belt="Fitted"

    def engine(self):
        self.engine="Petrol Engine"

    def seats(self):
        self.capacity="5 seater"
        return self.capacity

    def tyre(self):
        self.tyre="Fitted"

    def welcome(self):
        print("Welcome to FORD motor car company")
f1=Fiesta("Ford",2015)
f1.welcome()
print(f1.seats())

f1.price("EcoSport")