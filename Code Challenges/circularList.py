#Challenge: You run an e-commerce website and want to record the last N order 
#           ids in a log. Implement a data structure to accomplish this, with 
#           the following API:
#           record(order_id): adds the order_id to the log
#           get_last(i): gets the ith last element from the log. i is 
#                        guaranteed to be smaller than or equal to N.
#           You should be as efficient with time and space as possible.

class CircularList:
    def __init__(self, n=5):
        self.max_size = n
        self.list = []
        self.index = 0
        
    def record(self, order_id):
        if len(self.list) < self.max_size:
            self.list.append(order_id)
        else:
            self.list[self.index] = order_id
            
        self.index += 1
        if self.index == self.max_size:
            self.index %= self.max_size
            
    def get_last(self, i):
        if len(self.list) < self.max_size and i < len(self.list):
            return self.list[len(self.list)-i]
        elif len(self.list) == self.max_size:
            return self.list[(self.index-i)%self.max_size]
    
    def printList(self):
        print(self.list, self.index)
    
if __name__ == '__main__':
    cl = CircularList(5)
    #Case: no wrap around, max size not reached
    cl.record(1)
    cl.record(2)
    cl.record(3)
    cl.record(4)
    print(cl.get_last(3)) #returns 2
    print("=====================")
    #Case: no wrap around, max size hit
    cl.record(1)
    cl.record(2)
    cl.record(3)
    cl.record(4)
    cl.record(5)
    print(cl.get_last(3)) #returns 3
    print("=====================")
    #Case: wrap around
    cl = CircularList(5)
    cl.record(1)
    cl.record(2)
    cl.record(3)
    cl.record(4)
    cl.record(5)
    cl.record(6)
    print(cl.get_last(3)) #returns 4