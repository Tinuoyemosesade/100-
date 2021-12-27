import random

choice = input('What is your choice? Head or Tail  type 1 for head, and 0 for tail')

number = random.randint(0, 1)

if number == 1:

 print ('You have got Head!')

else:

 print ('You got a Tail!')

