# 讀取第一行：P點座標
x1, y1 = map(int, input().split())

# 讀取第二行：Q點座標
x2, y2 = map(int, input().split())

# 計算座標差
dx = x2 - x1
dy = y2 - y1

# 計算距離平方並輸出
ans = dx * dx + dy * dy
print(ans)