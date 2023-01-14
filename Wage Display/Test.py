import random

#Always have one element
Five_Element = 1 #100%
for i in range(1000):
    Five_Element = 1
    if (random.randint(1,10) == 1):#10%
        Five_Element = 2
    if (random.randint(1,50) == 1):#  5%
        Five_Element = 3
    if (random.randint(1,100) == 1):#.01 - 1.0%
        Five_Element = 4
    if(random.randint(1,1000) == 1):#.001 - 0.1%
        Five_Element = 5
    print(Five_Element, end= " ")

