import random

list1 = sorted([random.randint(1, 99) for i in range(10)])
list2 = sorted([random.randint(1, 99) for i in range(10)])

################################
list3 = list1 + list2

###############################
repetitive = []
for i in list1:
    for j in list2:
        if i == j:
            repetitive.append(i)
#################################
a = set(list3)
####################################
maxi = max(list3)
mini = min(list3)


print(list1)        #1
print(list2)        #2
print(list3)        #1+2
print(repetitive)    # одинаковые числа
print(a)     #множество
print(maxi)
print(mini)
