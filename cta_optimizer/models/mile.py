MILE_TO_KILOMETER = 0.621371


class Mile:
    def __init__(self, value: float):
        if value is None:
            raise ValueError("Distance cannot be None")

        if not isinstance(value, (int, float)):
            raise ValueError("Distance must be a number")

        if value < 0:
            raise ValueError("Distance cannot be negative")
        self.value = value

    def to_kilometers(self):
        from cta_optimizer.models.kilometer import Kilometer

        return Kilometer(self.value / MILE_TO_KILOMETER)

    def __add__(self, other: "Mile") -> "Mile":
        return Mile(self.value + other.value)

    def __sub__(self, other: "Mile") -> "Mile":
        return Mile(self.value - other.value)

    def __eq__(self, other):
        if not isinstance(other, Mile):
            return False

        return self.value == other.value

    def __hash__(self):
        return hash(self.value)

    def __str__(self):
        return f"{self.value} miles"
