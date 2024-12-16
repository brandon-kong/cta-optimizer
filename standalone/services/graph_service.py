"""
graph_service.py
----------------
The GraphService class is responsible for managing the graph building of the train system
and optimization logic for finding the best path between the source and destination stations.
"""

class Graph:
    def __init__(self):
        self.stations = {}

    def add_station(self, station):
        self.stations[station] = {}

    def add_connection(self, source, destination, distance):
        self.stations[source][destination] = distance

    def find_best_path(self, source, destination):
        visited = {source: 0}
        path = {}

        stations = set(self.stations.keys())

        while stations:
            min_station = None
            for station in stations:
                if station in visited:
                    if min_station is None:
                        min_station = station
                    elif visited[station] < visited[min_station]:
                        min_station = station

            if min_station is None:
                break

            stations.remove(min_station)
            current_weight = visited[min_station]

            for connection, distance in self.stations[min_station].items():
                weight = current_weight + distance
                if connection not in visited or weight < visited[connection]:
                    visited[connection] = weight
                    path[connection] = min_station

        if destination not in path:
            return None

        best_path = []
        while destination is not None:
            best_path.append(destination)
            destination = path.get(destination)

        return best_path[::-1]

class GraphService:
    def __init__(self):
        self.graph = Graph()

    def build_graph(self, stations):
        for station in stations:
            self.graph.add_station(station)

    def add_connection(self, source, destination, distance):
        self.graph.add_connection(source, destination, distance)

    def find_best_path(self, source, destination):
        return self.graph.find_best_path(source, destination)