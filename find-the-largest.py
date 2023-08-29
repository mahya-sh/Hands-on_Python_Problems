## find the largest number, if -1 has been entered, stop getting input.
age = int(input())
oldest = age
while age != -1:
      if oldest < age:
            oldest = age
      age = int(input())
print(oldest)