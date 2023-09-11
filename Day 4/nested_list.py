#Nested Lists 

nested_list = [1, [2, 3], 4, [5, 6, [7, 8]]]
element0 = nested_list[2]
element1 = nested_list[1][1]
element2 = nested_list[3][2]
element3 = nested_list[3][2][0]  
""" 
element = nested_list[4][0] 
#is not a seperate element it is nested within 3rd element so this will arise error
""" 


print(element0)
print(element1)
print(element2)
print(element3)
