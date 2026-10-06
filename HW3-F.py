# 讀取 2 行輸入
a, b = map(int, input().split())
c, d = map(int, input().split())

# 計算行列式
det = a * d - b * c

# 計算反矩陣的四個實數值
r11 = d / det
r12 = (-b) / det
r21 = (-c) / det
r22 = a / det

# 輸出結果，:.4f 代表固定顯示小數點後 4 位
print(f"{r11:.4f} {r12:.4f}")
print(f"{r21:.4f} {r22:.4f}")