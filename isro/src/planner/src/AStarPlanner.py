import heapq

class Node:
    def __init__(self, x, y, cost):
        self.x = x
        self.y = y
        self.cost = cost  # cost of traversing this node
        self.g = float('inf')  # cost from start node to current node
        self.h = 0  # heuristic cost from current node to end node
        self.f = float('inf')  # total cost (g + h)
        self.parent = None

    def __lt__(self, other):
        return self.f < other.f

class AStarPlanner:
    def heuristic(self, node, goal):
        return ((node.x - goal.x) ** 2 + (node.y - goal.y) ** 2) ** 0.5

    def search(self, grid, start, end):
        open_list = []
        closed_list = set()

        start_node = Node(start[0], start[1], grid[start[0]][start[1]])
        end_node = Node(end[0], end[1], grid[end[0]][end[1]])

        start_node.g = 0
        start_node.h = self.heuristic(start_node, end_node)
        start_node.f = start_node.g + start_node.h

        heapq.heappush(open_list, start_node)
        count=0

        while open_list:
            current_node = heapq.heappop(open_list)
            count+=1
            if current_node.x == end_node.x and current_node.y == end_node.y:
                path = []
                while current_node:
                    path.append((current_node.x, current_node.y))
                    current_node = current_node.parent
                return path[::-1]

            closed_list.add((current_node.x, current_node.y))

            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                neighbor_x, neighbor_y = current_node.x + dx, current_node.y + dy

                if (
                    0 <= neighbor_x < len(grid) and
                    0 <= neighbor_y < len(grid[0]) and
                    (neighbor_x, neighbor_y) not in closed_list
                ):
                    neighbor_cost = grid[neighbor_x][neighbor_y]
                    neighbor_node = Node(neighbor_x, neighbor_y, neighbor_cost)
                    neighbor_node.g = current_node.g + neighbor_cost
                    neighbor_node.h = self.heuristic(neighbor_node, end_node)
                    neighbor_node.f = neighbor_node.g + neighbor_node.h
                    neighbor_node.parent = current_node

                    heapq.heappush(open_list, neighbor_node)

        return None  # No path found