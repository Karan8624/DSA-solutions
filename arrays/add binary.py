def addBinary(a, b):
    alen = len(a) -1
    blen = len(b) -1 
    c = 0
    ans = []
    while alen >=0 or blen >= 0 or c:
        sum = c
        if alen>= 0:
            sum+= int(a[alen])
            alen-=1
        if blen>= 0:
            sum+= int(b[blen])
            blen-=1

        ans.append(sum%2)
        c = sum//2
    return ''.join(map(str, ans[::-1]))

print(addBinary(a = "1010", b = "1011"))


#Explaination:-
"""
1. we use alen and b lean as counters for indexing the stings a  and b 
2. We traverse through both of them in a reverse order 
3. C is the carry variable 
4. The while loop will run until there is nothing to be traversed or there is no carry present 
5. Inside the loop we assign sum to c "the purpose of sum is to calculate the digit at each index
6. we check if both a and b have a valid instance and then add the number at that index for that 
   index for that string to the sum by convering it with int()
7. We append sum%2 (this makes sure the number is either 1 or 2 )
8. We assign  c = sum//2 this assures that the there csan be no carry when the sum is just 1
9. Since ans isnt a string but a list we use join() to concatenate it 
"""

#Dry run :- a = 1010 and b = 1011 

"""
Initialization:- alen = 3 blen = 3 c= 0 and ans= [](empty list)

loop start :-

itereation 1 :- alen = 3 , blen =3 , c =0
    sum = 0
    alen >0  true :
        sum += 0 = 0
        alen -= 1  = 2
    blen>0 true:
        sum  += 1 = 1
        blen -= 1 = 2
    ans.append(sum%2= 1 )
    c = sum//2 = 0.5 -> 0

itereation 2 :- alen = 2 , blen =2 , c =1:-
    sum = 0
    alen >0  true :
        sum += 1 = 1
        alen -= 1  = 1
    blen>0 true:
        sum  += 1 = 2
        blen -= 1 = 1
    ans.append(sum%2= 0 )
    c = sum//2 = 1

iteration 3 :- alen = 1, blen = 1, c = 1:-
    sum = 1
    alen >= 0 true:
        sum += 0 = 1   # a[1] = '0'
        alen -= 1 = 0
    blen >= 0 true:
        sum += 0 = 1   # b[1] = '0'
        blen -= 1 = 0
    ans.append(1%2 = 1)
    c = 1//2 = 0


itereation 4 :- alen =0, blen =0 c =0:-
    sum = 0
    alen =0  true:
        sum += 1 = 1
        alen -= 1  = -1
    blen>0 true:
        sum  += 1 = 2
        blen -= 1 = -1
    ans.append(sum%2= 0 )
    c = sum//2 = 1

itereation 5 :- alen = -1 , blen =-1, c =1 (true since carry present):-
    sum = 1
    alen >0 false
    blen>0 false

    ans.append(sum%2= 1 )
    c = sum//2 = 0

loop end
"""
