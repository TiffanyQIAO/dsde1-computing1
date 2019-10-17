#number Datatypes
>>> 9/3
3.0
>>> 9//2
4
>>> 9//3
3
>>> 9/3.
3.0

#importing modules
>>> import math
>>> print(math.e)
2.718281828459045

>>> import math
>>> r=5
>>> area=(math.pi)*r**2
>>> print(area)
78.53981633974483
乘號一定要寫

# solve the following equations
#y = 2 + sin(x) when x = 3
>>> import math
>>> x=3
>>> y=2+math.sin(x)
>>> print(y)
2.1411200080598674

#y = log(x-3) + 2(x+4) when x = 5
import math
>>> x=5
>>> y=math.log10(x-3)+2*(x+4)
>>> print(y)
18.30102999566398
留意log 的base要寫在log之後

#number guessing game
import random
guess = input("Please input a number in range 1-6:")
random = random.randint(1,6)
print (guess==random)

>>> import random as r
>>> random=r.randint(1,20)

>>> from random import randint
>>> random=randint(1,30)