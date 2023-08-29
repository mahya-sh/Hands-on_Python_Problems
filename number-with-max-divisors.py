##find the number with max divisors among the entered numbers.
## print both the number and the number of divisors it has.
def dividend(number):
      count = 0
      for i in range(1,number+1):
            if (number%i) == 0:
                  count +=1
      return count
    
divisors = []
nums = []
for i in range (20):
      num = int(input())
      nums.append(num)

max_divisors = 0
max_divisor_number = 0

for num in nums:
    divisors = dividend(num)
    if divisors > max_divisors:
        max_divisors = divisors
        max_divisor_number = num
    elif divisors == max_divisors:
        if num > max_divisor_number:
            max_divisor_number = num



print(max_divisor_number, max_divisors)

