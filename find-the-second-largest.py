##find the largest and second largest number, if -1 has entered,
##getting input is over.
numbers = []
while True:
      num = int(input())
      if num == -1:
            break
      numbers.append(num)

numbers.sort()
largest = numbers[-1]
second_largest = numbers[-2]
print(largest, second_largest)




