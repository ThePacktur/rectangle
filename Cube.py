from Rectangle import Rectangle

class Cube(Rectangle):
    def __init__(self, largo: float, ancho: float,lado3:float):
        super().__init__(largo, ancho)
        self.__lado3 = lado3
    def set_lado3(self,lado3:float):
        self.__lado3 = lado3

    def get_lado3(self):
        return self.__lado3
    
    def volumen(self):
        return super().get_largo * super().get_ancho * self.__lado3
    
    def __str__(self):
        imp =  super().__str__()
        imp += f"\nLado3: {self.__lado3}"
        imp += f"\nVolumen: {self.volumen()}"
