## you pick a number between 1 and 99
## computer guesses one number, if it's greater enter k, if less enter b
## and if it's the right number enter d.

import random
min_g = 1
max_g = 99
geussed_num = random.randint(min_g,max_g)
print(geussed_num)
while (1):
    situation = input()
    if situation == 'b' :
           max_g = geussed_num
           geussed_num = random.randint(min_g,max_g)
           print(geussed_num)
    if situation == 'k' :
            min_g = geussed_num
            geussed_num = random.randint(min_g,max_g)
            print(geussed_num)
    if situation == 'd' :
          break


