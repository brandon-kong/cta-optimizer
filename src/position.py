class Position:
    
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


    def get_latitude(self):
        return self.latitude
    

    def get_longitude(self):
        return self.longitude
    

    def __str__(self):
        return f'Position(latitude={self.latitude}, longitude={self.longitude})'