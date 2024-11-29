from typing import Dict

class Position:
    positions: Dict[str, 'Position'] = {}
    
    def __init__(self, latitude: float=None, longitude: float=None):
        self.__set_latitude(latitude)
        self.__set_longitude(longitude)


    def __set_latitude(self, latitude: float):
        if latitude is None:
            raise ValueError('[Position]: latitude is required')
        
        if not isinstance(latitude, float):
            raise ValueError('[Position]: latitude must be a float')
        
        self.latitude = latitude


    def __set_longitude(self, longitude: float):
        if longitude is None:
            raise ValueError('[Position]: longitude is required')
        
        if not isinstance(longitude, float):
            raise ValueError('[Position]: longitude must be a float')
        
        self.longitude = longitude


    def get_latitude(self) -> float:
        return self.latitude
    

    def get_longitude(self) -> float:
        return self.longitude
    

    def distance_to(self, position: 'Position') -> float:
        return ((self.latitude - position.get_latitude()) ** 2 + (self.longitude - position.get_longitude()) ** 2) ** 0.5
    

    def __str__(self) -> str:
        return Position.format_position(self.latitude, self.longitude)
    

    def __eq__(self, other: 'Position') -> bool:
        if other is None:
            return False
        
        if not isinstance(other, Position):
            return False
        
        return self.latitude == other.get_latitude() and self.longitude == other.get_longitude()
    

    @staticmethod
    def format_position(latitude: float, longitude: float) -> str:
        return f'Position(latitude={latitude}, longitude={longitude})'