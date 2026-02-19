class Carro:
    def __init__(self, placa, tipo_carro, color):
        self.placa = placa
        self.tipo_carro = tipo_carro
        self.color = color
        
    # GETTERS
    
    def get_placa(self):
        return self.placa

    def get_tipo_carro(self):
        return self.tipo_carro

    def get_color(self):
        return self.color

    # SETTERS
    def set_placa(self, placa):
        self.placa = placa

    def set_tipo_carro(self, tipo_carro):
        self.tipo_carro = tipo_carro

    def set_color(self, color):
        self.color = color

    def mostrar_carro(self):
        return f"{self.placa} - {self.tipo_carro} - {self.color}"