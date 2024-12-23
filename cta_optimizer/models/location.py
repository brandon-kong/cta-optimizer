from math import radians, sin, cos, sqrt, asin
from cta_optimizer.models.kilometer import Kilometer

class Location:
    def __init__(self, latitude: float, longitude: float):
        self.__validate_latitude(latitude)
        self.__validate_longitude(longitude)

        self.latitude = latitude
        self.longitude = longitude

    @staticmethod
    def __validate_latitude(latitude: float):
        if latitude is None:
            raise ValueError("Latitude cannot be None")

        if not isinstance(latitude, (int, float)):
            raise ValueError("Latitude must be a number")

        if latitude < -90 or latitude > 90:
            raise ValueError("Latitude must be between -90 and 90")

    @staticmethod
    def __validate_longitude(longitude: float):
        if longitude is None:
            raise ValueError("Longitude cannot be None")

        if not isinstance(longitude, (int, float)):
            raise ValueError("Longitude must be a number")

        if longitude < -180 or longitude > 180:
            raise ValueError("Longitude must be between -180 and 180")

    def get_coordinates(self):
        return self.latitude, self.longitude

    def get_latitude(self):
        return self.latitude

    def get_longitude(self):
        return self.longitude

    def distance_to(self, other: "Location") -> Kilometer:
        """
        Calculate the distance between this location and another location using the Haversine formula

        :param other: The other location
        :return: The distance between the two locations in kilometers
        """

        if not isinstance(other, Location):
            raise ValueError("Invalid location")

        lat1, lon1 = self.get_coordinates()
        lat2, lon2 = other.get_coordinates()

        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

        # haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * asin(sqrt(a))
        r = 6371  # Radius of earth in kilometers. Use 3956 for miles. Determines return value units.
        return Kilometer(c * r)


    def __str__(self):
        return f"Location: {self.latitude}, {self.longitude}"

    def __eq__(self, other):
        if not isinstance(other, Location):
            return False

        return self.latitude == other.latitude and self.longitude == other.longitude

    def __hash__(self):
        return hash((self.latitude, self.longitude))