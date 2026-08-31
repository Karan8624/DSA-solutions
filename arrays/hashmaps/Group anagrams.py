def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    sorted_chars = [''.join(sorted(w)) for w in strs] #sort the characters for words within the strs list
    anagrams = {}

    for i, n in enumerate(sorted_chars):
        if n in anagrams:
            anagrams[n].append(strs[i]) # 
        else:
            anagrams[n] = [strs[i]]
    
    return anagrams,list(anagrams.values())
    
test = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(test))