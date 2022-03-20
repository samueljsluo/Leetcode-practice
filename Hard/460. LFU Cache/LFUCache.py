class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None
        
class LinkList:
    def __init__(self):
        self.head = Node(-1, 0)
        self.tail = Node(-1, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
        
    def insertBegin(self, node):
        nxt = self.head.next
        nxt.prev = node
        self.head.next = node
        node.prev = self.head
        node.next = nxt
        self.size+=1
        
    def removeNode(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next
        self.size-=1
        
    def removeTail(self):
        tail = self.tail.prev # the emement before self.tail is last one
        self.removeNode(tail)
        return tail

class LFUCache:
    def __init__(self, capacity: int):
        self.minFreq = 0
        self.capacity = capacity
        self.freq = defaultdict(list) # {1: [key, value, freq]}
        self.cache = {} # {key: {key, value, freq}}
        
    def get(self, key: int) -> int:
        if self.capacity == 0: return -1
        if key not in self.cache: return -1
        return self.update(key, self.cache[key]['val'])
        
    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0: 
            return
        if key in self.cache:
            self.update(key, value)
            return
        if len(self.cache) == self.capacity:
            node = self.freq[self.minFreq].pop(0) # pop least used item
            del self.cache[node['key']]
        self.freq[1].append({'key': key, 'val': value, 'freq': 1}) # new key, append at freq 1
        self.cache[key] = self.freq[1][-1]
        self.minFreq = 1
            
    def update(self, key, value):
        node = self.cache[key]
        freq = node['freq']
        self.freq[freq].remove(node) # since the freq would be update, node should not be at this freq level
        if len(self.freq[freq]) == 0:
            if self.minFreq == freq: self.minFreq+=1 # means all freq in cache is larger than min freq
        self.freq[freq+1].append({'key': key, 'val': value, 'freq': freq+1}) # add node with new freq
        self.cache[key] = self.freq[freq+1][-1]
        return value
    
# class LFUCache:
#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.minFreq = 0
#         self.cache = {}
#         self.freq = defaultdict(OrderedDict)
    
#     def get(self, key: int) -> int:
#         if key not in self.cache:
#             return -1
#         return self.update(key, self.freq[self.cache[key]][key])
        
#     def put(self, key: int, value: int) -> None:
#         if self.capacity <= 0:
#             return
#         if key in self.cache:
#             self.update(key, value)
#             return
#         if len(self.cache) == self.capacity:
#             item = self.freq[self.minFreq].popitem(last=False) # pop least used (FIFO)
#             del self.cache[item[0]]
#         self.cache[key] = 1
#         self.freq[1][key] = value
#         self.minFreq = 1
        
#     def update(self, key, value):
#         freq = self.cache[key]
#         del self.freq[freq][key]
#         if not self.freq[freq]:
#             if freq == self.minFreq:
#                 self.minFreq+=1
#             # del self.freq[freq]
#         self.freq[freq+1][key] = value
#         self.cache[key] = freq+1
#         return value
            
# class LFUCache:
#     def __init__(self, capacity: int):
#         self.cache = {}
#         self.freq = defaultdict(LinkList)
#         self.capacity = capacity
#         self.minFreq = 0
        
#     def get(self, key: int) -> int:
#         if key not in self.cache: return -1
#         return self.update(key, self.cache[key].val)
        
#     def put(self, key: int, value: int) -> None:
#         if self.capacity <= 0: return
#         if key in self.cache:
#             self.update(key, value)
#             return
#         if len(self.cache) == self.capacity:
#             prevTail = self.freq[self.minFreq].removeTail()
#             del self.cache[prevTail.key]
#         node = Node(key, value)
#         self.freq[1].insertBegin(node)
#         self.cache[key] = node
#         self.minFreq = 1
        
#     def update(self, key, value) -> int:
#         node = self.cache[key]
#         node.val = value
#         prevFreq = node.freq
#         node.freq+=1
#         self.freq[prevFreq].removeNode(node)
#         self.freq[node.freq].insertBegin(node)
#         if prevFreq == self.minFreq and self.freq[prevFreq].size == 0:
#             self.minFreq+=1
#         return node.val


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)