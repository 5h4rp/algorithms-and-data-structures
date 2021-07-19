class Node:
    def __init__(self):
        self.data = None
        self.next = None
    
    def setData(self,data):
        self.data = data
    
    def getData(self,data):
        return self.data

    def setNext(self,data):
        self.next = next

    def getNext(self,next):
        return self.next

    def hasNext(self):
        return self.next != None


class linkedList():
    def __init__(self):
        self.head = None
        self.length = 0
    
    def listLength(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.next
        return count

    def listPrint(self):
        current = self.head
        while current != None:
            print(current.data)
            current = current.next

    def insertAtBeginning(self,data):
        newNode = Node()
        newNode.data = data

        if self.length == 0:
            self.head = newNode
        else:
            current = self.head
            self.head = newNode
            newNode.next = current
        self.length += 1

    def insertAtEnd(self,data):
        newNode = Node()
        newNode.data = data
        current = self.head
        while current.next != None:
            current = current.next
        current.next = newNode
        self.length += 1

    def insertAtGivenPosition(self,pos,data):
        if pos > self.length or pos < 0:
            # print(self.length)
            return None
        else:
            if pos == 0:
                self.insertAtBeginning(data)
                # print(2)
            else:
                if pos == self.length + 1:
                    self.insertAtEnd(data)
                    # print(3)
                else:
                    # print(4)
                    newNode = Node()
                    newNode.data = data
                    count = 1
                    current = self.head
                    while count < (pos-1):
                        count += 1
                        current = current.next
                    newNode.next = current.next
                    current.next = newNode
                    self.length += 1

    def reverse(self): 
        prev = None
        current = self.head 
        while(current is not None): 
            next = current.next
            # print(f'P: {prev} | C: {current} | N:{next}')
            current.next = prev 
            prev = current 
            current = next
        self.head = prev

    def reverseUtil(self, curr, prev):   
        # If last node mark it head 
        if curr.next is None : 
            self.head = curr  
              
            # Update next to prev node 
            curr.next = prev 
            return 
          
        # Save curr.next node for recursive call 
        next = curr.next
  
        # And update next  
        curr.next = prev 
      
        self.reverseUtil(next, curr)  
  
    # This function mainly calls reverseUtil() 
    # with previous as None 
    def recreverse(self): 
        if self.head is None: 
            return 
        self.reverseUtil(self.head, None) 

    def deleteFromBeg(self):
        if self.length == 0:
            print('list empty')
        else:
            self.head = self.head.next
            self.length -= 1

    def deleteLastNode(self):
        if self.length == 0:
            print('listempty')
        else:
            current = self.head
            prev = self.head
            while current.next != None:
                prev = current
                current = current.next
            prev.next = None
            self.length -= 1

    def deleteWithNode(self, node):
        if self.length==0:
            raise ValueError("List is Empty")
        else:
            current = self.head
            previous = None
            found = False

            while not found:
                if current == node:
                    found = True
                elif current is None:
                    raise ValueError("Node not in list")
                else:
                    previous = current
                    current = current.next
        if previous is None:
            self.head = current.next
        else:
            previous = current.next
        self.length -= 1

    def deleteWithValue(self, value):
        current = self.head
        previous = self.head
        while current.next != None or current.data != value:
            
            if current.data == value:
                # print(current.data, ' ', previous.data)
                previous.next = current.next
                self.length -= 1
                return
            else:
                # print(f'else {current.data}')
                previous = current
                current = current.next
            # raise ValueError("Value not found in list")

    def deleteAtPos(self, pos):
        count = 0
        current = self.head
        previous = self.head
        if pos > self.length or pos < 0:
            raise ValueError("The pos does'nt exist.")
        else:
            while current.next != None or count < pos:
                count = count + 1
                if count == pos:
                    previous = current.next
                    self.length -= 1
                    return
                else:
                    previous = current
                    current = current.next



#####################################################################################################
weekdays = linkedList()
weekdays.insertAtBeginning("Monday")
weekdays.insertAtEnd("Tuesday")
weekdays.insertAtEnd("Thursday")
weekdays.insertAtBeginning("Sunday")
weekdays.insertAtGivenPosition(4,"Wednesday")

weekdays.listPrint()
print('----------')
# weekdays.deleteFromBeg()
# weekdays.listPrint()
# print('----------')
# weekdays.deleteLastNode()
# weekdays.listPrint()
# weekdays.listPrint()
# print(weekdays.listLength())
# weekdays.recreverse()
# weekdays.listPrint()

weekdays.deleteWithValue('Wednesday')
# print('------')
weekdays.listPrint()
