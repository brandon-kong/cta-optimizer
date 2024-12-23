from networkx import DiGraph

from cta_optimizer.models.station import Station


class StationsGraphService:
    def __init__(self):
        self.graph = DiGraph()

    def add_station(self, station: Station):
        self.graph.add_node(station)

    def add_edge(self, station1: Station, station2: Station):
        distance = station1.get_location().distance_to(station2.get_location())
        self.graph.add_weighted_edges_from([(station1, station2, distance.value)])

    def get_adjacent_stations(self, station: Station):
        return self.graph.adj[station]

    def get_all_stations(self):
        return self.graph.nodes()
