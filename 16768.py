##16768
##1<=N<=100, wide = 10, 1<= K <= 10N
##기능별로 세가지 함수가 필요
##count_cell(x,y,v): x,y를 기준으로 값이 v인 인접셀의 좌표를 tuple 리스트로 return
##delete_cell(target): target에서 전달받은 리스트의 길이가 3이상이라면 해당 좌표를 0으로 치환
##drop()
import sys
sys.setrecursionlimit(100000)
N, K = map(int, input().split())
board = []
dx, dy = [1,-1,0,0], [0,0,1,-1]

def count_cell(x,y,v):
    result = [(x,y)]
    visited[x][y] = 1
    for i in range(4):
        xx, yy = x+dx[i], y+dy[i]
        if xx<0 or xx>=N or yy<0 or yy>=10:
            continue
        if board[xx][yy] == v and not visited[xx][yy]:
            result.extend(count_cell(xx,yy,v))
    return result

def delete_cell(arr):
    for x, y in arr:
        board[x][y] = 0
    
def drop():
    for i in range(10):
        for j in range(N-1,0,-1):
            if board[j][i] == 0:
                for k in range(j-1,-1,-1):
                    if board[k][i]:
                        board[j][i], board[k][i] = board[k][i], 0
                        break

for _ in range(N):
    board.append(list(map(int, input())))

while True:
    target = []
    visited = [[0] * 10 for _ in range(N)]
    for i in range(N):
        for j in range(10):
            if board[i][j] > 0:
                dfs = count_cell(i,j,board[i][j])
                if len(dfs) >= K:
                    target.extend(dfs)
    delete_cell(target)
    drop()

    if not target:
        break
for i in board:
    line =''
    for j in i:
        line += str(j)
    print(line)
