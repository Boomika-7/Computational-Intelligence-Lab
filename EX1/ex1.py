from collections import deque
import heapq

graph={}
def addnode(node):
    if node not in graph.keys():
        graph[node]={}
    else:
        print("\nNode exists")
    print()
    for i in graph.keys():
            print(i,"->",graph[i])

def deletenode(node):
    if node not in graph.keys():
        print("Node does not exists")
    else:
        del graph[node]
        for neighbor in graph.values():
            if node in neighbor:
                del neighbor[node]
    print()
    for i in graph.keys():
        print(i,"->",graph[i])

def addedge(node1,node2,cost):
    if node1 not in graph.keys() or node2 not in graph.keys():
        print("No such node exists")
    else:
        graph[node1][node2] = cost
        graph[node2][node1] = cost
    print()
    for i in graph.keys():
        print(i,"->",graph[i])

def deleteedge(node1,node2):
    if node1 not in graph.keys() or node2 not in graph.keys():
        print("No such node exists")
    else:
        if node2 in graph[node1]:
            del graph[node1][node2]
        if node1 in graph[node2]:
            del graph[node2][node1]
    print()
    for i in graph.keys():
        print(i,"->",graph[i])

def bfs(graph,start,goal):
    visited=[]
    queue=[]
    visited.append(start)
    queue.append(start)
    print("\nPATH:\n")
    while queue:
        node= queue.pop(0)
        print(node,"-> ",end="")
        if node == goal:
            print()
            return None
        for neighbor in graph.get(node, {}):
            if neighbor not in visited:
                queue.append(neighbor)
                visited.append(neighbor)
    print()
    return None

def dfs(graph,start,goal):
    visited = []
    stack = []
    visited.append(start)
    stack.append(start)
    print("\nPATH:\n")
    while stack:
        node=stack.pop()
        print(node,"-> ",end="")
        if node == goal:
            print()
            return None
        neighbors = list(graph.get(node, {}))
        for i in range(len(neighbors) - 1, -1, -1):
            neighbor = neighbors[i]
            if neighbor not in visited:
                stack.append(neighbor)
                visited.append(neighbor)
    print()
    return None

def ucs(graph, start, goal, visited=None, path=None, cost=0, all_paths=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []
    if all_paths is None:
        all_paths = []
    visited.add(start)
    path.append(start)
    if start == goal:
        all_paths.append((list(path), cost))
    neighbors = graph.get(start, {})
    for neighbor, edge_cost in neighbors.items():
        if neighbor not in visited:
            new_cost = cost + edge_cost
            ucs(graph, neighbor, goal, visited, path, new_cost, all_paths)
    visited.remove(start)
    path.pop()

num_nodes = int(input("Enter the number of nodes: "))
for _ in range(num_nodes):
    node = input("Enter a node: ")
    graph[node] = {}
num_edges = int(input("Enter the number of edges: "))
for _ in range(num_edges):
    node1, node2 = input("Enter nodes connected by an edge: ").split()
    cost = float(input("Enter the cost for this edge: "))
    graph[node1][node2] = cost
    graph[node2][node1] = cost
while(True):
    print("\nChoose from the menu:")
    print("1. Add node")
    print("2. Remove node")
    print("3. Add edge")
    print("4. Remove edge")
    print("5. BFS")
    print("6. DFS")
    print("7. UCS")
    print("8. Display graph")
    print("9. Exit")
    print("Enter your choice:")
    ch=int(input())
    if ch==1:
        print("Enter node to add:")
        node1=input()
        addnode(node1)
    elif ch==2:
        print("Enter node to remove:")
        node1=input()
        deletenode(node1)
    elif ch==3:
        print("Enter edges:")
        edge1,edge2=input().split(" ")
        print("Enter cost:")
        cost=int(input())
        addedge(edge1,edge2,cost)
    elif ch==4:
        print("Enter edge to remove:")
        edge1,edge2=input().split(" ")
        deleteedge(edge1,edge2)
    elif ch==5:
        print("Enter start node:")
        choice=input()
        print("Enter goal node:")
        choice2=input()
        bfs(graph, choice,choice2)
    elif ch==6:
        visited = []
        print("Enter start node:")
        choice=input()
        print("Enter goal node:")
        choice2=input()
        dfs(graph,choice,choice2)
    elif ch==7:
        all_paths = []
        print("Enter start node and end node:")
        start,goal=input().split(" ")
        ucs(graph, start, goal, all_paths=all_paths)    
        print("All Paths:")
        for path, cost in all_paths:
            print("Path:", path)
            print("Cost:", cost)
            print()
        optimal_path, optimal_cost = min(all_paths, key=lambda x: x[1])
        print("Optimal Path:")
        print("Path:", optimal_path)
        print("Cost:", optimal_cost)
    elif ch==8:
        print()
        for i in graph.keys():
            print(i,"->",graph[i])
    else:
        break