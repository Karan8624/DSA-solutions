def longestCommonSubsequence(text1: str, text2: str) -> int:
    count = 0
    i = 0
    for c in text1:
        if c == text2[i]:
            count+=1
            i += 1
            if i == len(text2):
                return count
    return count


print(longestCommonSubsequence(text1 = "abcde", text2 = "ace" ))