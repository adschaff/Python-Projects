from abc import ABC, abstractmethod
class awesome(ABC):
    def paySlip(self, level):
        print("Your awesomness level: ", level)
#this function is telling us to pass in aargument, but we won't tell you how or what of data it will be
    @abstractmethod
    def payment(self, level):
        pass

class Awesomeness(awesome):
#here we've defined how to implement thep ayment functino from its parent paySlip class.
    def payment(self, level):
        print("Your awesomeness level of {} exceeded our scale of 500!".format(level))

obj = Awesomeness()
obj.paySlip("700")
obj.payment("700")


