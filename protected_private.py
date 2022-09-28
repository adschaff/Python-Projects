class Protected: #private class
    def __init__(self):
        self.__privateVar = 12

    def getPrivate(self): ##private attribute
        print(self.__privateVar)

    def setPrivate(self, private): 
        self.__privateVar = private

obj = Protected()
obj.getPrivate()
obj.setPrivate(45)
obj.getPrivate()


class Protected: #protected class
    def __init__(self):
        self._protectedVar = 0 #protected attribute


obj = Protected()
obj._protectedVar = 8 #object that makes use of protected 
print(obj._protectedVar)
