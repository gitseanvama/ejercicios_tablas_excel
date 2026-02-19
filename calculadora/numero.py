class Numero:
    def __init__(self, num1, num2):
        self.__num1 = num1
        self.__num2 = num2

    # Getters
    def get_num1(self):
        return self.__num1

    def get_num2(self):
        return self.__num2

    # Setters
    def set_num1(self, num1):
        self.__num1 = num1

    def set_num2(self, num2):
        self.__num2 = num2
        
    def mostrar_info(self):
        return f"Numero 1: {self.__num1} - Numero 2: {self.__num2}"