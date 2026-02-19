class Usuario:
    def __init__(self, cedula, nombre):
        self.__cedula = cedula
        self.__nombre = nombre

    # Getters
    def get_cedula(self):
        return self.__cedula

    def get_nombre(self):
        return self.__nombre

    # Setters
    def set_cedula(self, cedula):
        self.__cedula = cedula

    def set_nombre(self, nombre):
        self.__nombre = nombre