list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_2 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(list_1)

print("Length of List 1:", len(list_1)) #Length of list_1 

print("First value of List 2:", list_2[0]) #First value of list_2

print("Third value of List 1:", list_1[2]) #Third value of list_1

print("Last value of List 2:", list_2[-1]) #Last value of list_2

add_list = list_1 + list_2
print(add_list) #Add two list

print(list_1[1:]) #Access second to rest value list_1

print(list_2[0::2]) #Here, this will skip 1 value from the list


print("Reverse value of list 1:", list_1[::-1]) #Accessing values reversely


print("Reverse value of list 1:", list_1[::-2]) #Accessing values reversely


#Checking membership of list_1
if 3 in list_1:
  print("first: The value '3' is present in the list.")
else:
  print("first: empty")
print("")
if 12 in list_1:
  print("second: The value '12' is present in the list.")
else:
  print("second: empty")


finding_value = list_1.index(7)
print("finding_value:", finding_value)


#Replace a value in list
list_1[3] = 14
print(list_1)