# 1st program
print((9 ** 0.5) * 5)

# 2nd program
print(9.99 > 9.98 and 1000 != 1001)

#/3rd program
a = 1234;
b = 5678;

c = a % 1000 // 10;
d = b % 1000 // 10;

print(c+d)

#4th program
f = 13.42;
g = 42.13;

s = f * 100; #1342.0
h = g * 100; #4213.0

l = s % 10000 // 100; #13.0
o = s % 100; #42.0

k = h % 10000 // 100; #42.0
i = h % 100; #13.0

print(l == k or o == i or l == i or k == o)