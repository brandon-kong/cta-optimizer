from .position import Position
from .train_line import CTATrainLine

class TrainStation:

    def __init__(self, name: str=None, line: CTATrainLine=None, position: Position=None):
        self.__set_name(name)
        self.__set_position(position)
        self.__set_line(line)

        self.transfer_stations: list[TrainStation] = []


    def add_transfer_station(self, station: 'TrainStation'):
        if station is None:
            raise ValueError('[TrainStation]: station is required')
        
        if not isinstance(station, TrainStation):
            raise ValueError('[TrainStation]: station must be an instance of TrainStation')
        
        self.transfer_stations.append(station)

        
    def get_transfer_stations(self):
        return self.transfer_stations
    

    def get_name(self):
        return self.name


    def get_position(self):
        return self.position
    

    def get_line(self):
        return self.line
    
    def __set_name(self, name: str):
        if name is None:
            raise ValueError('[TrainStation]: name is required')
        
        if not isinstance(name, str):
            raise ValueError('[TrainStation]: name must be a string')
        
        self.name = name


    def __set_position(self, position: Position):
        if position is None:
            raise ValueError('[TrainStation]: position is required')
        
        if not isinstance(position, Position):
            raise ValueError('[TrainStation]: position must be an instance of Position')
        
        self.position = position


    def __set_line(self, line: CTATrainLine):
        if line is not None and not isinstance(line, CTATrainLine):
            raise ValueError('[TrainStation]: line must be a string')
        
        self.line = line
    

    def __str__(self):
        return f'{self.name} ({self.line})'
    
