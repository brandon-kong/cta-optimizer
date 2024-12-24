from cta_optimizer.models.station import Station
from cta_optimizer.models.location import Location

from enum import Enum


class CTATrainLine(Enum):
    RED = "red"
    BLUE = "blue"
    GREEN = "green"
    BROWN = "brown"
    PURPLE = "purple"
    YELLOW = "yellow"
    PINK = "pink"
    ORANGE = "orange"

    def __str__(self):
        return self.value


class CTATrainStation(Station):
    def __init__(self, name: str, location: Location, route: CTATrainLine):
        super().__init__(name, location)
        self.route = route

    def get_id(self):
        return f"{self.route}:{self.name}"

    def get_line(self):
        return self.route

    def __str__(self):
        return f"CTA Train Station: {self.name} ({self.location})"

    def __eq__(self, other):
        if not isinstance(other, CTATrainStation):
            return False

        return (
            self.name == other.name
            and self.location == other.location
            and self.route == other.route
        )

    def __hash__(self):
        return hash((self.name, self.location, self.route))
