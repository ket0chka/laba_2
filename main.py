
import random
from TR import TR 
from Swith import Swith
from bus import bus
from line import Line
import logging 
# создание и настройка логгера
logger = logging.getLogger() 
logger.setLevel(logging.DEBUG)

# Создание обработчика для вывода логов в консоль
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Создание форматтера для логов
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# Добавление обработчиков в логгер
logger.addHandler(console_handler)
logger.info('This is an info message')
# Выключатели между шиной вн и трансформаторами
sw_VN_1 = Swith()
sw_VN_2 = Swith()
sw_Vhod = Swith()
#Шина со стороны вн
sh_VN = bus(sw_Vhod.getVivod(),sw_VN_1.getVvod(), sw_VN_2.getVvod(),"ВН")

# Выключатели для сторон СН обоих трансформаторов
sw_SN_1 = Swith()
sw_SN_2 = Swith()
# Выключатели для сторон НН обоих трансформаторов
sw_NN_1 = Swith()
sw_NN_2 = Swith()
# Трансформаторы
tr1 = TR(sw_VN_1.getVivod(),sw_SN_1.getVvod(),sw_NN_1.getVvod())
tr2 = TR(sw_VN_2.getVivod(),sw_SN_2.getVvod(),sw_NN_2.getVvod())
# Линии со стороны СН
line1 = Line(sw_SN_1.getVivod(), "Линия №1 (СН)")
line2 = Line(sw_SN_2.getVivod(), "Линия №2 (СН)")

#Выключатели после шин для линий
sw_NN_Line1 = Swith()
sw_NN_Line2 = Swith()
sw_NN_Line3 = Swith()
sw_NN_Line4 = Swith()
# Шина со стороны НН
sh_NN_1 = bus(sw_NN_1.getVivod(),sw_NN_Line1.getVvod(), sw_NN_Line2.getVvod(),"НН")
sh_NN_2 = bus(sw_NN_2.getVivod(),sw_NN_Line3.getVvod(), sw_NN_Line4.getVvod(),"НН")
# Отходяшии линии НН
line3 = Line(sw_NN_Line1.getVivod(), "Линия №1 (НН)")
line4 = Line(sw_NN_Line2.getVivod(), "Линия №2 (НН)")
line5 = Line(sw_NN_Line3.getVivod(), "Линия №3 (НН)")
line6 = Line(sw_NN_Line4.getVivod(), "Линия №4 (НН)")

oborydovanie = (sh_VN,tr1,tr2,line1,line2,sh_NN_1,sh_NN_2,line3,line4,line5,line6)

i = 0
while i < 16:
    random.choice(oborydovanie).set_ShortCircuit()
    i += 1
    logging.info("---------------------------------------------Итерация #"+ str(i) + "-------------------------------------")
