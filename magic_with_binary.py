# magic version 1
''' 
Please submit a pull request how this program can be improved
using the computational ideas of, where appropriate, with
annotation (comments):
- abstraction
- decomposition
- pattern recognition
- algorithm design
You may add it as a new version below instead of replacing the
existing program so that it can be easily compared with the 
original version. There can be more than one good suggestion. :)
'''

print("Do you believe I can read your mind?")
print("Think of a number between 1 t0 31")

magic = 0
table1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]
print("Is your number here?")
print(table1)
ans = input("y/n: ")
if ans == 'y':
  magic += 1

table2 = [2, 3, 6, 7, 10, 11, 14, 15, 18, 19, 22, 23, 26, 27, 30, 31]
print("Is your number here?")
print(table2)
ans = input("y/n: ")
if ans == 'y':
  magic += 2

table3 = [4, 5, 6, 7, 12, 13, 14, 15, 20, 21, 22, 23, 28, 29, 30, 31]
print("Is your number here?")
print(table3)
ans = input("y/n: ")
if ans == 'y':
  magic += 4

table4 = [8, 9, 10, 11, 12, 13, 14, 15, 24, 25, 26, 27, 28, 29, 30, 31]
print("Is your number here?")
print(table4)
ans = input("y/n: ")
if ans == 'y':
  magic += 8

table5 = [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
print("Is your number here?")
print(table5)
ans = input("y/n: ")
if ans == 'y':
  magic += 16

print("Your number is:", magic)


# magic version 2
