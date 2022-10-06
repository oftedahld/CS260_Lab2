#
#  main.cpp
#  deque
#
#  Created by jim bailey on 4/8/21.
#

from Deque import Deque


def main():
    # uncomment functions to run tests

    queueTest()
    # resizeTest()
    # listTest()
    # addHeadTest()
    # removeTailTest()
    # revQueueTest()
    # mixTest()
    # thinkTest()
    

def queueTest():
    NUM_QUEUE = 8
    queue = Deque()
    num = 0

    print("Testing basic queue, addTail, removeHead, isEmpty\n")

    print("Adding eight odd integers to FIFO")
    for index in range(NUM_QUEUE):
        queue.addTail(2 * num + 1)
        num += 1

    print("Expected 1 3 5 7 9 11 13 15")
    print("Actually ", end="")
    for index in range(NUM_QUEUE):
        print(queue.removeHead(), end=" ")
    print()

    print("\nFIFO should be empty")
    if queue.isEmpty():
        print("FIFO is empty")
    else:
        print("FIFO is not empty")

    print("\nDone with basic test\n")


def resizeTest():
    NUM_RESIZE = 8
    NUM_RESIZE_EXTRA = 4
    resize = Deque(NUM_RESIZE)
    num = 0

    print("Testing resizing queue, addTail, removeHead\n")

    print("Adding eight odd integers to FIFO")
    for index in range(NUM_RESIZE):
        resize.addTail(2 * num + 1)
        num += 1

    print("Removing four to cause wrap")
    print("Expected 1 3 5 7")
    print("Actually ", end="")
    for index in range(NUM_RESIZE_EXTRA):
        print(resize.removeHead(), end = " ")
    print()

    print("\nAdding four more for wrapping")
    for index in range(NUM_RESIZE_EXTRA):
        resize.addTail(2 * num + 1)
        num += 1

    print("Dumping the array ")
    print("Expected 17 19 21 23 9 11 13 15")
    print("Actually " + resize.dumpArray())

    print("\nNow adding eight more")
    for index in range(NUM_RESIZE):
        resize.addTail(2 * num + 1)
        num += 1

    print("Expected 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39")
    print("Actually " + resize.dumpArray())

    print("\nDone with resize test\n")


def listTest():
    NUM_LIST = 7
    NUM_LIST_EXTRA = 5
    list = Deque(NUM_LIST+1)
    listValues = 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78
    num = 0

    print("Testing listQueue, addTail, removeHead\n")

    print("Adding seven values to FIFO")
    for index in range(NUM_LIST):
        list.addTail(listValues[num])
        num += 1

    print("Testing list")
    print("Expected 1 3 6 10 15 21 28")
    print("Actually " + list.listQueue())

    print("\nRemoving five to cause wrap")
    print("Expected 1 3 6 10 15")
    print("Actually ", end="")
    for index in range(NUM_LIST_EXTRA):
        print(list.removeHead(), end = " ")
    print()

    print("\nAdding five more for wrapping")
    for index in range(NUM_LIST_EXTRA):
        list.addTail(listValues[num])
        num += 1

    print("Testing list after wrap")
    print("Expected 21 28 36 45 55 66 78")
    print("Actually " + list.listQueue())

    print("\nDone with testing listQueue\n")


def addHeadTest():
    NUM_HEAD = 7
    head = Deque()
    headValues = 3, 5, 7, 11, 13, 17, 19

    print("Testing addHead\n")

    print("Adding seven values to head")
    for index in range(NUM_HEAD):
        head.addHead(headValues[index])


    print("Now removing from head")
    print("Expected 19 17 13 11 7 5 3")
    print("Actually ", end="")
    for index in range(NUM_HEAD):
        print(head.removeHead(), end = " ")
    print()

    print("\nDone with testing addHead\n")


def removeTailTest():
    NUM_TAIL = 6
    tail = Deque()
    tailValues = 1, 2, 4, 8, 16, 32

    print("Testing removeTail\n")

    print("Adding six values to tail")
    for index in range(NUM_TAIL):
        tail.addTail(tailValues[index])

    print("Now removing from tail")
    print("Expected 32 16 8 4 2 1")
    print("Actually ", end="")
    for index in range(NUM_TAIL):
        print(tail.removeTail(), end = " ")
    print()

    print("\nDone with testing removeTail\n")


def revQueueTest():
    NUM_REV_QUEUE = 8
    NUM_REV_ADD = 4
    revQueue = Deque(NUM_REV_QUEUE)
    num = 0

    print("Testing reverse FIFO, addHead, removeTail, isEmpty\n")

    print("Adding eight even integers to FIFO")
    for index in range(NUM_REV_QUEUE):
        revQueue.addHead(2 * num)
        num += 1

    print("Removing four before wrapping")

    print("Expected 0 2 4 6")
    print("Actually ", end="")
    for index in range(NUM_REV_ADD):
        print(revQueue.removeTail(), end = " ")
    print()

    print("\nAdding four more to force wrap")
    for index in range(NUM_REV_ADD):
        revQueue.addHead(2 * num)
        num += 1

    print("Now dumping array")
    print("Expected 14 12 10 8 22 20 18 16")
    print("Actually " + revQueue.dumpArray())

    print("\nNow adding eight more to force resize")
    for index in range(NUM_REV_QUEUE):
        revQueue.addHead(2 * num)
        num += 1

    print("Now dumping array")
    print("Expected 22 20 18 16 14 12 10 8 38 36 34 32 30 28 26 24")
    print("Actually " + revQueue.dumpArray())

    print("\nNow using removeTail to empty array")
    print("Expected 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38")
    print("Actually ", end="")
    for index in range(NUM_REV_QUEUE*2):
        print(revQueue.removeTail(), end = " ")
    print()

    print("\nFIFO should be empty")
    if revQueue.isEmpty():
        print("FIFO is empty")
    else:
        print("FIFO is not empty")

    print("\nDone with reverse FIFO tests\n")


def mixTest():
    NUM_MIX = 3
    mixQueue = Deque(NUM_MIX * 2)
    num = 0
    
    print("Testing reverse mix of adds and removes\n")

    print("Adding three odd integers to tail")
    for index in range(NUM_MIX):
        mixQueue.addTail(2 * num + 1)
        num += 1

    print("Adding three even numbers to head")
    for index in range(NUM_MIX):
        mixQueue.addHead(2 * num)
        num += 1

    print("Dumping array ")
    print("Expected 1 3 5 10 8 6")
    print("Actually " + mixQueue.dumpArray())

    print("\nAdding three more to tail to force resize")
    for index in range(NUM_MIX):
        mixQueue.addTail(2 * num + 1)
        num += 1

    print("Adding three more to head to fill array")
    for index in range(NUM_MIX):
        mixQueue.addHead(2 * num)
        num += 1

    print("Dumping array ")
    print("Expected 10 8 6 1 3 5 13 15 17 22 20 18")
    print("Actually " + mixQueue.dumpArray())

    print("\nNow removing from Tail ")
    print("Expected 17 15 13 5 3 1")
    print("Actually ", end="")
    for index in range(NUM_MIX*2):
        print(mixQueue.removeTail(), end = " ")
    print()

    print("\nNow removing from Head ")
    print("Expected 22 20 18 10 8 6")
    print("Actually ", end="")
    for index in range(NUM_MIX*2):
        print(mixQueue.removeHead(), end = " ")
    print()

    print("\nCalling removeHead from empty FIFO")
    try:
        mixQueue.removeHead()
        print("Failed to throw exception")
    except IndexError:
        print("Caught IndexError")
    except:
        print("Caught something else ")

    print("\nCalling removeTail from empty FIFO")
    try:
        mixQueue.removeTail()
        print("Failed to throw exception")
    except IndexError:
        print("Caught IndexError ")

    except:
        print("Caught something else ")

    print("\nDone with mixed tests\n")


def thinkTest():
    print("This location is for you to add your solution to the thinking problem")

    NUM_THINK = 5
    thinkValues = 2, 3, 5, 7, 11



    print("Values in reverse order should be 11 7 5 3 2")
    print("\nDone with thinking test\n")


if __name__ == "__main__":
    main()