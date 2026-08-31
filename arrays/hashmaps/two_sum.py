def twosum(nums,target):
    seen={}#Seen is a dictionary that will store each value that didnt have the same target-n value 
    for i,n in enumerate(nums):
        #here enumerate is used to simply assign numbers to each value present in the list "nums" 
        #ex:-- for nums=[8,6,2,4] enumerarte whill make it so that a number [8:0,6:1,2:2,4:3] so its basically indexing
        
        check = target - n#here we made check this is used as a condition to see if the num subtracted from the target is present 

        """ Now a question comes here ,why did we use check?
            The answer to it is efficiency since we are checking if 2 nums in a array will make a sum that is targe
            thinking about this if:
            a+b = target
            then
            b = target - a
            if there is a b present in the list that is equivalent to target - a then we can just say the result is the index of 
            [a,b] here : b is check and n is a  at each a if there is a b present in seen we consider it to be a result and if 
            there is no check present we add the new a to seen along with its index we got through enumeration"""
        
        if check in seen:
            return [seen[check],i]
        else:
            seen[n]=i

    return []

nums = [2,7,11,15]
target = 9       
print(twosum(nums,target))   
#This is the first test case just for demo purpose i picked from leet code