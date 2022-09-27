
#Create an object that makes use of protected and private.
#Add comments throughout your Python explaining your code.


class Protected2: ##protected attribute
    def __init__(self):
        self.__privateVar = 9 

    def getPrivate(self): ##private attribute
        print(self.__privateVar)

    def setPrivate(self, private): 
        self.__privateVar = private


obj = Protected2 () #object that makes use of protected and private 
obj.getPrivate()
obj.setPrivate(45)
obj.getPrivate()
