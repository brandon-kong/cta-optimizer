class Kilometer:
    def __init__(self, value: float):
        if value is None:
            raise ValueError("Distance cannot be None")

        if not isinstance(value, (int, float)):
            raise ValueError("Distance must be a number")

        if value < 0:
            raise ValueError("Distance cannot be negative")

        self.value = value

    def to_miles(self):
        from cta_optimizer.models.mile import Mile

        return Mile(self.value * 0.621371)

    def __add__(self, other: "Kilometer") -> "Kilometer":
        return Kilometer(self.value + other.value)

    def __sub__(self, other: "Kilometer") -> "Kilometer":
        return Kilometer(self.value - other.value)

    def __eq__(self, other):
        if not isinstance(other, Kilometer):
            return False

        return self.value == other.value

    def __hash__(self):
        return hash(self.value)

    def __str__(self):
        return f"{self.value} km"