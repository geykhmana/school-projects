import heapq
from math import radians, sin, cos, sqrt, atan2

def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Earth radius in km
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    return R * c * 0.621371  # Convert to miles

CITIES = {
    'Boston': (42.3601, -71.0589),
    'New York': (40.7128, -74.0060),
    'Philadelphia': (39.9526, -75.1652),
    'Baltimore': (39.2904, -76.6122),
    'Washington': (38.9072, -77.0369),
    'Richmond': (37.5407, -77.4360),
    'Raleigh': (35.7796, -78.6382),
    'Charlotte': (35.2271, -80.8431),
    'Atlanta': (33.7490, -84.3880),
    'Jacksonville': (30.3322, -81.6557),
    'Miami': (25.7617, -80.1918),
    'Portland': (43.6591, -70.2568),
    'New Haven': (41.3083, -72.9279),
    'Stamford': (41.0534, -73.5387),
    'Norfolk': (36.8508, -76.2859),
    'Charleston': (32.7765, -79.9311),
    'Savannah': (32.0809, -81.0912),
    'Orlando': (28.5384, -81.3789),
    'Tampa': (27.9506, -82.4572),
    'Wilmington': (34.2104, -77.8868)
}

ROAD_NETWORKS = {
    'I-95': {
        'type': 'Interstate',
        'sequence': [
            'Miami', 'Jacksonville', 'Savannah', 'Charleston',
            'Wilmington', 'Raleigh', 'Richmond', 'Washington',
            'Baltimore', 'Philadelphia', 'New York', 'New Haven',
            'Boston', 'Portland'
        ]
    },
    'I-85': {
        'type': 'Interstate',
        'sequence': ['Charlotte', 'Atlanta']
    },
    'US-1': {
        'type': 'Highway',
        'sequence': [
            'Miami', 'Jacksonville', 'Savannah', 'Charleston',
            'Wilmington', 'Richmond', 'Washington', 'Baltimore',
            'Philadelphia', 'New York', 'Boston', 'Portland'
        ]
    },
    'Back Roads': {
        'type': 'Back Road',
        'sequence': list(CITIES.keys())
    }
}

class Node:
    def __init__(self, city, parent=None, road=None):
        self.city = city
        self.parent = parent
        self.road = road
        self.g = 0  # Actual cost
        self.h = 0  # Heuristic cost
        self.f = 0  # Total cost

    def __lt__(self, other):
        return self.f < other.f

class AStarGPS:
    def __init__(self):
        self.road_graph = self.build_network()
        self.speed_weights = {'Interstate': 65, 'Highway': 55, 'Back Road': 45}

    def build_network(self):
        graph = {city: [] for city in CITIES}
        
        for road_name, data in ROAD_NETWORKS.items():
            road_type = data['type']
            sequence = data['sequence']
            
            # Connect consecutive cities with actual road name
            for i in range(len(sequence)-1):
                city1 = sequence[i]
                city2 = sequence[i+1]
                dist = haversine(*CITIES[city1], *CITIES[city2])
                
                graph[city1].append((city2, dist, road_name, road_type))
                graph[city2].append((city1, dist, road_name, road_type))
        
        # Add direct back roads between all city pairs as ultimate fallback
        all_cities = list(CITIES.keys())
        for i in range(len(all_cities)):
            for j in range(i+1, len(all_cities)):
                city1 = all_cities[i]
                city2 = all_cities[j]
                dist = haversine(*CITIES[city1], *CITIES[city2])
                graph[city1].append((city2, dist, 'Local Road', 'Back Road'))
                graph[city2].append((city1, dist, 'Local Road', 'Back Road'))
        
        return graph

    def get_allowed_roads(self, distance_category, preference):
        rules = {
            ('Very High', 'speed'): ['Interstate', 'Back Road'],
            ('Very High', 'avoid traffic'): ['Interstate', 'Highway', 'Back Road'],
            ('Very High', 'scenic'): ['Highway', 'Back Road'],
            ('Medium', 'speed'): ['Interstate', 'Highway', 'Back Road'],
            ('Medium', 'avoid traffic'): ['Highway', 'Back Road'],
            ('Medium', 'scenic'): ['Back Road', 'Highway'],
            ('Low', 'speed'): ['Highway', 'Back Road'],
            ('Low', 'avoid traffic'): ['Highway', 'Back Road'],
            ('Low', 'scenic'): ['Back Road']
        }
        return rules[(distance_category, preference)]

    def calculate_distance_category(self, distance):
        if distance > 500: return 'Very High'
        elif 100 <= distance <= 500: return 'Medium'
        else: return 'Low'

    def heuristic(self, current, goal):
        lat1, lon1 = CITIES[current]
        lat2, lon2 = CITIES[goal]
        return haversine(lat1, lon1, lat2, lon2) / 65  # Interstate speed

    def find_path(self, start, end, preference):
        start = start.title()
        end = end.title()
    
        sl_distance = haversine(*CITIES[start], *CITIES[end])
        distance_category = self.calculate_distance_category(sl_distance)
        allowed_roads = self.get_allowed_roads(distance_category, preference)
    
        open_list = []
        closed = set()
        start_node = Node(start)
        start_node.h = self.heuristic(start, end)
        start_node.f = start_node.g + start_node.h
        heapq.heappush(open_list, start_node)
    
        while open_list:
            current = heapq.heappop(open_list)
            closed.add(current.city)
        
            if current.city == end:
                path = []
                roads = []
                while current.parent:
                    path.append(current.city)
                    roads.append(current.road)
                    current = current.parent
                path.append(current.city)  # Add the start city
                path.reverse()
                roads.reverse()
                return path, roads
        
            for neighbor, dist, road_name, road_type in self.road_graph[current.city]:
                if neighbor in closed:
                    continue
            
                if road_type not in allowed_roads:
                    continue
            
                speed = self.speed_weights[road_type]
                new_g = current.g + (dist / speed)
            
                new_node = Node(neighbor, current, road_name)
                new_node.g = new_g
                new_node.h = self.heuristic(neighbor, end)
                new_node.f = new_node.g + new_node.h
            
                heapq.heappush(open_list, new_node)
    
        return None

def main():
    gps = AStarGPS()
    print("Available cities:", ", ".join(CITIES.keys()))
    
    # Enhanced input handling
    def clean_city_input(prompt):
        while True:
            city = input(prompt).split(',')[0].strip().title()
            if city in CITIES:
                return city
            print(f"Invalid city. Available options: {', '.join(CITIES.keys())}")
    
    start = clean_city_input("Enter start city: ")
    end = clean_city_input("Enter end city: ")
    preference = input("Route preference (speed/avoid traffic/scenic): ").strip().lower()

    result = gps.find_path(start, end, preference)
    if result:
        path, roads = result
        print("\nOptimal Route:")
        print(f"Start: {path[0]}")
        for i in range(len(roads)):
            print(f" → Via {roads[i]} → {path[i+1]}")
    else:
        print("No route found (this should never happen!)")

if __name__ == "__main__":
    main()