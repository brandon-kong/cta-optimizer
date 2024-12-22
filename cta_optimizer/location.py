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

    def __str__(self):
        return f"Location: {self.latitude}, {self.longitude}"

    def __eq__(self, other):
        if not isinstance(other, Location):
            return False

        return self.latitude == other.latitude and self.longitude == other.longitude

    def __hash__(self):
        return hash((self.latitude, self.longitude))