def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    seen = {}
    for c in magazine:
        if c in seen:
            seen[c] += 1
        else:
            seen[c] = 1
    magazine = set(magazine)
    for c in ransomNote:
        if c in magazine and seen[c]>=0:
            seen[c] -=1
        else:
            return False

    return True
            
