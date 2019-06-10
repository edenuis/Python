class minHeap:
    def __init__(self):
        self.list = []
    
    def swap(self, old_idx, new_idx):
        tmp = self.list[new_idx]
        self.list[new_idx] = self.list[old_idx]
        self.list[old_idx] = tmp
        
    def shiftDown(self, idx):
        l = 2*idx + 1
        r = 2*idx + 2
        
        new_idx = idx
        if l < len(self.list) and self.list[new_idx] > self.list[l]:
            new_idx = l
        if r < len(self.list) and self.list[new_idx] > self.list[r]:   
            new_idx = r
        if new_idx != idx:
            self.swap(idx, new_idx)
            idx = new_idx
            self.shiftDown(idx)
        else:
            return
    
    def shiftUp(self, idx):
        if idx == 0:
            return
        parent_idx = (idx - 1)//2
        if self.list[parent_idx] > self.list[idx]:
            self.swap(idx, parent_idx)
            self.shiftUp(parent_idx)
    
    def insert(self, item):
        self.list.append(item)
        self.shiftUp(len(self.list)-1)
    
    def extractMin(self):
        if len(self.list) > 0:
            self.swap(0, len(self.list)-1)
            min_elem = self.list.pop()
            self.shiftDown(0)
        else:
            min_elem = None
        return min_elem
    
    def heapify(self, pre_list):
        if isinstance(pre_list, list):
            self.list = pre_list
            for idx in range(len(pre_list)-1, -1, -1):
                self.shiftDown(idx)
            return True
        return False
    
    def printHeap(self):
        print(self.list)
        
if __name__ == '__main__':
    minheap = minHeap()
    minheap.heapify([5,4,3,2,1])
    minheap.printHeap()
    print("====================")
    minheap.heapify([])
    minheap.printHeap()
    print("====================")
    minheap.heapify([5,4,3])
    minheap.printHeap()
    print("====================")
    minheap.heapify([1,2,3])
    minheap.insert(0)
    minheap.printHeap()
    print("====================")
    minheap = minHeap()
    minheap.insert(1)
    minheap.printHeap()
    print("====================")
    minheap.heapify([5,4,3,2,1])
    minheap.insert(6)
    minheap.insert(7)
    minheap.insert(-1)
    minheap.printHeap() 
    print("====================")
    minheap.heapify([1,2,3])
    minheap.insert(0)
    print(minheap.extractMin())
    minheap.printHeap()
    print("====================")
    minheap = minHeap()
    print(minheap.extractMin())
    minheap.heapify([5,4,3,2,1])
    minheap.printHeap()
    print("====================")
    minheap.insert(6)
    minheap.insert(7)
    minheap.insert(-1)
    minheap.printHeap()
    print(minheap.extractMin())
    minheap.printHeap() 