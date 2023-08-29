# Get input string from user
input_string = input()
numbers = input_string.split("+")
# Convert string to int    
numbers = [int(n) for n in numbers]
# Sort list in descending order  
numbers.sort()  
# Join list into string    
output = "+".join([str(n) for n in numbers])
print(output)