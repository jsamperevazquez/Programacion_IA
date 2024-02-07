class Vehicle:
    def __init__(self, max_speed, kms):
        if max_speed < 0:
            raise ValueError("La velocidad máxima no puede ser negativa")
        if kms < 0:
            raise ValueError("El kilometraje no puede ser negativo")
        self.max_speed = max_speed
        self.kms = kms

    def __str__(self):
        return (f"Vehículo con:\n"
                f"velocidad_maxima: {self.max_speed}"
                f"\nkilometraje: {self.kms}")


if __name__ == '__main__':
    try:
        pass
    except ValueError as e:
        print(f"Error al instanciar el vehículo, error --> {e}")
