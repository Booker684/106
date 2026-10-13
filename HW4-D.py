import sys

def main():
    # 讀取停車時數 h
    line = sys.stdin.readline().strip()
    if not line:
        return
    
    h = int(line)
    total_fee = 0
    
    # 1. 計算第 1~2 小時的費用
    if h <= 2:
        total_fee += h * 30
    else:
        total_fee += 2 * 30  # 滿 2 小時扣滿
        
        # 2. 計算第 3~5 小時的費用
        if h <= 5:
            total_fee += (h - 2) * 20
        else:
            total_fee += 3 * 20  # 滿 3 小時扣滿
            
            # 3. 計算第 6 小時起的費用
            total_fee += (h - 5) * 10
            
    # 輸出總車費
    print(total_fee)

if __name__ == "__main__":
    main()