class Automovil:
    def __init__(self, marca, modelo, _velocidad_max, _nivel_combustible, _año_fabricacion):
        self.marca = marca
        self.modelo = modelo
        self._velocidad_max = _velocidad_max
        self._nivel_combustible = _nivel_combustible
        self._año_fabricacion = _año_fabricacion

    @property
    def año_fabricacion(self):
        return self._año_fabricacion

    @año_fabricacion.setter
    def año_fabricacion(self, valor):
        if not (1886 <= valor <= 2026):
            raise ValueError("El año debe estar entre 1886 y 2026")
        self._año_fabricacion = valor

    @property
    def nivel_combustible(self):
        return self._nivel_combustible

    @nivel_combustible.setter
    def nivel_combustible(self, valor):
        if not (0.0 <= valor <= 100.0):
            raise ValueError("El combustible debe estar entre 0 y 100")
        self._nivel_combustible = valor

    @property
    def velocidad_max(self):
        return self._velocidad_max

    @velocidad_max.setter
    def velocidad_max(self, valor):
        if valor <= 0:
            raise ValueError("La velocidad debe ser mayor a 0")
        self._velocidad_max = valor

    def tiempo_llegada(self, distancia_km):
        return distancia_km / self._velocidad_max

    def __str__(self):
        return (f"Automóvil {self.marca} {self.modelo} ({self._año_fabricacion}) | "
                f"Vel. máx: {self._velocidad_max} km/h | "
                f"Combustible: {self._nivel_combustible}%")


if __name__ == "__main__":
    auto = Automovil("Toyota", "Corolla", 180, 50, 2020)
    print(auto)
    print(f"Tiempo a 360 km: {auto.tiempo_llegada(360):.2f} h")

    try:
        auto.año_fabricacion = 1800
    except ValueError as e:
        print(f"Error capturado: {e}")