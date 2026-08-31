def partitionLabels( s):
    """
    :type s: str
    :rtype: List[int]
    """

    seen = {}

    for i in range(len(s)):
        seen[s[i]] = i

    start = 0
    end = 0
    result = []
    for i in range(len(s)):
        end = max(end,seen[s[i]])
        if i == end:
            result.append(end - start +1)
            start = i+1
    return result

print(partitionLabels(s = "ababcbacadefegdehijhklij"))

#the approach

"""
1. Treat the partitions as a set
2. For each partition has a different set of characters
3. Each unique character in a set/partition will have a klast index it appearedin
4. if we track the last index occurence of each element and save it as a dict in seen
5. Then we linearly traverse the list again but this time we set 'end'.
6. end keeps track of the max index for each character and stores it this works as a limiter.
7. start is used to calculate the length as it is used as the index from 
   where we make a new partion. 
8. As we traverse throught the string we will encounter a situation where i==best in such case we
   have found our partition. We use end-start +1 to calculate the length of the partition and then
   we append it to our final result.


"""

#The dry run s = "abacded"

#For the above test case the seen dict will be 
"""
seen = [a:2 , b:1 , c:3 , d:6, e:5]
length of s  = 7
"""
# start,end = 0 result =[]
#The loop:
"""
at i = 0
end = max(end , seen[s[i]) = 2
i != 2 continue

at i = 1 
end  =  max(1,2) = 2
i != 2 continue

at  i= 2
end = max(2,2) = 2
i == 2
result  = end -start +1 = 2-0+1 = 3
start = 3

at  i =3 s[i] = c
end  = max(2,3) = 3
i == 3
result = 3 - 3 +1 = 1 
start = 4

at i = 4 s[i] = d
end  = (6,3)= 6
i != 6 continue

at i = 5 continue

at i = 6
end = 6
i == 6
result  = 6-4 +1 = 3

i == len(s)  terminate

result = [3,1,3] in strings ["aba" ,"c", "ded"]


"""

