import time
import random
import logging 
import ShortCircuit

class Protection ():
    
    def __init__(self,value,veroyatnost_otkaza,op_time_reserve, where):
        self.__value = value
        self.__veroyatnost_otkaza = veroyatnost_otkaza 
        self.__op_time_reserve = op_time_reserve
        self.__current = 10
        self.__where = where

    def rabota_zasgiti(self,tok):

        veroyatnost_otkaza = random.randint(0,100)

        if tok >= int(''.join(map(str, self.__value))) and int(''.join(map(str, self.__veroyatnost_otkaza))) < veroyatnost_otkaza:
            return self.podacha_signala_na_vikluchatel()
        
        elif tok >= int(''.join(map(str, self.__value))):
            time.sleep(int(''.join(map(str, self.__op_time_reserve)))/1000)
            return self.call_reserv_protection()
        
        else:
            logging.info("Значение тока не превышает уставку")
            return False

    # Значения тока и сразу его проверяем на срабатывание защиты
    def setCurrent (self, current ):
        self.__current = current
        return self.rabota_zasgiti(self.__current)

    # возвращем значение тока для других видов первичого оборудования
    def getCurrent (self):
        return self.__current
    
    def setShortCircuit (self):
        return self.setCurrent(ShortCircuit.ShortCircuit(150).get_current())
    
    def podacha_signala_na_vikluchatel (self):
        
        logging.info("Произошло КЗ " + self.__where)
        logging.info ("Сработала основная защита")
        self.__current = 0
        return True
    
    def call_reserv_protection (self):
        logging.info("Произошло кз на " + self.__where)
        logging.info("Сработала резервная защита через " + str((int(''.join(map(str, self.__op_time_reserve))))/1000) + " секунды")
        self.__current = 0
        return True
