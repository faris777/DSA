from collections import deque
graph = {}
graph["you"] = ['alice', 'bob', 'claire']
graph["bob"] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []
#the nodes and edges the connection directional graph
#the direction is one way
#neighbours are determined for you have neighbours alice , bob and claire the direction from you to them. so that
#not vice verse alice not neighbours of you becasue the direction is you to neighbours

def person_is_seller(name):
    return name[-1] == 'm'
def bfs():
    search_queue = deque()
    search_queue +=  graph['you']
    while search_queue:
        person = search_queue.popleft()
        if person_is_seller(person):
            print(person+"is a mango seller")
            return True
        else:
            search_queue += graph[person]
    return False

