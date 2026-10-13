import sys

def main():
    # 讀取輸入的年份
    line = sys.stdin.readline().strip()
    if not line:
        return
    
    y = int(line)
    
    # 根據閏年規則進行條件判斷
    if y % 400 == 0:
        print("Leap")
    elif y % 100 == 0:
        print("Common")
    elif y % 4 == 0:
        print("Leap")
    else:
        print("Common")

if __name__ == "__main__":
    main()