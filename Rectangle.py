class Rectangle:
    def __init__(self,largo:float,ancho:float):
        self.__largo = largo
        self.__ancho = ancho

    def set_largo(self,largo:float):
        self.__largo = largo

    def get_largo(self):
        return self.__largo        
    def set_ancho(self,ancho:float):
        self.__ancho = ancho

    def get_ancho(self):
        return self.__ancho
    
    def perimetro(self):
        return 2 * (self.__largo * self.__ancho)
    
    def area(self):
        return self.__largo * self.__largo

    def __str__(self):
        imp = f"\nLongitud: {self.__largo}"
        imp += f"\nAncho: {self.__ancho}"
        imp += f"\nPerimetro: {self.perimetro}"
        imp += f"\nArea: {self.area}"
        return imp  
    