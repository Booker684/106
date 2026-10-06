# 讀取輸入
N = int(input())

# 拆解百位、十位、個位
hundreds = N // 100
tens = (N // 10) % 10
ones = N % 10

# 計算總和、乘積與反轉
digit_sum = hundreds + tens + ones
digit_product = hundreds * tens * ones
reversed_N = ones * 100 + tens * 10 + hundreds

# 依題目要求格式輸出
print(f"{hundreds} {tens} {ones}")
print(digit_sum)
print(digit_product)
print(reversed_N)