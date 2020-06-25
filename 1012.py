## 1012
## T, 1<=M<=50, 1<=N<=50, 1<=K<=2500, 0<=X<=M-1, 0<=Y<=N-1
## recursive limit을 해제해줘야함

import sys
sys.setrecursionlimit(100000)



dx, dy = [1,-1,0,0], [0,0,1,-1]

def adjacent(y,x):
    farm[y][x] = 0
    for i in range(4):
        yy, xx = y+dy[i], x+dx[i]
        if xx < 0 or xx >= len(farm[0]) or yy < 0 or yy >= len(farm):
            continue
        if farm[yy][xx]:
            adjacent(yy,xx)

for t in range(int(input())):
    # print('test', t)
    result = 0
    m, n, k = map(int, input().split())
    farm = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        farm[y][x] = 1

    for i in range(n):
        for j in range(m):
            if farm[i][j]:
                adjacent(i,j)
                # print('cycle', result+1)
                # for k in farm:
                #     print(k)
                result += 1
    print(result)