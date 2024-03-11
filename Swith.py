
class Swith():
    
    def __init__ (self,vvod = 10, vivod = 10):
        self.__vvod = vvod
        self.__vivod = vivod
        

    def off (self):
        self.__vivod = None


    # get and set
    def getVvod (self):
        return self.__vvod
    
    def getVivod (self):
        return self.__vivod

    def setVvod (self, vvod):
        self.__vvod = vvod
    
    def setVivod (self, vivod):
        self.__vivod = vivod
