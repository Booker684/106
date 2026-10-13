import sys

def main():
    # 讀取一行輸入，並以空白分隔轉換為三個整數 a, b, c
    line = sys.stdin.readline().strip()
    if not line:
        return
    
    a, b, c = map(int, line.split())
    
    # 計算判別式 D = b^2 - 4ac
    D = b * b - 4 * a * c
    
    # 依據判別式的值輸出實根個數
    if D > 0:
        print(2)
    elif D == 0:
        print(1)
    else:
        print(0)

if __name__ == "__main__":
    main()