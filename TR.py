import protection
import json
import perv_ob
import random
import logging 

class TR (perv_ob.abc_perv_ob):

    def __init__ (self,  vvod , vivod_SN, vivod_NN ):
        self.__vvod =  vvod 
        self.__vivvod_SN = vivod_SN
        self.__vivvod_NN = vivod_NN
        self.__vivodi =  {self.__vivvod_SN: 10, self.__vivvod_NN:10}
        
        with open (r'C:\Users\Admin\Desktop\help.json') as param:
            tempates = json.load(param)

        self.__protection__VN = protection.Protection(tempates['setting'],tempates['reject_probability'], tempates['op_time_reserve'], "Сторона ВН трансформатора")
        self.__protection__SN = protection.Protection(tempates['setting'],tempates['reject_probability'], tempates['op_time_reserve'], "Сторона СН трансформатора")
        self.__protection__NN = protection.Protection(tempates['setting'],tempates['reject_probability'], tempates['op_time_reserve'],"Сторона НН трансформатора")
        self.__protection__inside = protection.Protection(tempates['setting'],tempates['reject_probability'], tempates['op_time_reserve'], "Внутренняя защита трансформатора")
    
    
    def get_vivod(self):
        return self.__vivodi
    
    def get_vvod(self):
        return self.__vvod
    
    def set_vivod(self,vivod):
        self.__vivodi = vivod

    def set_vvod(self,vvod):
        self.__vvod = vvod
    
    def set_ShortCircuit (self):
        arr = [self.__protection__inside, self.__protection__SN, self.__protection__NN, self.__protection__VN]
        per = random.choice(arr) 
        result = per.setShortCircuit()
        if per == self.__protection__inside and result:
            self.__vvod =  None 
            self.__vivvod_SN = None
            self.__vivvod_NN = None
            logging.info ("Отключены все выключатели")
        elif per == self.__protection__VN and result:
            self.__vvod =  None 
            self.__vivvod_SN = None
            self.__vivvod_NN = None
            logging.info("Отключены все выключатели")
        elif per == self.__protection__SN and result:
            self.__vivvod_SN = None
            logging.info("Отключен выключатель со стороны CН")
        elif per == self.__protection__NN and result:
            self.__vivvod_NN = None
            logging.info("Отключен выключатель со стороны НН")
