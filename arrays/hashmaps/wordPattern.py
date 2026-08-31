def wordPattern(pattern: str, s: str) -> bool:
    record = {}
    for i in range(len(pattern)):
        if pattern[i] in record and record[pattern[i]] != s[i]:
            hi = 0
        else:
            record[pattern[i]] = s[i]
    return record

print(wordPattern(pattern = "abba", s = "dog cat cat dog"))