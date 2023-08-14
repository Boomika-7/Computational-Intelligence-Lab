import heapq

def astar(graph, start, goal, heuristic):
    open_set = [(0, start, [start])]
    g_scores = {start: 0}
    print("\n***********************SOLUTION***********************")
    print("\nOPEN_SET =", open_set)
    while open_set:
        f_score, current_node, current_path = heapq.heappop(open_set)
        if current_node!=goal:
            print("\nExploring:", current_node)
            print()
        if current_node == goal:
            print("\nGoal reached:", current_node)
            print("\nOptimal Path:", "->".join(current_path))
            print("Path Cost:",f_score,"\n")
            return
        for neighbor, cost in graph[current_node]:
            tentative_g_score = g_scores[current_node] + cost
            if neighbor not in g_scores or tentative_g_score < g_scores[neighbor]:
                print("Path:",current_path+[neighbor])
                g_scores[neighbor] = tentative_g_score
                h_score = float(heuristic[neighbor])
                f_score = tentative_g_score + h_score
                print("Cost:",tentative_g_score,"+",h_score,"=",f_score)
                heapq.heappush(open_set, (f_score, neighbor, current_path + [neighbor]))
        open_set.sort()   
        print("\nOPEN_SET =", open_set)
    return None

graph = {}
heuristic = {}
num_nodes = int(input("Enter the number of nodes: "))
for _ in range(num_nodes):
    node = input("Enter a node: ")
    graph[node] = []
    heuristic[node] = float(input("Enter the heuristic value for node {}: ".format(node)))
num_edges = int(input("Enter the number of edges: "))
for _ in range(num_edges):
    node1, node2 = input("Enter nodes connected by an edge: ").split()
    cost = float(input("Enter the cost for this edge: "))
    graph[node1].append((node2, cost))
    graph[node2].append((node1, cost))
print("\nGraph:")
for node, neighbors in graph.items():
    print(node, "->", neighbors)
print()
start = input("Enter the start node: ")
goal = input("Enter the goal node: ")
astar(graph, start, goal, heuristic)