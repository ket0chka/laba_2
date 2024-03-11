import protection
import json
import perv_ob
import random
import logging 

class Line (perv_ob.abc_perv_ob):
        
    def __init__ (self,  vvod, name):
        self.__vvod =  vvod 
        self.__name = name
        
        with open (r'C:\Users\Admin\Desktop\help.json') as param:
            tempates = json.load(param)
        self.protection = protection.Protection(tempates['setting'],tempates['reject_probability'], tempates['op_time_reserve'], str(self.__name))
        
    def get_vivod(self):
        pass
    
    def get_vvod(self):
        return self.__vvod
    
    def set_vivod(self,vivod):
        self.__vivod = vivod

    def set_vvod(self,vvod):
        self.__vvod = vvod
    
    def set_ShortCircuit (self):
        veroyatnost_samoystraneniya = random.randint(0,100)
        if (veroyatnost_samoystraneniya <50):
            logging.info("КЗ на "+str(self.__name)+" самоустранилось")
        elif (self.protection.setShortCircuit()):
            self.__vvod = None 
            logging.info("Отключен выключатель со стороны шины")
