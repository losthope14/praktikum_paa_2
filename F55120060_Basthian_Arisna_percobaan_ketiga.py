def get_BMBC(pattern): #untuk pergeseran pada pattern
    BMBC = dict()
    for i in range(len(pattern) - 1):
        char = pattern[i]
        BMBC[char] = i + 1
    return BMBC

def get_BMGS(pattern):
    BMGS = dict()
    BMGS[''] = 0
    for i in range(len(pattern)):
        GS = pattern[len(pattern) - i - 1]
        for j in range(len(pattern) - i - 1):
            NGS = pattern[j:j + i + 1]
            if GS == NGS:
                BMGS[GS] = len(pattern) - j - i - 1
    return BMGS

def BM(string, pattern, BMBC,BMGS): #algoritma boyer moore untuk pencarian string
    i = 0
    j = len(pattern)
    #j = 4

    while i < len(string): # i < 18
        print('loop 1: ', i)
        while(j > 0): #pencocokan bit string dan pattern
        # 4 > 0
            print('if i: ', i)
            a = string[i + j - 1:i + len(pattern)]
            b = pattern[j - 1:]

            if a == b:
                j = j - 1
                print(a)
                print('j : ', j)
            else:
                print('else i: ',i)
                i = i + max(BMGS.setdefault(b[1:], len(pattern)), j - BMBC.setdefault(string[i  + j - 1], 0))
                print('change : ',i)
                print(BMGS.setdefault(b[1:], len(pattern)))
                print(j - BMBC.setdefault(string[i  + j - 1], 0))
                print(max(BMGS.setdefault(b[1:], len(pattern)), j - BMBC.setdefault(string[i  + j - 1], 0)))
                j = len(pattern)
                print('j : ', j)

            if j == 0:
                print('Bas')
                return i
    return None

if __name__ == '__main__':
    string = 'nama saya basthian'
    pattern = 'basthian'
    BMBC = get_BMBC(pattern=pattern)
    BMGS = get_BMGS(pattern=pattern)
    x = BM(string=string, pattern=pattern, BMBC=BMBC, BMGS=BMGS)

    print(BMBC)
    print(BMGS)
    print(x)
    th = x + len(pattern)
    print(string[x:th])