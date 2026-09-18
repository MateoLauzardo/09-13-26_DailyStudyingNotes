

# so link list is reversed, we want to grab all the value
# from the list and make it into one big number 
# for instance: 2 -> 4 -> 3 (342) would be your answer 


# you would do this for heada and headb ADD both of those answers together 


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


# 2 -> 4 -> 3
# need to convert: 3 -> 4 -> 2
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


    answer = head_a + head_b

    return answer 



def make_into_new_list(x, y):

    num1 = x # 2
    num2 = y # 5

    result1  = str(num1.value) # -> ("243")
    result2  = str(num2.value) # -> ("564")

    # we alreadty have first values saved ^^^ so we need to start next 
    num1 = num1.next
    num2 = num2.next

    while num1:

        result1 = result1 + str(num1.value)

        num1 = num1.next

    
    while num2:
        
        result2 = result2 + str(num2.value)

        num2 = num2.next



    # reversing the string (still string)
    reverse1 = result1[::-1]
    reverse2 = result2[::-1]


    # now we need to convert these to integers
    int_result1 = int(reverse1) 
    int_result2 = int(reverse2) 


    # call function 
    return add_two_numbers(int_result1, int_result2)



def answer():

    final_value = (make_into_new_list(num1, num)) # the literal number 807


    string = str(final_value) 
    reversed_string = string[::-1] 


    int_first_value = int(reversed_string[0]) 
    
    # this should contain values
    head =  Node(int_first_value) 
    current = head



    for ch in reversed_string[1:]:

        # i thought about this but had 0 clue to implement it i see 
        current.next = Node(int(ch))
        current = current.next 


    return head




def print_list(node):
    parts = []
    while node:
        parts.append(str(node.value))
        node = node.next
    print(" -> ".join(parts))


print_list(answer())



