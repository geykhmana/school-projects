import heapq

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0  # Cost from start to current node
        self.h = 0  # Heuristic cost from current node to goal
        self.f = 0  # Total cost (g + h)

    def __eq__(self, other):
        return self.position == other.position

    def __lt__(self, other):
        return self.f < other.f

def heuristic(a, b):
    """Calculate the Manhattan distance between two points."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star_search(grid, start, goal):
    """Perform A* search on a grid."""
    open_list = []
    closed_list = set()

    start_node = Node(start)
    goal_node = Node(goal)

    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)
        closed_list.add(current_node.position)

        if current_node == goal_node:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # Return reversed path

        neighbors = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # 4-connected grid
        for neighbor in neighbors:
            neighbor_position = (current_node.position[0] + neighbor[0], current_node.position[1] + neighbor[1])

            if (neighbor_position[0] < 0 or neighbor_position[0] >= len(grid) or
                neighbor_position[1] < 0 or neighbor_position[1] >= len(grid[0])):
                continue  # Skip out-of-bounds positions

            if grid[neighbor_position[0]][neighbor_position[1]] == 1:
                continue  # Skip blocked positions

            neighbor_node = Node(neighbor_position, current_node)
            if neighbor_node.position in closed_list:
                continue  # Skip already evaluated nodes

            neighbor_node.g = current_node.g + 1
            neighbor_node.h = heuristic(neighbor_node.position, goal_node.position)
            neighbor_node.f = neighbor_node.g + neighbor_node.h

            if add_to_open(open_list, neighbor_node):
                heapq.heappush(open_list, neighbor_node)

    return None  # No path found

def add_to_open(open_list, neighbor_node):
    """Check if a neighbor should be added to the open list."""
    for node in open_list:
        if neighbor_node == node and neighbor_node.g > node.g:
            return False
    return True

def print_grid(grid, path=None):
    """Print the grid with the path (if provided)."""
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if path and (i, j) in path:
                print("P", end=" ")
            elif grid[i][j] == 1:
                print("#", end=" ")
            else:
                print(".", end=" ")
        print()

def create_grid(rows, cols):
    """Create a grid based on user input."""
    grid = [[0 for _ in range(cols)] for _ in range(rows)]
    print("Enter the grid (0 = free, 1 = blocked):")
    for i in range(rows):
        row = input(f"Row {i} (e.g., 0 0 1 0): ").strip().split()
        for j in range(cols):
            grid[i][j] = int(row[j])
    return grid

def get_position(prompt, grid):
    """Get a valid position from the user."""
    while True:
        pos = input(prompt).strip().split()
        if len(pos) != 2:
            print("Please enter two numbers separated by a space.")
            continue
        x, y = int(pos[0]), int(pos[1])
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            print("Position is out of bounds. Try again.")
        else:
            return (x, y)

# Main program
if __name__ == "__main__":
    # Get grid size
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    # Create the grid
    grid = create_grid(rows, cols)

    # Get start and goal positions
    start = get_position("Enter the start position (row col): ", grid)
    goal = get_position("Enter the goal position (row col): ", grid)

    # Ensure start and goal are not blocked
    if grid[start[0]][start[1]] == 1:
        print("Start position is blocked. Please try again.")
        exit()
    if grid[goal[0]][goal[1]] == 1:
        print("Goal position is blocked. Please try again.")
        exit()

    # Perform A* search
    path = a_star_search(grid, start, goal)
    if path:
        print("Path found:")
        print_grid(grid, path)
    else:
        print("No path found.")