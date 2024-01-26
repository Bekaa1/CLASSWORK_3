#CLASSWORK 3
#1
'''a= int(input())
n=[]
for i in range(1,a+1):
    n.append(i)
print(n)'''

#2
'''import string
def alphabet(n):
    alphabet = string.ascii_lowercase[:n]
    print(list(alphabet))
n=int(input())
print(alphabet(n))'''

#3
'''numbers1 = [1, 2, 3]
numbers2 = [6]
numbers3 = [7, 8, 9, 10, 11, 12, 13]
numbers1*=2
numbers2*=9
print(numbers1+numbers2+numbers3)'''

#4
'''n=int(input())
num=[int(input()) for i in range(n)]
res=num[::2]
print(res)'''

#5
'''n = int(input())
num = [input() for i in range(n)]
k = int(input())
for i in num:
    if 1 <= k <= len(i):
        print(i[k - 1], end="")'''

#6
'''n = int(input())
num = [input() for i in range(n)]
b=[]
for i in num:
    for j in i:
        b.append(j)
print(b)'''

#7
'''n = int(input())
num = [input() for i in range(n)]
k = int(input())
podhodyashiy = [input() for i in range(k)]
for s in num:
    if all(q.lower() in s.lower() for q in podhodyashiy):
        print(s)'''

#8
'''n = int(input())
num = [int(input()) for i in range(n)]
for s in num:
    if s<0:
        print(s)
for s in num:
    if s==0:
        print(s)
for s in num:
    if s>0:
        print(s)'''

#list and tuples
#1
'''list=[]
for i in range(5):
    list.append(input())
print(list)'''

#2
'''a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(a[2:7])'''

#3
'''num1 = float(input())
num2 = float(input())
num3 = float(input())
tuple = (num1, num2, num3)
print(tuple)'''

#4
'''list=['ffff', 'ffff', 'dnvsjk']
list.append(input())
list.pop(0)
list.sort()
print(list)'''

#5
'''n=int(input())
list=[1,2,3,4,5,9]
for i in list:
    if i==n:
        print("yes")'''

#6
'''list=[1,2,3,4,5,9]
list.reverse()
print(list)'''

#7
'''my_tuple = (1, 'apple', 3.14, True)
var1, var2, var3, var4 = my_tuple
print(var1)
print(var2)
print(var3)
print(var4)'''

#8
'''user = input()
numbers = [float(x) for x in user.split()]
if numbers:
    max = max(numbers)
    min = min(numbers)
    print(max)
    print(min)'''

#9
'''list1_input = input()
list1 = [x.strip() for x in list1_input.split()]
list2_input = input()
list2 = [x.strip() for x in list2_input.split()]
result_list = list1 + list2
print(result_list)'''

#10
'''a=int(input())
list=[int(input()) for i in range(a)]
print(tuple(list))'''

#11
'''set={int(input()) for i in range(3)}
print(set)'''

#12
'''import random
set1={random.randrange(1, 100) for i in range(5)}
set2={random.randrange(1, 100) for i in range(5)}
print(f"Set1 is {set1}")
print(f"Set2 is {set2}")
print(set1.union(set2))
print(set1.difference(set2))
print(set1.intersection(set2))
print(set1.symmetric_difference(set2))'''

#13
'''dict = {}
for i in range(3):
    key = input("Enter a key: ")
    value = input("Enter a value: ")
    dict[key] = value
print("Dictionary:", dict)'''

#14
'''dict = {}
key=input("enter key:")
for i in range(3):
    key = input("Enter a key: ")
    value = input("Enter a value: ")
    dict[key] = value
print(f"the value of key is {dict[key]}" if key in dict else " no such value" )'''

#15
'''user_input = input("Enter a string: ")
frequency_dict = {}
for char in user_input:
    frequency_dict[char] = frequency_dict.get(char, 0) + 1
for char, frequency in frequency_dict.items():
    print(f"Character '{char}' occurs {frequency} times.")'''

#16
'''import random
my_set = set(random.randrange(1, 20) for i in range(10))
print(my_set)
print("Number is in set" if int(input("Enter a number: ")) in my_set else "Number is not in set")'''


#17
'''my_dict = {"color": "red", "size": "medium", "price": 100, "fruit": "apple"}
for key, value in my_dict.items():
    print(my_dict[key])'''

#18
'''first_dict = {"color": "red", "size": "medium", "price": 100, "fruit": "apple"}
second_dict = {"university": "AITU", "language": "english", "country": "Kazakhstan", "name": "Bekaaa"}
for key, value in first_dict.items():
             second_dict[key] = value
print(second_dict)'''

#19
'''my_dict = {'a': 1, 'b': 2, 'c': 3}
remove = input("Enter the key to remove: ")
if remove in my_dict:
    del my_dict[remove]
    print(f"Key '{remove}' removed successfully.")
else:
    print(f"Key '{remove}' not found in the dictionary.")
print("Updated Dictionary:", my_dict)'''

#20
'''user_input = input("Enter a list of elements separated by spaces: ")
input_list = user_input.split()
unique_elements_set = set(input_list)
print("Unique Elements:", unique_elements_set)'''


