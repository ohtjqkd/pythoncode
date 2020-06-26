##12100
##스와이프방향을 생각하자
##시간 복잡도에서는 각 벡터를 구현하는것이 좋지만 시간내에 구현해야하는 경우 방향을 고정시키고 테이블을 변화시키는게 빠름

N = int(input())
Board = [list(map(int,input().split())) for _ in range(N)]


def rotate90(N, board):
    newboard = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            newboard[j][N-i-1] = board[i][j]
    return newboard

def swipe(lst,N):
    new_list = [i for i in lst if i]
    for i in range(len(new_list)-1):
        if new_list[i] == new_list[i+1]:
            new_list[i] *= 2
            new_list[i+1] = 0
    new_list = [i for i in new_list if i]
    return new_list + [0] * (N-len(new_list))

def dfs(N, board, n):
    ret = max([max(i) for i in board])
    if n == 0:
        return ret
    for _ in range(4):
        swiped = [swipe(i,N) for i in board]
        if board != swiped:
            ret = max(dfs(N, swiped, n-1), ret)
        board = rotate90(N, board)
    return ret

print(dfs(N, Board, 5))
