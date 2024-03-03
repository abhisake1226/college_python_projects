class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}

    def read_edge_list_file(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                edge = line.strip().split()
                if len(edge) == 2:
                    node1, node2 = edge
                    self.add_edge(node1, node2)

    def add_node(self, node):
        self.nodes.add(node)

    def remove_node(self, node):
        if node in self.nodes:
            self.nodes.remove(node)
            if node in self.edges:
                del self.edges[node]
            for n in self.edges:
                if node in self.edges[n]:
                    self.edges[n].remove(node)

    def add_edge(self, node1, node2):
        self.add_node(node1)
        self.add_node(node2)
        self.edges.setdefault(node1, set()).add(node2)
        self.edges.setdefault(node2, set()).add(node1)

    def remove_edge(self, node1, node2):
        if node1 in self.edges and node2 in self.edges[node1]:
            self.edges[node1].remove(node2)
            self.edges[node2].remove(node1)

    def get_neighbors(self, node):
        return self.edges.get(node, set())

    def print_nodes(self):
        print("Nodes:", ", ".join(sorted(self.nodes)))

    def print_edges(self):
        print("Edges:")
        for node, neighbors in self.edges.items():
            for neighbor in neighbors:
                if (neighbor, node) not in self.edges:
                    print(f"{node} - {neighbor}")

    def __str__(self):
        output = ""
        for node, neighbors in self.edges.items():
            for neighbor in neighbors:
                if (neighbor, node) not in self.edges:
                    output += f"{node} - {neighbor}\n"
        return output


# Example usage:
graph = Graph()
graph.read_edge_list_file('edge_list.txt')

graph.print_nodes()
graph.print_edges()

print("Neighbors of 'A':", graph.get_neighbors('A'))
