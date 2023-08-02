from collections import defaultdict
class Allocator:

    def __init__(self, n: int):
        self.memory = [None] * n
        self.mem_map = defaultdict(set)
        self.free_memory = len(self.memory)

    def allocate(self, size: int, mID: int) -> int:
        left = right = 0
        original_size = size
        
        while right < len(self.memory) and size != 0:
            if self.memory[right] is not None:
                left = right + 1
                right = left
                size = original_size
            else:
                size -= 1
                right += 1
        
        if size == 0: # means we succesfully have enough memory
            for index in range(left, right):
                self.memory[index] = mID
                self.mem_map[mID].add(index)
                self.free_memory -= 1
            
            return left
        
        return -1

    def free(self, mID: int) -> int:
        freed_memory = 0
        for mem_index in self.mem_map[mID]:
            self.memory[mem_index] = None
            freed_memory += 1
        
        self.mem_map[mID] = set()
        self.free_memory += freed_memory
        return freed_memory

"""

n = size of memory array
- Allocate(size, mID) => block of contiguous memory with an id assigned to it
- Dynamically allocated structure 
-  

Need
- map = { mID: [indices having those mids] }
- array of size n
- 



HashMap
HashSet
List
Queue
Stack
LinkedList
Heap


"""


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)
