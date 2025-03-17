#linked list
from node import Node
class LinkedList():
    def __init__(self):
        self.head = None
    #Methods
    #Append()Method
    #Create a node w data to append
    #if LL is empty, put node at head
    #Else search through our list and advance until we find the end. At end set the last pointer to reference the node created
    #STR
    def __str__(self):
        print_out = ""
        if self.head == None:
            print_out += "The list is empty!"
        else:
            #traverse the list
            traverser = self.head
            while traverser != None:
                print_out += str(traverser.data) +"\n"
                traverser = traverser.next
        return print_out
    def __contains__ (self, target):
        traverser = self.head
        while traverser != None:
            if traverser.data == target:
                return True
            traverser = traverser.next
        return False


    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            searcher = self.head
            while searcher.next != None:
                searcher = searcher.next
            searcher.next = new_node

    #preprend method 
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert(self, data, position):
        if position == 0:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head
            while temp.next != None and position > 1:
                temp = temp.next
                position -= 1
            new_node = Node(data)
            new_node.next = temp.next
            temp.next = new_node
        
    def remove(self, data):
        node_removal = Node(data)
        while node_removal.data != None:
            if node_removal == self.head:
                node_removal = self.head
                node_removal.next = None
            else:
                node_removal.next
            return print("the node had been removed")



    
traverser = self.head
        while traverser != None:
            if traverser.data == target:
                return True
            traverser = traverser.next