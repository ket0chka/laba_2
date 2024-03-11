import protection
import json
import perv_ob
import logging 

class bus (perv_ob.abc_perv_ob):
        
    def __init__ (self,  vvod ,vivod1, vivod2, storona):
        self.__vvod =  vvod 
        self.__vivod1 = vivod1
        self.__vivod2 = vivod2
        self.__storona = storona
        
        with open (r'C:\Users\Admin\Desktop\help.json') as param:
            tempates = json.load(param)
        self.protection = protection.Protection(tempates['setting'],tempates['reject_probability'], tempates['op_time_reserve'],"Защита шины на стороне " + str(self.__storona))
        

    def get_vivod(self):
        arr = [self.__vivod1,self.__vivod2]
        return arr
    
    def get_vvod(self):
        return self.__vvod
    
    def set_vivod(self,vivod1, vivod2):
        self.__vivod1 = vivod1
        self.__vivod2 = vivod2

    def set_vvod(self,vvod):
        self.__vvod = vvod

    def set_ShortCircuit (self):
        if (self.protection.setShortCircuit()):
            self.__vvod = None 
            self.__vivod1 = None
            self.__vivod2 = None
            logging.info("Отключены все выключатели присоединенные к шине")
