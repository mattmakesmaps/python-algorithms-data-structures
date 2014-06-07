class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.curentSize = 0

    def percUp(self, i):
    """Perform required amounts of
    swaps to properly position a newly
    inserted item within the heap structure"""
    # i // 2 yields the parent node 
    while i // 2 > 0: # while we haven't reached the top of heap.
        # if new value is less then its parent
        if self.heapList[i] < self.heapList[i // 2]:
        	tmp = self.heapList[i // 2] # get parent val
        	self.heapList[i // 2] = self.heapList[i] #populate par with cur
        	self.heapList[i] = tmp # populate cur with par
        i = i // 2 # setup for inspection of par (now populated with cur)

    def insert(self, k):
        self.heapList.append(k) 
        self.curentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def percDown(self, i):
        while (i * 2) <= self.currentSize:
        	mc = self.minChild(i)
        	if self.heapList[i] > self.heapList[mc]:
        		tmp = self.heapList[i]
        		self.heapList[i] = self.heapList[mc]
        		self.heapList[mc] = tmp
        	i = mc

    def minChild(self, i):
    	# Return the smallest child of a given parent
    	# node i.
    	# check if we are at the end of the heap 
    	if i * 2 + 1 > self.currentSize:
    		return i * 2
    	else:
    		if self.heapList[i*2] < self.heapList[i*2+1]:
    			return i * 2
    		else:
    			return i * 2 + 1

    def delMin(self):
    	# Get the min val; the top of the heap.
    	retval = self.heapList[1]
        # Perform the swap with last element.
    	self.heapList[1] = self.heapList[self.currentSize]
    	self.currentSize = self.currentSize - 1
    	# Actually remove last element, now at top of heap.
    	self.heapList.pop()
    	# Now push last element down into proper order.
    	self.percDown(1)
    	return retVal

    def buildHeap(self, alist):
    	i = len(alist) // 2 # the index of the last item
    	self.currentSize = len(alist)
    	self.heapList = [0] + alist[:]
    	# iterate through the keys, using percDown to sort
    	# the heap.
    	while (i > 0):
    		self.percDown(i)
    		i = i - 1