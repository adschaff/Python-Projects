class Protected: #private class
    def __init__(self):
        self.__privateVar = 12

    def getPrivate(self): ##private attribute
        print(self.__privateVar)

    def setPrivate(self, private): 
        self.__privateVar = private

     def __init__(self):
        self._protectedVar = 0 #protected attribute
        print(obj._protectedVar)

        

obj = Protected()
obj.getPrivate()
obj.setPrivate(45)
obj.getPrivate()
obj._protectedVar = 8 

