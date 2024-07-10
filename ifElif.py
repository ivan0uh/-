first = int(input())
second = int(input())
third = int(input())

if first == second and second == third and third == first :
    print(3)
elif first == second or second == third and third == first :
    print(2)
else:
    print(0)








