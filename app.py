from abc import ABC,abstractmethod

class Vechile(ABC):
     @abstractmethod
     def start_engine(self):
        pass
      # doosra abstract method
     @abstractmethod
     def stop_engine(self): 
         pass
     
class Car(Vechile):    #inharit vechile class
    def start_engine(self):    # implementation abstract
        print("Car engine started")

    def stop_engine(self):    # second implement
        print("Car engine stopped")


class Motorcycle(Vechile):
    def start_engine(self):
        print("Motorcyle engine started")

    def stop_engine(self):
        print("Motorcyle engine stopped")
    




# object create
Vechile1 = Car()
Vechile2 = Motorcycle()

Vechile1.start_engine() 
Vechile2.stop_engine() 