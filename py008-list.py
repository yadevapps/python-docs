fruit_list = ["apple", 'banana', 'orange','banana']
#                0         1        2        3 
#               -4        -3       -2       -1 

print(type(fruit_list))
print(len(fruit_list))      # count item
print(fruit_list)           # all items
print(fruit_list[0:-1])     # all items
print(fruit_list[0])        # first item
print(fruit_list[-1])       # last item
print(fruit_list[1:3])
print(fruit_list[-3:-1])


fruit_list.append("cherry") # add item at last
print(fruit_list)  

fruit_list.insert(1, "kiwi") # add item by index
print(fruit_list)    

fruit_list.pop()             # remove last item
print(fruit_list) 

fruit_list.remove('banana')  # remove first same item
print(fruit_list) 

fruit_list.clear()            # remove all item
print(fruit_list) 


fruit_list = ["apple", 'banana', 'orange','banana']
number_list = [1, 2, 4, 3]

fruit_list.reverse()         # reverse without sort
print(fruit_list) 
number_list.reverse()          
print(number_list) 

fruit_list.sort()            # sort 1,2,... or a,b,...
print(fruit_list) 
number_list.sort()          
print(number_list) 

fruit_list.sort(reverse=True)  # sort and reverse
print(fruit_list) 
number_list.sort(reverse=True)          
print(number_list) 


fruit_list = ["apple", 'banana', 'orange','banana']
copy_fruit_list = fruit_list.copy()   # copy of list
print(copy_fruit_list)

add_list_to_list = fruit_list + number_list
print(add_list_to_list)
