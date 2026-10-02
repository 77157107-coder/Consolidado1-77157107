class CuentaBancaria:
    def __init__(self, numero_cuenta, titular, __saldo=0.0):
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self.__saldo = __saldo

    def depositar(self, monto):
        if monto <= 0:
            raise ValueError("El monto debe ser positivo")
        self.__saldo += monto

    def retirar(self, monto):
        if monto <= 0:
            raise ValueError("El monto debe ser positivo")
        if monto > self.__saldo:
            raise ValueError("Saldo insuficiente")
        self.__saldo -= monto

    def consultar_saldo(self):
        return self.__saldo

    def __str__(self):
        return f"Cuenta {self.numero_cuenta} - {self.titular} | Saldo: {self.__saldo}"


class CuentaAhorros(CuentaBancaria):
    def __init__(self, numero_cuenta, titular, saldo, tasa_interes):
        super().__init__(numero_cuenta, titular, saldo)
        self.tasa_interes = tasa_interes

    def calcular_interes(self):
        return self.consultar_saldo() * self.tasa_interes / 100

    def __str__(self):
        return super().__str__() + f" | Tasa: {self.tasa_interes}% | Interés: {self.calcular_interes():.2f}"


class CuentaCorriente(CuentaBancaria):
    def __init__(self, numero_cuenta, titular, saldo, limite_sobregiro):
        super().__init__(numero_cuenta, titular, saldo)
        self.limite_sobregiro = limite_sobregiro

    def retirar(self, monto):
        if monto <= 0:
            raise ValueError("El monto debe ser positivo")
        if monto > self.consultar_saldo() + self.limite_sobregiro:
            raise ValueError("Excede el límite de sobregiro")
        # usamos setter indirecto
        self._CuentaBancaria__saldo -= monto

    def permite_sobregiro(self):
        return self.consultar_saldo() < 0


if __name__ == "__main__":
    ahorro = CuentaAhorros("001", "Ana", 1000, 4.5)
    ahorro.depositar(500)
    print(ahorro)
    print(f"Interés: {ahorro.calcular_interes():.2f}")

    corriente = CuentaCorriente("002", "Luis", 200, 300)
    corriente.retirar(400)
    print(corriente)
    print(f"¿Permite sobregiro? {corriente.permite_sobregiro()}")