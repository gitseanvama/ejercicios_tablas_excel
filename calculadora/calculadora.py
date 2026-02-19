from datetime import datetime

class Calculadora:
    def __init__(self, usuario, numero, tipo_operacion):
        self.__usuario = usuario
        self.__numero = numero
        self.__tipo_operacion = tipo_operacion
        self.__fecha = datetime.now().date()
        self.__resultado = self.calcular()

    def calcular(self):
        n1 = self.__numero.get_num1()
        n2 = self.__numero.get_num2()

        if self.__tipo_operacion == "Suma":
            return n1 + n2
        elif self.__tipo_operacion == "Resta":
            return n1 - n2
        elif self.__tipo_operacion == "Multiplicación":
            return n1 * n2
        elif self.__tipo_operacion == "División":
            return n1 / n2 if n2 != 0 else "Error"
        else:
            return "Operación inválida"

    # Getters
    def get_usuario(self):
        return self.__usuario

    def get_numero(self):
        return self.__numero

    def get_tipo_operacion(self):
        return self.__tipo_operacion

    def get_resultado(self):
        return self.__resultado

    def get_fecha(self):
        return self.__fecha