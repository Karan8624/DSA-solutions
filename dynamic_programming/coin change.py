def coinChange(  coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    record = [float('inf')] * (amount + 1)
    record[0] = 0
    for i in range(1,amount+1):
        for c in coins:
            if c<=amount:

                record[i] = min(record[i-c]+1,record[i])
            else:
                continue
    return record[-1]

print(coinChange(coins = [1,2,5], amount = 11))


"""
d[0] = 0
d[1] = d[i-c] + c= d[1-1] +1 = 1(present)
d[2] = d[2-1] + 1 = d[1] + 1 = 1+1 = 2
d[3] = d[3-1] + 1 = d[2] +1 = 2 + 1 = 3 (we consider 2 +1 beacuase theres no 3 in the coins array)
d[4] = d[4-1] + 1 = d[3] + 1 =  1+2+1 = 4 (valid)
    d[4] = d[4-2] + 2 = d[2] + 2 = 2+2 = 4 (valid) (best)
    d[4] = d[4-5] = d[-1] invalid
d[5] = d[5-1] +1 = d[4] + 1 = 2+2+1 = 5 (valid)
    d[5] = d[5-2] + 2 = d[3] + 2 = 1+2+2 = 5(valid)
    d[5] = d[5-3] + 3(not valid 3 is not a coin)
    d[5] = d[5-4] + 4(not valid 4 is not a coin)
    d[5] = d[5-5] + 5 = 0+5 (valid) (best)
d[6] = d[6-1] + 1 = d[5] + 1 = 5+1 = 6(valid)
    d[6] = d[6-2] = d[4] + 2 = 2+2+2 = 6 (valid)
    d[6] = d[6-3] + 3(invalid)
    d[6 - 4] invalid
    d[6-5] = d[6-1] (best)
only chacking for in coins now

d[7] = d[7-1] +1 = d[6] + 1 = 5+1+1 = 7(valid)
    d[7] = d[7-2] + 2 = d[5]+2 = 5+2 = 7(valid)
    d[7] = d[7-5] = d[2] + 5 = 5+2 = 7 (valid) (best)

d[8] = d[8-1] +d[1] = d[7] +1 = 5+2+1
    d[8] = d[8-2] + 2 = d[6] +2 = 5+1+2 = 8(valid)
    d[8] = d[8-5] +5 = d[3] + 5 = 1+2+5 = 8(valid)
d[9] = d[9-1] +1 = d[8] +1 = 1+2+5+1 = 9(valid)
    d[9] = d[9-2] = d[7] + 2= 2+5+2 = 9(valid)
    d[9] = d[9-5] = d[4] + 5 = 2+2+5 (valid) best
d[10] = d[10-1] +1 = d[9] +1 = 2+2+5+1 = 10 valid
    d[10] = d[10-2] + 2 = d[8]+2 = 5+1+2+2 = 10 valid
    d[5] = d[10-5] + 5= d[5] + 5 = 5+5 = 10 best
d[11] = d[11-1] = d[10] + 1= 5+5+1 valid
    d[11] = d[11-2] +2 = d[9] + 2 = 5+2+2+2 = 11
    d[11] = d[11-5] + 5 = d[6] + 5 = 5+1+5 = 11 best
"""
#The number of coins are to be considered for the answer

"""
This is a DP problem that follows recurrence relation or state transition formula for the result
"""

