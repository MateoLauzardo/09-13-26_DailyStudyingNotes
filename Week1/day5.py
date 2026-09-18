

# Problem 1: Week 6

def print_linked_list(head):

    string = ""

    # while there are values in head.next 
    while head.next != None:
        
        string += head.value + " -> "

        head = head.next 

    # adding last value
    string = string + head.value


    print(string)


print_linked_list(node_1)



class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node4.next = node3
node3.next = node2
node2.next = node1 
# node 1 next is not specificed so is just None 

def print_list(head):
    current = head
    while current is not None:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

print_list(node4)   # 4 -> 3 -> 2 -> 1 -> None


# -------------------------------------

# Problem #2

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next



node1 = Node(3)
node2 = Node(1)
node3 = Node(2)
node4 = Node(1)

node1.next = node2 
node2.next = node3 
node3.next = node4 


# the amount of time that value pops up 
def count_element(head, val):

    counter = 0 

    while head is not None:
        if head.value == val:
            counter += 1 
        head = head.next 

    return counter 


print(count_element(node1, 1))
        

# -------------------------------------


# Problem #3 ->  remove the tail of a singly linked list

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next



node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.next = node2 
node2.next = node3 
node3.next = node4 


        
# Helper function to print the linked list
def print_list(node):
    current = node
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()



# I have a bug! 
def remove_tail(head):

    # If the list is empty, return None (this is correct)
    if head is None: 
        return None
    
    # If there's only one node, removing it leaves the list empty
    if head.next is None: 
        return None 
		
	# this is correct
    current = head
    
    while current.next.next is not None:
        current = current.next

    current.next = None
        
    
    return head


print_list(node1)              # 1 -> 2 -> 3 -> 4
remove_tail(node1)
print_list(node1)              # 1 -> 2 -> 3



# -------------------------------------


