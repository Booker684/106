import sys

def main():
    # 讀取一行輸入，並轉換為三個整數
    line = sys.stdin.readline().strip()
    if not line:
        return
    
    # 將三邊長放入清單並排序，確保 edges[0] <= edges[1] <= edges[2]
    edges = sorted(map(int, line.split()))
    a, b, c = edges[0], edges[1], edges[2]
    
    # 1. 檢查是否能組成三角形
    if a + b <= c:
        print("Invalid")
    else:
        # 2. 能組成三角形，接著判斷種類
        if a == b == c:
            print("Equilateral")
        elif a == b or b == c or a == c:
            print("Isosceles")
        else:
            print("Scalene")

if __name__ == "__main__":
    main()