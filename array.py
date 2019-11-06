#In the array.py create an array with the following elements in this order
#Ford
#Chrysler
#Dodge
#Ram
#Jeep
#Chevy
#GMC
cars = ['Ford', 'Chrysler', 'Dodge', 'Ram', 'Jeep', 'Chevy', 'GMC']
#print the array to the console
print (cars)
# the length of the array to the console
print ('Array length: ')
print(len(cars))
#Append Buick to the Array -- print the array
cars.append('Buick')
print (cars)
#Print the 4th element in the array (Not index 4)
print ('Element 4: ')
jeep = cars[4]
print (jeep)
#Insert 'Toyota' into element 3 in the array -- print the array
cars.insert(3, 'Toyota')
print (cars)
#Remove element 5 of the array -- print the array (hint look at options for pop())
cars.pop(5)
print (cars)
#Sort the array in ascending order -- print the array
cars.sort()
print (cars)
#Sort the array in descending order -- print the array
cars.sort(reverse=True)
print (cars)
#Store the length of the array in a variable called MyArrayLen
MyArrayLen = str(len(cars))
#Print the message 'The length of my array is ' with MyArrayLen concatenated on the end of the message\
print ('The length of my array is ' + MyArrayLen)