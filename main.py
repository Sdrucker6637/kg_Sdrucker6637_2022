def mapchecker(s1,s2):
    if len(s1)<= len(s2):
        dr={}
        for i in range(len(s1)):
            if s1[i] not in dr:
                dr[s1[i]]=s2[i]
            if dr[s1[i]]!=s2[i]:
                return False
        return True
    return False

