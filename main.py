#14620
#6<=N<=10, 0<=G<=200
#heap으로 풀어보려했으나 값이 겹치는 경우가 생겨 전체 탐색으로 구현
# import heapq


# N = int(input())
# M = [list(map(int, input().split())) for _ in range(N)]
# occupied = [[False] * N for _ in range(N)]
# heap = []
# dx, dy = [0,1,0,-1], [1,0,-1,0]
# for i in range(1, N-1):
#     for j in range(1, N-1):
#         lease = M[i][j]
#         for n in range(4):
#             ii, jj = i + dx[n], j + dy[n]
#             lease += M[ii][jj]
#         heapq.heappush(heap, (lease, i, j))

# cnt = 0
# result = 0
# while heap:
#     l, x, y = heapq.heappop(heap)
#     p = True
#     for n in range(4):
#         xx, yy = x + dx[n], y + dy[n]
#         if occupied[xx][yy]:
#             p = False
#             break
#     if p:
#         occupied[x][y] = True
#         result += l
#         for n in range(4):
#             xx, yy = x + dx[n], y + dy[n]
#             occupied[xx][yy] = True
#         cnt += 1
#     print(l,x,y)
#     for i in occupied:
#         print(i)
#     if cnt == 3:
#         break
        
# print(result)

N = int(input())
M = [list(map(int, input().split())) for _ in range(N)]
values = []
dx, dy = [0,1,0,-1], [1,0,-1,0]
ans = 10000
def ck(lst):
    occupied = [[False] * N for _ in range(N)]
    for t in lst:
        l, x, y = t
        if occupied[x][y]:
            return False
        else:
            occupied[x][y] = True
            for n in range(4):
                ii, jj = x + dx[n], y + dy[n]
                if occupied[ii][jj]:
                    return False
                else:
                    occupied[ii][jj] = True
        print('occupied')
        for i in occupied:
            print(i)
    return True
    


for i in range(1, N-1):
    for j in range(1, N-1):
        lease = M[i][j]
        for n in range(4):
            ii, jj = i + dx[n], j + dy[n]
            lease += M[ii][jj]
        values.append((lease, i, j))
print(values)
leng = len(values)
for i in range(leng-2):
    a = values[i]
    for j in range(i+1, leng-1):
        b = values[j]
        for k in range(j+1, leng):
            c = values[k]
            print(a,b,c)
            if ck([a,b,c]):
                print(a[0]+b[0]+c[0])
                ans = min(ans, (a[0]+b[0]+c[0]))
                

print(ans)