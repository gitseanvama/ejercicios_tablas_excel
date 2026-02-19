class Usuario:
    def __init__(self, cedula, nombre, tipo_usuario):
        self.cedula = cedula
        self.nombre = nombre
        self.tipo_usuario = tipo_usuario
        
    # GETTERS
    
    def get_cedula(self):
        return self.cedula

    def get_nombre(self):
        return self.nombre

    def get_tipo_usuario(self):
        return self.tipo_usuario

    # SETTERS
    def set_cedula(self, cedula):
        self.cedula = cedula

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_tipo_usuario(self, tipo_usuario):
        self.tipo_usuario = tipo_usuario

    def mostrar_usuario(self):
        return f"{self.cedula} - {self.nombre} - {self.tipo_usuario}"
    