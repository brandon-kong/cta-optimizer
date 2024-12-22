from cta_optimizer.station import Station
from cta_optimizer.location import Location

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
    def __init__(self, name: str, location: Location, line: CTATrainLine):
        super().__init__(name, location)
        self.line = line

    def get_line(self):
        return self.line

    def __str__(self):
        return f"CTA Train Station: {self.name} ({self.location})"

    def __eq__(self, other):
        if not isinstance(other, CTATrainStation):
            return False

        return self.name == other.name and self.location == other.location and self.line == other.line

    def __hash__(self):
        return hash((self.name, self.location, self.line))