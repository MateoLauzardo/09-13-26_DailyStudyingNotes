

# Question 1:
# greater than 1 and can ONLY be divided by 1 

def is_prime(n):
    
    # must be greater than 1 
    if n < 2:
        return False

    # loops through each number starting at 2 ending to the number we are looking for 
    for i in range(2, n):
        # found a divisor -> not prime (if n is disvisble by i)
        if n % i == 0:
            return False

        
    return True 


print(is_prime(5))
print(is_prime(12))
print(is_prime(9))


# ----------------------------------------------


# Question 2:
def reverse_list(lst):
    return lst[::-1]





print(reverse_list([1, 2, 3, 4, 5]))



# ----------------------------------------------

# # question 3:
def reverse_list(lst):

    # time complex of o(k)
    # Create a new reversed list
    reversed_lst = lst[::-1]

    # time complx: 0(n)
    # Copy the elements back into the original list
    for i in range(len(lst)):
        lst[i] = reversed_lst[i]


# # answer: First one cuz notation is 0(k)



# ----------------------------------------------


# question 4:

def sort_array_by_parity(nums):
    
    even = []
    odd = []
    answer = []

    # flls up these list
    for num in nums:

        if num % 2 == 0:
            even.append(num)

        else:
            odd.append(num)



    # for even
    for num in even:
        answer.append(num)


    for num in odd:
        answer.append(num)

    
    return answer 

        


nums = [3,1,2,4]
nums2 = [0]
print(sort_array_by_parity(nums))
print(sort_array_by_parity(nums2))



# ----------------------------------------------


def first_palindrome(words):

# o(n) notation
# two pointer tech

    # ["abc","car","ada","racecar","cool"]
    for word in words:
        left, right = 0, len(word) - 1
        is_palindrome = True

        while left <= right:
            
            if word[left] != word[right]:
                is_palindrome = False
                break
            
            
            left += 1
            right -= 1


        if is_palindrome:
            return word

    return ""



# # o(k) notation
# # OR do it with slciing 
def first_palindrome(words):

    for word in words:
        if word == word[::-1]:
            return word 

    return ""

        


        

words = ["abc","car","ada","racecar","cool"]
palindrome1 = first_palindrome(words)
print(palindrome1)

words2 = ["abc","racecar","cool"]
palindrome2 = first_palindrome(words2)
print(palindrome2)

words3 = ["abc", "def", "ghi"]
palindrome3 = first_palindrome(words3)
print(palindrome3)




# ----------------------------------------------


# question 5 

# We need to do this in 0(1) MEANING we can NOT do for loop

def remove_duplicates(nums):


    new_list = [] 

    




nums = [1,1,2,3,4,4,4,5]
print(nums)
print(remove_duplicates(nums))
print(nums) # same list



# ----------------------------------------------

# Week 5: question 1, 2, 3


class Pokemon:
    
    def __init__(self, name, types, evolution = None):
        self.name = name
        self.types = types
        self.is_caught = False
        self.evolution = evolution # starts as None but whatever is in parameters equals itself 


    def print_pokemon(self):
        print({
            "name": self.name,   
            "types": self.types, 
            "is_caught": self.is_caught 
        })

    
    def catch(self):
        self.is_caught = True

    
    def choose(self):
        if self.is_caught == True:
            print(self.name + " I Choose you!")
        else:
            print(self.name + " Is wild! Catch them if you can!")


    def add_type(self, new_type):
        self.types.append(new_type)



#     # printing a list or dict containing your objects, and 
#     # the REPL echoing a value → always __repr__.
#     # used for instances in class 
    def __repr__(self):
        return f"{self.name}"
    

    
    
def get_evolutionary_line(starter_pokemon):
    
    answer = []
    current = starter_pokemon

    # i get it now its a while loop 
    while current is not None:
        answer.append(current)
        current = current.evolution # changes value each time 

    return answer




def get_by_type(my_pokemon, pokemon_type):
 
    answer = []

    # so my_pokemon is a list of instances of class 
    for pokemon in my_pokemon:

        # its this that is messing it up 
        if pokemon_type in pokemon.types:
            answer.append(pokemon)

    
    return answer 




    
# instnace of class and calling method to print 
my_pokemon = Pokemon("rattata", ["Normal"]) # types is an array  because thats what you plugged into 
my_pokemon.print_pokemon()
my_pokemon.choose() # print false
my_pokemon.catch() # changes to is caught to True
my_pokemon.choose() # print true 



# a ton  of pokemon instances -> these have access to pokemon class methods
charizard = Pokemon("Charizard", ["fire", "flying"])
charmeleon = Pokemon("Charmeleon", ["fire"], charizard)
charmander = Pokemon("Charmander", ["fire"], charmeleon)

charmander_list = get_evolutionary_line(charmander)
print(charmander_list)

charmeleon_list = get_evolutionary_line(charmeleon)
print(charmeleon_list)

charizard_list = get_evolutionary_line(charizard)
print(charizard_list)



# ----------------------------------------------


# Question 9


class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

    
node_1 = Node('mario')
node_2 = Node('luigi')
node_3 = Node('Wario')
node_4 = Node('Toad ')

node_1.next = node_2
node_2.next = node_3
node_3.next = node_4

print(node_1.value, "->", node_1.next.value)
print(node_2.value, "->", node_2.next.value)
print(node_3.value, "->", node_3.next.value)
print(node_4.value, "->", node_4.next)


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
