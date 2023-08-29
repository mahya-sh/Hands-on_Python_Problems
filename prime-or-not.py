##python code to detect if a number ia a prime one or not.
##number is given as an input, the result is printed as output.
n = int(input())
i = 1
if n > 1 : ## 1 is not a prime number
      for i in range(2, n+1):
            if ((n%i == 0) & (i != n)):
                  print("not prime")
                  break
            else:
                  if (i == n):
                        print("prime")
                        break
else:
     print("not prime") 