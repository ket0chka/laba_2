import abc

class abc_perv_ob (abc.ABC):
    def __init__ (self):
        super.__init__(self)

    @abc.abstractmethod
    def get_vvod (self):
        pass

    @abc.abstractmethod
    def get_vivod (self):
        pass
    
    @abc.abstractmethod
    def set_vvod (self):
        pass

    @abc.abstractmethod
    def set_vivod (self):
        pass

    @abc.abstractmethod
    def set_ShortCircuit (self):
        pass
