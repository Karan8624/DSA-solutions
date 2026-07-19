def evalRPN(tokens):
    """
    :type tokens: List[str]
    :rtype: int
    """

    ops = set(["-","+","*","/"])
    ans  = None
    nums = []

    """for i in range(len(tokens)):
        if tokens[i] in ops:
            if ans != None:
                if tokens[i] == "+":
                    ans += nums[-1]
                elif tokens[i] == "-":
                    ans -= nums[-1]
                elif tokens[i] == "*":
                    ans *= nums[-1]
                else:
                    ans /= nums[-1]
                nums.pop()
                nums.append(ans)
            else:
                if tokens[i] == "+":
                    ans = nums[-1] + nums[-2]
                elif tokens[i] == "-":
                    ans = nums[-1] - nums[-2]
                elif tokens[i] == "*":
                    ans = nums[-1] * nums[-2]
                else:
                    ans = nums[-1] / nums[-2]
                nums.pop()
                nums.pop()
                nums.append(ans)
        else:
            nums.append(int(tokens[i]))
    return ans
    """
    #the above one didnt work trying a diff approach by using just one stack 

    for t in tokens:
        if t in ops:
            b = nums[-1]
            nums.pop()
            a = nums[-1]
            nums.pop()
            if t == "+":
                nums.append(a+b)
            elif t == "-":
                nums.append(a-b)
            elif t == "*":
                nums.append(a*b)
            else:
                nums.append(int(a/b))
        else:
            nums.append(int(t))

    return nums[-1]


            

                



print(evalRPN(tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))