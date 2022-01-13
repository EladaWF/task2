# https://codeforces.com/problemset/problem/750/A
a, b = map(int, input().split())
b = 240 - b
s = 0
count = 0
for i in range(1, a + 1):
    if count + (5 * i) > b:
        break
    else:
        count += i * 5
        s += 1
print(s)
