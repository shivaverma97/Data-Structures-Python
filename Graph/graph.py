class Graph():
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for strt, end in edges:
            if strt in self.graph_dict:
                self.graph_dict[strt].append(end)
            else:
                self.graph_dict[strt] = [end]
        print('Available flights',self.graph_dict)

    def get_paths(self, start, end, path=[]):
        path = path + [start]

        if start == end :
            return  [path]

        if start not in self.graph_dict :
            return []

        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_paths(node,end,path)
                for p in new_paths:
                    paths.append(p)

        return paths

    def get_shortest_path(self, start, end, path=[]):
        path = path + [start]

        if start == end :
            return path
        if start not in self.graph_dict :
            return None
        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path)
                if sp :
                    if shortest_path is None or len(shortest_path) > len(sp):
                        shortest_path = sp
        return  shortest_path

if __name__ == '__main__':
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]
    route_list = Graph(routes)
    print(route_list.get_paths('Toronto','mumbai'))
    print(route_list.get_paths('Paris','Toronto'))
    print(route_list.get_shortest_path('Paris','Toronto'))