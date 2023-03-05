def solution(s, p, dna, acgt):
    count = 0
    check = [0] * 4
    curIdx = 0
    reset(p, dna, check)
    if isAcgt(check, acgt):
        count += 1
    for i in range(p, s):
        moveRight(i, curIdx, check, dna)
        curIdx += 1
        if (isAcgt(check, acgt)):
            count += 1

    print(count)

def reset(p, dna, check):
    for i in range(p):
        inputCheck(dna[i], check)

def inputCheck(str, check):
    if str == 'A': check[0] += 1
    elif str == 'C': check[1] += 1
    elif str == 'G': check[2] += 1
    elif str == 'T': check[3] += 1

def outCheck(str, check):
    if str == 'A': check[0] -= 1
    elif str == 'C': check[1] -= 1
    elif str == 'G': check[2] -= 1
    elif str == 'T': check[3] -= 1

def moveRight(i, curIdx, check, dna):
    outCheck(dna[curIdx], check)
    inputCheck(dna[i], check)

def isAcgt(check, acgt):
    for i in range(4):
        if not isCorrect(check[i], acgt[i]):
            return False
    return True

def isCorrect(a, b):
    if b > 0 and a >= b:
        return True
    elif b == 0:
        return True
    return False


s, p = map(int, input().split())
dna = list(input())
acgt = list(map(int, input().split()))
solution(s, p, dna, acgt)