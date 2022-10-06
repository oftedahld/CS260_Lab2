class Deque:
    def __init__(self, arraySize = 20):
        """Creates a blank array of specified size"""
        if arraySize < 1:
            size = 20
        self.size = arraySize
        self.headIndex = 0
        self.tailIndex = 0
        self.elementsCount = 0
        self.isWrapped = False
        self.theArray = [0] * arraySize
        self.printer() #TESTING ONLY, REMOVE FOR SUBMISSION

    def addTail(self, value):
        """Adds a new value to the tail of the queue, wrapping if necessary. Calls resize if necessary"""
        #need to determine where next index should be, assigning basic for now with no wrapping or resizing
        newCount = self.elementsCount + 1
        if newCount > self.size: #call resize () if the new count of elements will be greater than the array size
            self.resize()
        if self.elementsCount > 0: #If there are elements in the array, add at current tailIndex +1
            self.theArray[self.tailIndex + 1] = value
            self.tailIndex +=1
        else: #If there are elements in the array, add at index 0
            self.theArray[self.tailIndex] = value
        self.elementsCount +=1
        self.printer() #TESTING ONLY, REMOVE FOR SUBMISSION


    def removeHead(self):
        """Save the value at the head of the queue, update it to remove access to that value, and return the saved value, wrapping if necessary"""

    def isEmpty(self):
        """Returns true when the double ended queue is empty, false otherwise"""
        if self.elementsCount == 0:
            return True
        else:
            return False


    def resize(self):
        """Creates a new array twice as large and copies the elements to it"""


#==============================================================================
#FUNCTIONS BELOW FOR TESTING ONLY, REMOVE FOR SUBMISSION
#==============================================================================
    def printer(self): 
        """Prints out the full array and key variables"""
        print(self.theArray)
        print(f"|| Head index: {self.headIndex} || Tail index: {self.tailIndex} || Elements count: {self.elementsCount} ||") 
    
    def checkWrapped(self):
        """Checks position of the head and tail index to see if array is wrapped"""
        if self.tailIndex < self.headIndex:
            return True
        else:
            return False
#==============================================================================
#==============================================================================