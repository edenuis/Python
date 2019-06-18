#Heapsort - Sort numbers in ascending order

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
    
    def isEmpty(self):
        return self.list == []

def heapSort(numbers):
    minheap = minHeap()
    minheap.heapify(numbers)
    new = []
    while not minheap.isEmpty():
        new.append(minheap.extractMin())
    return new

if __name__ == "__main__":
    assert heapSort([1,2,3,4,5]) == [1,2,3,4,5]
    assert heapSort([5,4,3,2,1]) == [1,2,3,4,5]
    assert heapSort([5,2,3,4,4,2,1]) == [1,2,2,3,4,4,5]
    assert heapSort([]) == []
    assert heapSort([-1,23,0,123,5,6,4,-12]) == [-12,-1,0,4,5,6,23,123]
    assert heapSort([10, 7, 8, 9, 1, 5]) == [1,5,7,8,9,10]