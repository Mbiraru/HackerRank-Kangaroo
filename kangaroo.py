def kangaroo(x1, v1, x2, v2):
    if x1<x2 and v1<v2:
        return "NO"
    else:
        if v1!=v2 and (x2-x1)%(v1-v2) == 0:
            return "YES"
        else:
            return "NO"

x1V1X2V2 = input().split()

x1 = int(x1V1X2V2[0])

v1 = int(x1V1X2V2[1])

x2 = int(x1V1X2V2[2])

v2 = int(x1V1X2V2[3])
