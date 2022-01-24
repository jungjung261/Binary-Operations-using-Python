def sum(A, B):
    temp = 0
    C = ''
    if(len(A) > len(B)):
        B = B.zfill(len(A))
    else:
        A = A.zfill(len(B))
    for i in range(len(A)-1, -1, -1):
        a = temp
        if(A[i] == '1'):
            a += 1
        if(B[i] == '1'):
            a += 1
        if(a % 2 == 1):
            C = '1' + C
        else:
            C = '0' + C
        if (a < 2):
            temp = 0
        else:
            temp = 1
    if (temp > 0):
        C = '1'+C
    return C

def dif(A, B):
    C = ''
    if(len(A) > len(B)):
        B = B.zfill(len(A))
    else:
        A = A.zfill(len(B))
    if (int(A) < int(B)):
        return "error"
    for i in range(len(A)-1, -1, -1):
        if(B[i] == '1'):
            C = '0' + C
        else:
            C = '1' + C
    C = sum(A, sum(C, '1'))
    return str(int(C[1:]))

def prod(A, B):
    temp = []
    if(len(A) > len(B)):
        B = B.zfill(len(A))
    else:
        A = A.zfill(len(B))
    for i in range(len(A)-1, -1, -1):
        if B[i] == '1':
            temp.append(A)
        else:
            temp.append('0')
    for i in range(1, len(B)):
        temp[i] = temp[i].ljust(len(A)+i, '0')
    C = temp[0]
    for i in range(1, len(temp)):
        C = sum(C, temp[i])
    return str(int(C))


def deleteZero(A):
    temp = 0
    for i in range(0, len(A)):
        if (A[i] == '0'):
            temp += 1
        else:
            break
    if (temp == len(A)):
        return '0'
    return A[temp:len(A)]


def bitwiseAnd(A, B):
    C = ''
    counta = len(A) - 1
    countb = len(B) - 1
    while (counta >= 0 and countb >= 0):
        C += str(int(A[counta]) and int(B[countb]))
        counta -= 1
        countb -= 1
    return deleteZero(C[::-1])

def bitwiseOr(A, B):
    C = ''
    if(len(A) > len(B)):
        B = B.zfill(len(A))
    else:
        A = A.zfill(len(B))
    for i in range(len(A)):
        if(A[i] == '1' or B[i] == '1'):
            C = C + '1'
        else:
            C = C + '0'
    return str(int(C))

def bitwiseXor(A, B):
    C = ''
    if(len(A) > len(B)):
        B = B.zfill(len(A))
    else:
        A = A.zfill(len(B))
    for i in range(len(A)):
        if(A[i] == B[i]):
            C = C + '0'
        else:
            C = C + '1'
    return str(int(C))

def bitwiseNot(A):
    C = ''
    for i in range(len(A)):
        if(A[i] == '1'):
            C = C + '0'
        else:
            C = C + '1'
    return str(int(C))

def bitwiseLeftShift(A):
    C = list(A)
    temp = C[0]
    for i in range(len(A)-1):
        C[i] = C[i+1]
    C[len(A)-1] = temp
    C = "".join(C)
    return str(int(C))

def bitwiseRightShift(A):
    C = list(A)
    temp = C[len(A)-1]
    C = temp + "".join(C[:len(A)-1])
    return str(int(C))

def bin2Hex(A):
    C = ''
    a = len(A)
    while a > 0:
        if a - 4 < 0:
            temp = int(A[0:a])
        else:
            temp = int(A[(a-4):a])
        if (temp == 0):
            C += '0'
        elif (temp == 1):
            C += '1'
        elif (temp == 10):
            C += '2'
        elif (temp == 11):
            C += '3'
        elif (temp == 100):
            C += '4'
        elif (temp == 101):
            C += '5'
        elif (temp == 110):
            C += '6'
        elif (temp == 111):
            C += '7'
        elif (temp == 1000):
            C += '8'
        elif (temp == 1001):
            C += '9'
        elif (temp == 1010):
            C += 'A'
        elif (temp == 1011):
            C += 'B'
        elif (temp == 1100):
            C += 'C'
        elif (temp == 1101):
            C += 'D'
        elif (temp == 1110):
            C += 'E'
        elif (temp == 1111):
            C += 'F'
        a -= 4
    return deleteZero(C[::-1])
