

# # Session 2 


# # Problem 1: 
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"Node({self.value!r})"


# just check if value in node1 is the same as node4 
node1 = Node("num1")
node2 = Node("num2")
node3 = Node("num3")
node4 = Node("num1")

node1.next = node2 
node2.next = node3 
node3.next = node4 




# that answer my question LOL
def is_circular(head):

    # this is actually num1 
    actual_head = head 

    # this is actually at the 2nd value 
    current = head
    current = current.next  


    # loop WHILE current has a value 
    while current:

        if current.value == actual_head.value:
            return True

        # # updates the counter 
        current = current.next
    

        
    return False   
    

# num1 -> num2 -> num3 -> num1
print(is_circular(node1))

# ------------------------------------



# problem 2 (i get it)

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"Node({self.value!r})"


node1 = Node("num1")
node2 = Node("num2")
node3 = Node("num3")
node4 = Node("num4")

# makes into cycle
node1.next = node2 
node2.next = node3 
node3.next = node4 
node4.next = node2 



# floy algo to find entrence node. 
def find_entrance_node(head, meeting_point):
    
    slow = head
    fast = meeting_point

    while slow is not fast:
        slow = slow.next
        fast = fast.next

    return slow



def find_last_node_in_cycle(head):
	

    slow = head 
    fast = head


    while fast and fast.next:

        slow = slow.next 
        fast = fast.next.next
        

        # if there is a cycle do something in here 
        if slow == fast:

            # you pass in head and slow NOT fast 
            entrance = find_entrance_node(head, slow)

            # this is your entrence point 
            current = entrance

            
            while current.next is not entrance:
                current = current.next

            return current.value


    return False







print(find_last_node_in_cycle(node1))




# ------------------------------------


# problem 3 

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"Node({self.value!r})"


node1 = Node(1)
node2 = Node(4)
node3 = Node(3)
node4 = Node(2)
node5 = Node(5)
node6 = Node(2)

node1.next = node2 
node2.next = node3 
node3.next = node4 
node4.next = node5 
node5.next = node6  




def partition(head, val):
    
    # dummy heads so we don't special-case the first append
    before_head = Node(None)
    after_head = Node(None)

    before = before_head
    after = after_head


    current = head

    while current:
        
        # puts everything LESS to the left
        if current.value < val:
            before.next = current
            before = current
        
        # puts everything else to the right including val itself 
        else:
            after.next = current
            after = current

        # current always updating 
        current = current.next


    # critical: cut the old tail, or you'll keep a stale link
    after.next = None

    # stitch the two lists together
    before.next = after_head.next

    return before_head.next




def show(head):
    parts = []
    while head:
        parts.append(str(head.value))
        head = head.next
    print(" -> ".join(parts))

show(partition(node1, 3))   # 1 -> 2 -> 2 -> 4 -> 3 -> 5



# ------------------------------------



class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


num1 = Node(1)   # head of the list
num2 = Node(0)
num3 = Node(1)

num1.next = num2 
num2.next = num3 



def binary_to_int(head):
	
    # first thing is count how many digits is head / gets ur n

    current = head

    count = 0 

    # this segment counts how many digits 
    while current:

        count += 1
        current = current.next 


    # reset current value (count value is back to 1)
    current = head 

    answer = 0 


    # # with those n do the math (current x 2^n)
    # do this three times 
    while current:

        # starts with this cuz intead of 0,1,2 -> its 1,2,3 (this sorts that issue out)        
        count -= 1
        answer += current.value * 2 ** count # instead of math.pow() which gues us a double, doing ** makes a while number 

        current = current.next  


    return answer 



int_num = binary_to_int(num1)
# 101 in binary is 5
print(int_num)  # Output: 5



# ------------------------------------


# so link list is reversed, we want to grab all the value
# from the list and make it into one big number 
# for instance: 2 -> 4 -> 3 (342) would be your answer 


# you would do this for heada and headb ADD both of those answers together 


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


# 2 -> 4 -> 4
num1 = Node(2)   
num2 = Node(4)
num3 = Node(3)
num1.next = num2 
num2.next = num3 


# 5 -> 6 -> 4
num = Node(5)
num_two = Node(6)
num_three = Node(4)

num.next = num_two
num_two.next = num_three





def add_two_numbers(head_a, head_b):




    return sum1, sum2 






# i would call add_two_numbers function TWICE for the list, grabs those values in a whole dif functon to make into an ew list 
def make_into_new_list():

    sum1, sum2 = add_two_numbers(num1, num)
   
    
