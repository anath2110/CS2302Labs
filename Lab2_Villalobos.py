'''
    Code created and modified by: Ismael Villalobos
    Lab Assignment2
    Node Functions provided by: Olac Fuentes
'''

# Node Functions
import random

class Node(object):
    # Constructor
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

def PrintNodes(N):
    if N != None:
        print(N.item, end=' ')
        PrintNodes(N.next)

def PrintNodesReverse(N):
    if N != None:
        PrintNodesReverse(N.next)
        print(N.item, end=' ')

# List Functions
class List(object):
    # Constructor
    def __init__(self):
        self.head = None
        self.tail = None
        self.Len = 0

def IsEmpty(L):
    return L.head == None

def Append(L, x):
    # Inserts x at end of list L
    if IsEmpty(L):
        L.head = Node(x)
        L.tail = L.head
        L.Len += 1
    else:
        L.tail.next = Node(x)
        L.tail = L.tail.next
        L.Len += 1

def Prepend(L, x):
    ##inserts x at begingin of list L
    if IsEmpty(L):
        L.head = Node(x)
        L.tail = L.head
        L.Len += 1
    else:
        L.head = Node(x, L.head)
        L.Len += 1

def Print(L):
    # Prints list L's items in order using a loop
    temp = L.head
    while temp is not None:
        print(temp.item, end=' ')
        temp = temp.next
    print()  # New line


def Remove(L, x):
    # Removes x from list L
    # It does nothing if x is not in L
    if L.head == None:
        return
    if L.head.item == x:
        if L.head == L.tail:  # x is the only element in list
            L.head = None
            L.tail = None
            L.Len -= 1
        else:
            L.head = L.head.next
            L.Len_ = 1
    else:
        # Find x
        temp = L.head
        while temp.next != None and temp.next.item != x:
            temp = temp.next
        if temp.next != None:  # x was found
            if temp.next == L.tail:  # x is the last node
                L.tail = temp
                L.tail.next = None
                L.Len -= 1
            else:
                temp.next = temp.next.next
                L.Len -= 1
def Copy(L):
    # copies list L into a new list with the same values
    copy = List()
    temp = L.head
    while temp != None:
        Append(copy, temp.item)
        t = temp.next
    return copy

def bubbleSort(L):
    if IsEmpty(L):
        return None
    counter = 0
    temp = L.head
    isSwap = False #base case
    while temp.next is not None:
        if temp.item > temp.next.item:
            hold = temp.item
            temp.item = temp.next.item # swapping with temp holders
            temp.next.item = hold
            isSwap = True
        temp = temp.next
        counter +=1
    if isSwap == True:
        bubbleSort(L)

def quickSort(L):
    if L.Len >1:
        pivot = L.head.item

        L1 = List()
        L2 = List()
        temp = L.head.next

        while temp != None:
            if temp.item < pivot:
                Append(L1, temp.item)
            else:
                Append(L2,temp.item)
            temp = temp.next
        quickSort(L1)
        quickSort(L2)

        if IsEmpty(L1):
            Append(L1,pivot)
        else:
            Prepend(L2,pivot)

        if IsEmpty(L1):
            L.head = L2.head
            L.tail = L2.tail
        else:
            L1.tail.next = L2.head
            L.head = L1.head
            L.tail = L2.tail

def mergeSort(L):
    if L.Len >1:
        L1 = List()
        L2 = List()
        temp = L.head
        for i in range(L.Len//2):
            Append(L1,temp.item)
            temp = temp.next
        while temp != None:
            Append(L2, temp.item)
            temp = temp.next
        mergeSort(L1)
        mergeSort(L2)

        tempList(L)
        mergeList(L,L1,L2)

def mergeList(L,L1,L2):
    #combies sorted lists into one list
    temp1 = L1.head
    temp2 = L2.head
    while temp1 != None and temp2 != None:
        if temp1.item < temp2.item:
            Append(L,temp1.item)
            temp1=temp1.next
        else:
            Append(L,temp2.item)
            temp2 = temp2.next

        if temp1 is None:
            while temp2 != None:
                Append(L,temp2.item)
                temp2 =temp2.next
        if temp2 is None:
            while temp1 != None:
                Append(L,temp1.item)
                temp1 =temp1.next

def tempList(L):
    L.head = None
    L.tail = None
    L.Len = 0

def modifiedQuickSort(L,median):
    if L.Len <=1:
        return L.head.item
    pivot = L.head.item
    L1 = List()
    L2 = List()
    temp = L.head.next #remove pivot

    while temp != None:
        if temp.item < pivot:
            Append(L1,temp.item)
        else:
            Append(L2,temp.item)
        temp = temp.next
    if L1.Len > median:
        #median is in first list
        return modifiedQuickSort(L1,median)
    elif(L1.Len ==0 and median==0):
        return pivot
    elif(L1==median):
        return pivot
    else:
        return modifiedQuickSort(L2,median-L1.Len-1)

def Copy(L):
    copy = List()
    temp = L.head
    while temp != None:
        Append(copy,temp.item)
        temp = temp.next
    return copy

def medianBS(L):
    C = Copy(L)
    bubbleSort(C)
    temp = C.head
    for i in range(C.Len//2):
        temp = temp.next
    return temp.item

def medianQS(L):
    C = Copy(L)
    quickSort(C)
    temp = C.head
    for i in range(C.Len//2):
        temp = temp.next
    return temp.item

def medianMS(L):
    C = Copy(L)
    mergeSort(C)
    temp = C.head
    for i in range(C.Len//2):
        temp = temp.next
    return temp.item
def medianModded(L):
    C = Copy(L)
    print(modifiedQuickSort(C,C.Len//2))

List1 = List()
for j in range(5):
    t=random.randrange(100)
    Append(List1,t)
print('Unsorted List')
Print(List1)

bubbleSort(List1)
print('Sorted using Bubble Sort')
Print(List1)
print('Median using Bubbl Sort is ', medianBS(List1))
quickSort(List1)
print('Sorted using Quick Sort')
Print(List1)
print('Median using Quick Sort is ', medianQS(List1))

mergeSort(List1)
print('Sorted using Merge Sort')
Print(List1)
print('Median using Merge Sort is ', medianMS(List1))
print('Median using Modified Quick Sort is ', end =' ')
medianModded(List1)

