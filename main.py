def mapchecker(s1,s2):
    s1s=len(s1)
    s2s=len(s2)
    if s1s<= s2s:
        dr={}
        for i in range(s1s):
            if s1[i] not in dr:
                dr[s1[i]]=s2[i]
            if dr[s1[i]]!=s2[i]:
                print(False)
                return False
        print(True)
        return True
    print(True)
    return False

