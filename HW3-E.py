# 依序讀取 4 行輸入
a, b = map(int, input().split())
c, d = map(int, input().split())
e, f = map(int, input().split())
g, h = map(int, input().split())

# 根據矩陣乘法公式計算結果
c11 = a * e + b * g
c12 = a * f + b * h
c21 = c * e + d * g
c22 = c * f + d * h

# 依題目格式輸出（共 2 行，每行 2 個數字以空白分隔）
print(f"{c11} {c12}")
print(f"{c21} {c22}")