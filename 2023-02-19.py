'''https://school.programmers.co.kr/learn/courses/30/lessons/154540?language=python3'''

# def solution(maps):
#     answer = []
#     pastDict = {}
#     for m in maps:
#       current = [(index, food) for index, food in enumerate(list(m)) if food != 'X']
#       currentDict = dict(current)
      
#       count = 0
#       for _, food in current:
#         count += int(food)
      
#       if not pastDict:
#         pastDict = dict(current)
#         answer.append(count)
#       else:
#         num = answer[-1]
#         for index, food in currentDict.items():
#           if index in pastDict:
#             answer[-1] += sum(map(int, currentDict.values()))
#             break
#         if (num == answer[-1]):
#           for index, food in currentDict.items():
#             answer.append(int(food))
#         pastDict = currentDict
#     answer.sort()
#     if all(element == 0 for element in answer):
#       answer = [-1]
#     return answer
  
# solution(["X591X","X1X5X","X231X", "1XXX1"])

## 그냥 맨바닥에 풀려다가 DFS인거 질문하기 보고 알아서 갖다가 일단 배낌... 알고리즘 다까먹어서 다시하기 어렵다... ㅠ

import sys 
sys.setrecursionlimit(10000)

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def solution(maps):
    row_length = len(maps)
    column_length = len(maps[0])
    
    global now_island_value
    now_island_value = 0
    
    visited = [
        [False for column in range(column_length)]  # "FFFFF"
        for row in range(row_length)
    ]
    
    def DFS(y, x):
        global now_island_value
        # 방문 여부 체크
        if visited[y][x]:
            return 0
        visited[y][x] = True
        now_island_value += int(maps[y][x])

        # 상하좌우 체크
        for i in range(4):
            next_y = y + dy[i]
            next_x = x + dx[i]

            # 칸 벗어남 체크 + 바다 체크 (무인도인 경우 재귀호출)
            ret = int(maps[y][x])
            if (0 <= next_y < row_length) and (0 <= next_x < column_length) and maps[next_y][next_x] != 'X':
                DFS(next_y, next_x)
                
    # 각 무인도마다 식량 갯수 구하기 (result list)
    result = []
    for row in range(row_length):
        for column in range(column_length):
            # 바다가 아니고, 이미 방문한 칸이 아닌 경우 무인도 1개
            if maps[row][column] != 'X' and not visited[row][column]:
                DFS(row, column)  # 무인도 전체 순회
                result.append(now_island_value)  # 그 무인도 전체의 값 추가
                now_island_value = 0  # 이제 다음 무인도로 떠날 시간이라서 0으로 초기화

    if len(result) < 1:
        return [-1]

    return sorted(result)