import math
from AreaConfig import AreaConfig


class MathUtility:

    @staticmethod
    def distance(pos1, pos2):
        return math.sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)


class Node:
    def __init__(self, pos, name):
        self.pos = pos
        self.name = name


class Edge:
    def __init__(self, nodeA, nodeB):
        self.nodeA = nodeA
        self.nodeB = nodeB


class CityMap:
    """
    Use Floyd Method to find shortest path.
    """
    def __init__(self, node_list, edge_list):
        self.node_list = node_list
        self.edge_list = edge_list
        self.edge_pair_list = [[edge.nodeA, edge.nodeB] for edge in edge_list]
        self.dis_matrix = None
        self.path_matrix = None
        self.update_matrix()

    def update_matrix(self):
        INFINITE = 65535
        nodes_num = len(self.node_list)
        dis_matrix = [[0 for i in range(nodes_num)] for i in range(nodes_num)]
        path_matrix = [[0 for i in range(nodes_num)] for i in range(nodes_num)]

        # initial dis_matrix
        for i in range(nodes_num):
            for j in range(nodes_num):
                if [self.node_list[i], self.node_list[j]] in self.edge_pair_list or \
                        [self.node_list[j], self.node_list[i]] in self.edge_pair_list:
                    dis_matrix[i][j] = MathUtility.distance(self.node_list[i].pos, self.node_list[j].pos)
                    dis_matrix[j][i] = MathUtility.distance(self.node_list[i].pos, self.node_list[j].pos)
                    path_matrix[i][j] = self.node_list[i].name
                    path_matrix[j][i] = self.node_list[j].name
                elif i == j:
                    dis_matrix[i][j] = 0
                    path_matrix[i][j] = self.node_list[i].name
                else:
                    dis_matrix[i][j] = INFINITE
                    path_matrix[i][j] = "NO"
        
        # calculate dis_matrix
        for k in range(nodes_num):
            for i in range(nodes_num):
                for j in range(nodes_num):
                    if dis_matrix[i][j] > dis_matrix[i][k] + dis_matrix[k][j]:
                        dis_matrix[i][j] = dis_matrix[i][k] + dis_matrix[k][j]
                        path_matrix[i][j] = self.node_list[k].name

        self.dis_matrix = dis_matrix
        self.path_matrix = path_matrix
    
    def print_matrix(self):
        nodes_num = len(self.node_list)
        for i in range(nodes_num):
            for j in range(nodes_num):
                print("%2d" % self.dis_matrix[i][j], end=' ')
            print("")

        print("------------------------------------")

        for i in range(nodes_num):
            for j in range(nodes_num):
                print(self.path_matrix[i][j], end=' ')
            print("")

    @staticmethod
    def find_node_by_name(name, node_list):
        for node in node_list:
            if node.name == name:
                return node

    def find_path(self, posA, posB, path_list):
        idxA = self.node_list.index(posA)
        idxB = self.node_list.index(posB)

        mid = self.find_node_by_name(self.path_matrix[idxA][idxB], self.node_list)
        if mid.name == posA.name:
            return

        self.find_path(posA, mid, path_list)
        path_list.append(mid)
        self.find_path(mid, posB, path_list)


def main():

    node_list = []

    node1 = Node([0, 0], "A")
    node_list.append(node1)
    node2 = Node([10, 0], "B")
    node_list.append(node2)
    node3 = Node([0, 10], "C")
    node_list.append(node3)
    node4 = Node([10, 10], "D")
    node_list.append(node4)
    node5 = Node([0, 20], "E")
    node_list.append(node5)
    node6 = Node([10, 20], "F")
    node_list.append(node6)
    node7 = Node([20, 20], "G")
    node_list.append(node7)

    edge_list = []

    edge1 = Edge(node1, node2)
    edge_list.append(edge1)
    edge2 = Edge(node2, node4)
    edge_list.append(edge2)
    edge3 = Edge(node4, node3)
    edge_list.append(edge3)
    edge4 = Edge(node3, node1)
    edge_list.append(edge4)
    edge5 = Edge(node3, node5)
    edge_list.append(edge5)
    edge6 = Edge(node5, node6)
    edge_list.append(edge6)
    edge7 = Edge(node6, node4)
    edge_list.append(edge7)
    edge8 = Edge(node6, node7)
    edge_list.append(edge8)

    cityMap = CityMap(node_list, edge_list)
    cityMap.print_matrix()
    print("------------------------------------")
    path_list = []
    cityMap.find_path(node1, node7, path_list)
    for path in path_list:
        print(path.name, end=" -> ")


def test_city_map():
    config = AreaConfig(0.8)
    graph = config.get_city_map()
    node_list = graph[0]
    edge_list = graph[1]

    city_map = CityMap(node_list, edge_list)
    # city_map.print_matrix()
    # print("------------------------------------")
    path_list = []
    city_map.find_path(CityMap.find_node_by_name("BAR", node_list), CityMap.find_node_by_name("HIGH-TECHNOLOGY", node_list), path_list)
    for path in path_list:
        print(path.name, end=" -> ")


if __name__ == '__main__':
    test_city_map()
