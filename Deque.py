class Deque:
    def __init__(self, arraySize = 5):
        """Creates a blank array of specified size"""
        if arraySize < 1:
            size = 20
        self.size = arraySize
        self.headIndex = 0
        self.tailIndex = 0
        self.elementsCount = 0
        self.isWrapped = False
        self.theArray = [0] * arraySize
        #self.printer() #TESTING ONLY, REMOVE FOR SUBMISSION

    def addTail(self, value):
        """Adds a new value to the tail of the queue, wrapping if necessary. Calls resize if necessary"""
        #print(f"Adding value: {value}") #TESTING ONLY, REMOVE FOR SUBMISSION
        #need to determine where next index should be, assigning basic for now with no wrapping or resizing
        if self.elementsCount == self.size: #Call resize () if elementsCount already equal to size
            self.resize()
        if self.elementsCount > 0: #If there are elements in the array, add at current tailIndex +1 (or start wrap)
            if self.tailIndex == (self.size - 1): #If tailIndex = outer bound of the array, start of a wrap is needed
                self.theArray[0] = value
                self.tailIndex = 0
                self.isWrapped = True
            else: #If tail index != outer bound of array, start of a wrap is not needed. Continue with current index increments
                self.theArray[self.tailIndex + 1] = value
                self.tailIndex +=1
        else: #If there are no elements in the array yet, add at index 0
            self.theArray[self.tailIndex] = value
        self.elementsCount +=1
        #self.printer() #TESTING ONLY, REMOVE FOR SUBMISSION


    def removeHead(self):
        """Save the value at the head of the queue, update it to remove access to that value, and return the saved value, wrapping if necessary"""
        headValue = self.theArray[self.headIndex]
        self.elementsCount -=1
        if self.elementsCount == 0: #If head removal results in no items left, reset the key attributes to default
            self.headIndex = 0
            self.tailIndex = 0
            self.isWrapped = False
        else:
            self.headIndex +=1 #Need to add logic for when index would now flip back over to 0 if we were wrapped but at the end of the array bounds
        #print(f"Removed value: {headValue}") #TESTING ONLY, REMOVE FOR SUBMISSION
        #self.printer() #TESTING ONLY, REMOVE FOR SUBMISSION
        return headValue
    
    def dumpArray(self):
        """return an array containing the contents of the array from index 0 to size-1. This is for debugging purposes and to verify that wrapping is working properly."""
        stringArray = ""
        for i in range (0,self.size):
            stringArray = stringArray + str(self.theArray[i]) + " "
        return stringArray



    def isEmpty(self):
        """Returns true when the double ended queue is empty, false otherwise"""
        if self.elementsCount == 0:
            return True
        else:
            return False


    def resize(self):
        """Creates a new array twice as large and copies the elements to it"""            
        if self.isWrapped == True:
            #need to build handling for wrapping, for now just doing basic resize
            self.unWrapQueue()
        self.theArray = self.theArray + ([0] * self.size)
        self.size = self.size * 2

    def unWrapQueue(self):
        """Takes the current array and unwraps it, resetting the headIndex to 0, tailIndex to elementsCount -1, and isWrapped to False"""
        tempArray = [0] * self.size
        tempArrayIndex = 0
        for i in range (self.headIndex, self.size):
            tempArray[tempArrayIndex] = self.theArray[i]
            tempArrayIndex +=1
        for i in range (0, self.tailIndex+1):
            tempArray[tempArrayIndex] = self.theArray[i]
            tempArrayIndex +=1
        self.headIndex = 0
        self.tailIndex = self.elementsCount-1
        self.theArray = tempArray
        self.isWrapped = False
    
    def listQueue(self):
        """Returns a string listing the elements from head to tail"""
        stringArray = ""
        if self.isWrapped == True:
            for i in range (self.headIndex, self.size):
                stringArray = stringArray + str(self.theArray[i]) + " "
            for i in range (0, self.tailIndex+1):
                stringArray = stringArray + str(self.theArray[i]) + " "
        else:
            for i in range (self.headIndex, self.tailIndex+1):
                stringArray = stringArray + str(self.theArray[i]) + " "       
        return stringArray
    
    def addHead(self, value):
        """Adds a new value at the head. Wrapping if necessary. This should not overwrite data that was previously in the queue. If the array is full, call resize() to double the array and copy the data as needed."""
        # First check if array is already full, then if already wrapped, if not wrapped, can just move the head to the max position in the array and call it wrapped.
        if self.elementsCount == self.size: #Call resize() if elementsCount already equal to size
            self.resize()
        if self.elementsCount != 0:
            if self.headIndex == 0: #If headIndex == 0, need to trigger a wrap to append the item. 
                self.headIndex = (self.size - 1) #Array size has already been checked and adjusted if necessary, so we should be free to assign the outer bound to the headIndex without overwritting 
                self.isWrapped = True
            else:
                self.headIndex -=1
        self.theArray[self.headIndex] = value
        self.elementsCount +=1
        self.printer() #TESTING ONLY, REMOVE FOR SUBMISSION
                
                


    
    def removeTail(self):
        """Saves the value at the tail of the queue, updating the queue to remove access to the item at the tail, and returns the saved value. Wrapping if necessary. If the queue is empty, throw an exception.(IndexError)."""
        


#==============================================================================
#FUNCTIONS BELOW FOR TESTING ONLY, REMOVE FOR SUBMISSION
#==============================================================================
    def printer(self): 
        """Prints out the full array and key variables"""
        print("Queue Order: [", end="")
        if self.isWrapped == True:
            for i in range (self.headIndex, self.size):
                print(self.theArray[i], end=", ")
            for i in range (0, self.tailIndex+1):
                print(self.theArray[i], end=", ")
        else:
            for i in range (self.headIndex, self.tailIndex+1):
                print(self.theArray[i], end=", ")
        print("] ", end="")
        print("Index Order: [", end="")
        for i in range(0, self.size):
            print(self.theArray[i], end=", ")
        print("] ", end="")
        print(f"|| headIndex: {self.headIndex} || tailIndex: {self.tailIndex} || elementsCount: {self.elementsCount} || size: {self.size} || isWrapped: {self.isWrapped} ||") 
    
    def checkWrapped(self):
        """Checks position of the head and tail index to see if array is wrapped"""
        if self.tailIndex < self.headIndex:
            return True
        else:
            return False
#==============================================================================
#==============================================================================