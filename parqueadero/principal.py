# principal.py

from usuario import Usuario
from carro import Carro
from parqueadero import RegistroParqueadero

def main():

    registros = []  

    # -------- CREAR REGISTROS --------

    usuario1 = Usuario("1020345678", "Juan García", "Administrador")
    carro1 = Carro("ABC123", "Sedan", "Negro")
    registro1 = RegistroParqueadero(usuario1, carro1, "A-01")
    registro1.registrar_salida()

    usuario2 = Usuario("1020345679", "María López", "Cliente")
    carro2 = Carro("XYZ789", "SUV", "Blanco")
    registro2 = RegistroParqueadero(usuario2, carro2, "B-05")

    usuario3 = Usuario("1020345680", "Carlos Rodríguez", "Cliente")
    carro3 = Carro("KLM456", "Pickup", "Azul")
    registro3 = RegistroParqueadero(usuario3, carro3, "C-12")
    registro3.registrar_salida()

    usuario4 = Usuario("1020345681", "Ana Martínez", "Administradora")
    carro4 = Carro("DEF321", "Hatchback", "Rojo")
    registro4 = RegistroParqueadero(usuario4, carro4, "A-03")

    registros.extend([registro1, registro2, registro3, registro4])

    # -------- IMPRIMIR TABLA --------

    print("\n" + "-" * 140)
    print(f"{'Cédula':<12} {'Nombre':<20} {'Tipo Usuario':<15} {'Placa':<10} "
          f"{'Tipo Carro':<12} {'Color':<10} {'Puesto':<8} "
          f"{'Fecha Entrada':<15} {'Hora Entrada':<12} "
          f"{'Hora Salida':<12} {'Estado':<10}")
    print("-" * 140)

    for r in registros:
        print(f"{r.get_usuario().get_cedula():<12} "
              f"{r.get_usuario().get_nombre():<20} "
              f"{r.get_usuario().get_tipo_usuario():<15} "
              f"{r.get_carro().get_placa():<10} "
              f"{r.get_carro().get_tipo_carro():<12} "
              f"{r.get_carro().get_color():<10} "
              f"{r.get_puesto():<8} "
              f"{str(r.get_fecha_entrada()):<15} "
              f"{r.get_hora_entrada():<12} "
              f"{str(r.get_hora_salida() if r.get_hora_salida() else ''):<12} "
              f"{r.get_estado():<10}")

    print("-" * 140)


# Ejecutar solo una vez
if __name__ == "__main__":
    main()
