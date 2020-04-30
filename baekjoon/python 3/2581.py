# 문제 링크: https://www.acmicpc.net/problem/2581

import sys
input = sys.stdin.readline

m, n = int(input()), int(input())

s = [False, False] + [True] * (n - 1)
for i in range(2, int(n ** .5) + 1):
  if s[i]:
    for j in range(i * 2, n + 1, i):
      s[j] = False

p = [i for i in range(m, n + 1) if s[i]]
if p == []:
  print(-1)
else:
  print(sum(p))
  print(p[0])