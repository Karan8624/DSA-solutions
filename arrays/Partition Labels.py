def partitionLabels( s):
    """
    :type s: str
    :rtype: List[int]
    """

    seen = {}

    for i in range(len(s)):
        seen[s[i]] = i

    return seen

print(partitionLabels(s = "ababcbacadefegdehijhklij"))