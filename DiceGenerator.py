import random

six = ("[------]\n"
      "[ 0  0 ]\n"
      "[ 0  0 ]\n"
      "[ 0  0 ]\n"
      "[------]")

five=("[------]\n"
      "[ 0  0 ]\n"
      "[  0   ]\n"
      "[ 0  0 ]\n"
      "[------]")
four=("[------]\n"
      "[ 0  0 ]\n"
      "[      ]\n"
      "[ 0  0 ]\n"
      "[------]")

three =("[------]\n"
      "[ 0  0 ]\n"
      "[      ]\n"
      "[  0   ]\n"
      "[------]")

two = ("[------]\n"
      "[       ]\n"
      "[   0   ]\n"
      "[   0   ]\n"
      "[------]")

one = ("[------]\n"
      "[      ]\n"
      "[   0  ]\n"
      "[      ]\n"
      "[------]")
numbers = [one,two,three,four,five,six]
while(True):
    x=input("Press Enter to roll a new dice or any key + enter to stop")
    if(x):
        print("Thanks for playing")
        break
    y = random.randint(0,5)
    print(y+1)
    # if(y>6 or y<=0):
    #     y = random.randint(0, 5)
    print(numbers[y])
