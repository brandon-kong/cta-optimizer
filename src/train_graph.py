from collections import deque
import networkx as nx

from src.train_station import TrainStation, TrainTransfer, TrainAction


class TrainGraph:
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_node(self, node: TrainStation) -> None:
        """
        Add a node to the graph

        :param node: TrainStation
        :return: None
        """
        if node is None:
            raise ValueError("[GraphRepresentation]: node is required")

        if not isinstance(node, TrainStation):
            raise ValueError(
                "[GraphRepresentation]: node must be an instance of TrainStation"
            )

        self.graph.add_node(node)

    def add_edge(
        self, source: TrainStation, destination: TrainStation, weight: float
    ) -> None:
        """
        Add an edge to the graph

        :param source: str
        :param destination: str
        :param weight: float
        :return: None
        """
        if source is None:
            raise ValueError("[GraphRepresentation]: source is required")

        if destination is None:
            raise ValueError("[GraphRepresentation]: destination is required")

        if weight is None:
            raise ValueError("[GraphRepresentation]: weight is required")

        self.graph.add_edge(source, destination, weight=weight)

    def get_shortest_path(
        self, source: TrainStation, destination: TrainStation
    ) -> deque[TrainAction]:
        """
        Get the shortest path between two nodes

        :param source: TrainStation
        :param destination: TrainStation
        :return: nx.DiGraph
        """
        if source is None:
            raise ValueError("[GraphRepresentation]: source is required")

        if destination is None:
            raise ValueError("[GraphRepresentation]: destination is required")

        if not isinstance(source, TrainStation):
            raise ValueError(
                "[GraphRepresentation]: source must be an instance of TrainStation"
            )

        if not isinstance(destination, TrainStation):
            raise ValueError(
                "[GraphRepresentation]: destination must be an instance of TrainStation"
            )

        shortest_path = nx.shortest_path(
            self.graph, source, destination, weight="weight"
        )

        shortest_path_queue = deque(shortest_path)

        queue = deque()

        last_station = source
        while len(shortest_path_queue) > 0:
            station = shortest_path_queue.popleft()

            if last_station.get_line() != station.get_line():
                queue.append(TrainTransfer(station, station))

            queue.append(TrainAction(station))
            last_station = station

        return queue

    def get_graph(self) -> nx.DiGraph:
        """
        Get the graph

        :return: nx.DiGraph
        """
        return self.graph
