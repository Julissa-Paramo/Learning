'''
Julissa Paramo
10/5/23
Arithmetic in Strings
'''
# for loops w strings
# failed lab assignment , only works for integers ! ! !

nums1 = (input('Enter numbers to make three lists!\nList 1: ')) # gets three numbers from user to make each list
nums2 = (input('List 2: '))
nums3 = (input('List 3: '))


listA = nums1.split() # splits numbers at each space, makes a list
listB = nums2.split()
listC = nums3.split()


list1 = list(map(int, listA)) # converts list of strings ['1','2','3'] into a list of integers [1,2,3]
list2 = list(map(int, listB))
list3 = list(map(int, listC))


list1, list2, list3 = [6.3,8.4,9.2], [-1.2,7.6,3.2], [4.1,-2.1,9.6]

sum = 0 

if len(list1) == len(list2) == len(list3): # checks if all three lists are the same length
       
	for num in range (len(list1)) : # goes through each index in the list

		sum = sum + list1[num] * list2[num] - list3[num] # each calculation made for each idex gets added together

	print(sum) 

else:
									
	print('All lists are required to be the same length.') # if they're not the same length there's an error



