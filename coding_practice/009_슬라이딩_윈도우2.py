checkList = [0] * 4
myList = [0] * 4
checkSecret = 0

def myAdd(c):
    global checkList, myList, checkSecret
    if c == 'A':
        myList[0] += 1
        if myList[0] == checkList[0]:
            checkSecret += 1
    elif c == 'C':
        myList[1] += 1
        if myList[1] == checkList[1]:
            checkSecret += 1
    elif c == 'G':
        myList[2] += 1
        if myList[2] == checkList[2]:
            checkSecret += 1
    elif c == 'T':
        myList[3] += 1
        if myList[3] == checkList[3]:
            checkSecret += 1

def myRemove(c):
    global checkList, myList, checkSecret
    if c == 'A':
        if myList[0] == checkList[0]:
            checkSecret -= 1
        myList[0] -= 1
    elif c == 'C':
        if myList[1] == checkList[1]:
            checkSecret -= 1
        myList[1] -= 1
    elif c == 'G':
        if myList[2] == checkList[2]:
            checkSecret -= 1
        myList[2] -= 1
    elif c == 'T':
        if myList[3] == checkList[3]:
            checkSecret -= 1
        myList[3] -= 1

S, P = map(int, input().split())
Result = 0
A = list(input())
checkList = list(map(int, input().split()))

# checkList에서 0이면 무조건 조건을 만족시키므로 checkSercret을 += 1해준다.
# checkList는 A,C,G,T의 각 글자를 만족시키는지 여부를 숫자로 센다.
# A,C,G,T 조건 모두 만족시 checkList = 4
# 그러므로 checkList[i] == 0이면 무조건 한 글자의 조건을 만족시킨다는 뜻이다.
for i in range(4):
    if checkList[i] == 0:
        checkSecret += 1

for i in range(P):
    myAdd(A[i])

if checkSecret == 4:
    Result += 1

for i in range(P, S):
    j = i - P
    myAdd(A[i])
    myRemove(A[j])
    if checkSecret == 4:
        Result += 1

print(Result)