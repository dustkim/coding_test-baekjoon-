# baekjoon no.10809

n = int(input())
m = str(input())

total = 0
for idx in range(n):
    total += int(m[idx])

print(total)