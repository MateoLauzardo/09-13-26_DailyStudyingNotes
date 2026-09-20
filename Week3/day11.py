# # what it wants us to do is we are given two values
# # wants us to reverse all the values from m to n


# this is right 
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

node1.next = node2
node2.next = node3
node3.next = node4 
node4.next = node5 



# we need to traverse through link list till we get to index m and add those values
# to a list until we hit index n, reverse them and than create new list 
def reverse_between(head, m, n):
	
    current = head

    array1 = []
    array2 = []
    index = 1

    # this while loop should be going the whole way 
    while current:
        
        # if index is not at m add to array 1 ( [1] )
        if index < m:
            array1.append(current.value)
            index += 1
            current = current.next 


        # else add to array 2 ( [2,3,4,5] )
        else:
            array2.append(current.value)
            index += 1
            current = current.next 


    
    # reverse (done)
    reversed_array = array2[::-1]

    # combine (done)
    combined = array1 + reversed_array


    # make new link list and return
    first_value = combined[0]
    head = Node(first_value) # turns int to node

    current = head

    for values in combined[1::]:
        
        current.next = Node(values)
        current = current.next


    return head


        

node = reverse_between(node1, 2, 5)

def print_list(node):
    parts = []
    while node:
        parts.append(str(node.value))
        node = node.next
    print(" -> ".join(parts))
    
print_list(node)

 

#------------------------------------

# # Week 7

def repeat_hello(n):
	if n > 0:
		print("Hello")
		repeat_hello(n - 1)
		
repeat_hello(5)


def repeat_hello_iterative(z):

    for x in range(z):

        print("hello")


print(repeat_hello_iterative(5))


# Compare: The recursive functions calls itself and not having to do in range
# or a for loop. I know that the Big 0 notation is faster when using recussion
# for task like this. 




# 
def factorial(n):
    print(f"going down, n={n}")
    if n == 0:
        return 1
    answer = n * factorial(n - 1) # and 2-1 is 1 factorial(1) was just solved right before 
    print(f"coming back up, n={n}, answer={answer}")
    return answer


print(factorial(5))
        
    
# thats why the next is 6 BECAUSE factorial(2) was solved before and answer is 2
# so if n is 3 and needs to mult w fact(2) the answer to that is 2 so 3*2 is 6
