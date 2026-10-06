# 讀取輸入總秒數
S = int(input())

# 計算小時、分鐘、秒
hours = S // 3600
remaining_seconds = S % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

# 依題目要求格式輸出，以空白分隔
print(f"{hours} {minutes} {seconds}")