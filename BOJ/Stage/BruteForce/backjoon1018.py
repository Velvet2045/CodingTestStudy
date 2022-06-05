## backjoon1018.py
## 브루트 포스(brute force), 키 전수조사(exhaustive key search) 또는 무차별 대입(無差別代入)은 조합 가능한 모든 문자열을 하나씩 대입해 보는 방식으로 암호를 해독하는 방법

row, col = map(int, input().split())

data = []
repair = []
for _ in range(row):
    data.append(input())
    
# 체스판에서 검사해야 할 영역을 8x8만큼 줄여서 repair에 append
for i in range(row-7):
    for j in range(col-7):
        count_w = 0
        count_b = 0
        # 체스판에서 검사해야 할 영역 8x8
        for k in range(i,i+8):
            for l in range(j,j+8):
                # k와 l의 합이 짝수인 경우가 색상이 같아야 하는 영역 1
                if (k + l) % 2 == 0:
                    if data[k][l] != 'W':
                        count_w += 1
                    if data[k][l] != 'B':
                        count_b += 1
                # k와 l의 합이 홀수인 경우가 색상이 같아야 하는 영역 2
                else:
                    if data[k][l] != 'B':
                        count_w += 1
                    if data[k][l] != 'W':
                        count_b += 1
                        
        # BWBWBWBW인 경우와 WBWBWBWB인 경우를 모두 계산
        repair.append(count_w)
        repair.append(count_b)
        
print(min(repair))
