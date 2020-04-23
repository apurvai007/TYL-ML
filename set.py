#INIT A SET WITH VALUES
set1 = {1,2,3}

print(set1)
print(type(set1))

#OUTPUT
"""
{1, 2, 3}
<class 'set'>
"""

set2 = set()
set3 = set()

for i in range(5):
    set2.add(i)

for i in range(3,10):
    set3.add(i)


union = set2 | set3 
intersec = set2 & set3 
diff = set2 - set3

print("set2 = {}".format(set2))
print("set3 = {}".format(set3))

print("set2 Union set3 =  {}".format(union))
print("set2 Intersection set3 =  {}".format(intersec))
print("set2 diffrence set3 =  {}".format(diff))

#OUTPUT
"""
set2 = {0, 1, 2, 3, 4}
set3 = {3, 4, 5, 6, 7, 8, 9}
set2 Union set3 =  {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
set2 Intersection set3 =  {3, 4}
set2 diffrence set3 =  {0, 1, 2}
"""