from usuario import Usuario
from numero import Numero
from calculadora import Calculadora

def main():

    registros = []

    # Usuario 1
    u1 = Usuario("1020345678", "Juan García López")
    registros.append(Calculadora(u1, Numero(50, 30), "Suma"))
    registros.append(Calculadora(u1, Numero(50, 30), "Resta"))
    registros.append(Calculadora(u1, Numero(50, 30), "Multiplicación"))
    registros.append(Calculadora(u1, Numero(150, 3), "División"))

    # Usuario 2
    u2 = Usuario("1020345679", "María López Pérez")
    registros.append(Calculadora(u2, Numero(100, 5), "Suma"))
    registros.append(Calculadora(u2, Numero(100, 5), "Resta"))
    registros.append(Calculadora(u2, Numero(100, 5), "Multiplicación"))
    registros.append(Calculadora(u2, Numero(100, 5), "División"))

    # Usuario 3
    u3 = Usuario("1020345680", "Carlos Rodríguez Sánchez")
    registros.append(Calculadora(u3, Numero(200, 8), "Suma"))
    registros.append(Calculadora(u3, Numero(200, 8), "Resta"))
    registros.append(Calculadora(u3, Numero(75, 3), "División"))

    # -------- IMPRIMIR TABLA --------

    print("\n" + "-" * 120)
    print(f"{'Cédula':<12} {'Nombre Usuario':<25} {'Número 1':<10} {'Número 2':<10} "
          f"{'Tipo Operación':<18} {'Resultado':<12} {'Fecha de Uso':<12}")
    print("-" * 120)

    for r in registros:
        print(f"{r.get_usuario().get_cedula():<12} "
              f"{r.get_usuario().get_nombre():<25} "
              f"{r.get_numero().get_num1():<10} "
              f"{r.get_numero().get_num2():<10} "
              f"{r.get_tipo_operacion():<18} "
              f"{r.get_resultado():<12} "
              f"{str(r.get_fecha()):<12}")

    print("-" * 120)


if __name__ == "__main__":
    main()