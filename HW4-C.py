import sys

def main():
    # 讀取一行輸入，並以空白分隔轉換為三個整數
    line = sys.stdin.readline().strip()
    if not line:
        return
    
    a, b, c = map(int, line.split())
    
    # 假設 a 是最大值
    ans = a
    
    # 檢查 b 是否比目前假設的最大值大
    if b > ans:
        ans = b
        
    # 檢查 c 是否比目前假設的最大值大
    if c > ans:
        ans = c
        
    # 輸出最終的最大值
    print(ans)

if __name__ == "__main__":
    main()