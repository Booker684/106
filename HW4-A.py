import sys

def main():
    # 讀取一行輸入，並以空白分隔轉換為兩個整數
    line = sys.stdin.readline().strip()
    if not line:
        return
    
    a, b = map(int, line.split())
    
    # 判斷大小並輸出結果
    if a > b:
        print("Greater")
    elif a < b:
        print("Less")
    else:
        print("Equal")

if __name__ == "__main__":
    main()