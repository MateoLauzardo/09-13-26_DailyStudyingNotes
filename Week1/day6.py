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


# problem 4

class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next



node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2 
node2.next = node3 



def middle_match(head, val):
	
    current = head 

    # we need to find the middle value 

    slow = current 
    fast = current 

    while fast and fast.next:

        slow = slow.next 
        fast = fast.next.next 

    if slow.value == val:
        return True 

    
    else:
        return False 


print(middle_match(node1, 2))
print(middle_match(node1, 3))



# -------------------------------------


# problem 5 


# determine the node where the cycle starts


class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next


# 1 -> 2 -> 3 -> 4 -> 1.....

n1, n2, n3, n4, = Node(1), Node(2), Node(3), Node(4)
n1.next = n2
n2.next = n3 
n3.next = n4 
n4.next = n2



def get_loop_start(head):
	
    # check is there is a cycle 
    current = head 

    slow = current 
    fast = current 

    while fast and fast.next:

        slow = slow.next 
        fast = fast.next.next 


        # phase 2 — find where the cycle begins
        if fast == slow:
            # change slow we need to keep fast
            slow = head 

            while slow is not fast:
                slow = slow.next
                fast = fast.next
            return slow

    

    return None



print(get_loop_start(n1).value) 


# -------------------------------------


# problem 6 (i get it )


# so it cant be head or last node.
# we need to keep track of the value t othe left of it and right 
# that value must  be Less than and we need a greater than


 
# should we make a prev value attribute in class? 
class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next


n1, n2, n3, n4, n5, n6, n7, n8  = Node(1), Node(2), Node(3), Node(3), Node(3), Node(5), Node(1), Node(3)
n1.next = n2
n2.next = n3 
n3.next = n4 
n4.next = n5
n5.next = n6
n6.next = n7
n7.next = n8




def count_critical_points(head):
    
    # base case: if there is no head or if link list is just head 
    if head is None or head.next is None:
        return 0


    # i need to remeber this tech
    count = 0
    prev = head # keeps tracks of before
    curr = head.next # our current is a value ahead 

    # curr.next is the last value 
    while curr and curr.next:
       
        nxt = curr.next

        is_maxima = curr.value > prev.value and curr.value > nxt.value
        is_minima = curr.value < prev.value and curr.value < nxt.value

        # keep track of how many times there is a crit 
        if is_maxima or is_minima:
            count += 1

        # this is what traverses uys every loop 
        prev = curr
        curr = nxt

    return count
    

print(count_critical_points(n1))


