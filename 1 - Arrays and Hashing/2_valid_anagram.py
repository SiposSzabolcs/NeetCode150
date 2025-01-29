def isAnagram(self, s: str, t: str) -> bool:
    charlist = []
    
    for char in s:
        charlist.append(char)
        
    for char in t:
        if char in charlist:
            charlist.remove(char)
        else:
            return False
        
    if len(charlist) == 0:
        return True
    
    return False

def isAnagram_better(s,t):
    return sorted(s) == sorted(t)


print(isAnagram_better("x", "xx"))
        