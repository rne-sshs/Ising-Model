from cmath import log
from math import exp

ARRAY_W = [[0 for _ in range(1000)] for _ in range(1000)]
ARRAY_A = [[0 for _ in range(1000)] for _ in range(1000)]
ARRAY_R = [[0 for _ in range(1000)] for _ in range(1000)]
CONST_T = 0.5
CONST_N = 0
CONST_I = 5000

data = open("data.txt", 'r')
lines = data.readlines()
CONST_N = len(lines)
for i in range(CONST_N):
    for j in range(CONST_N):
        ARRAY_W[i][j] = float(lines[i].split(" ")[j])
data.close()

for i in range(CONST_I):
    for j in range(CONST_N):
        sum = 0
        for k in range(CONST_N):
            print(ARRAY_W[j][k])
            sum += exp((ARRAY_R[j][k] + ARRAY_W[j][k]/2)/CONST_T)
        for k in range(CONST_N):
            ARRAY_A[j][k] = ARRAY_W[j][k]/2 - CONST_T * log(sum - exp((ARRAY_R[j][k] + ARRAY_W[j][k]/2)/CONST_T))
    for j in range(CONST_N):
        sum = 0
        for k in range(CONST_N):
            sum += exp((ARRAY_A[j][k] + ARRAY_W[j][k]/2)/CONST_T)
        for k in range(CONST_N):
            ARRAY_R[j][k] = ARRAY_W[j][k]/2 - CONST_T * log(sum - exp((ARRAY_A[j][k] + ARRAY_W[j][k]/2)/CONST_T))

for i in range(CONST_N):
    for j in range(CONST_N):
        if (ARRAY_R[i][j] + ARRAY_A[i][j]) > 0:
            print("1 ", sep="")
        else:
            print("0 ", sep="")
    print()