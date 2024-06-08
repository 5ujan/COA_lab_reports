from addition import fullSum

def mul(first, second):
    for n in range(len(first), 8):
        first = "0"+first
    for n in range(len(second), 8):
        second = "0"+second
    prodArr = []
    for i in range(8):
        if(second[len(second)-i-1]=='1'):
            temp = first
            n=0
            while(n<i):
                temp+='0'
                n+=1
            prodArr.append(temp)
    result ="00000000"
    for i in prodArr:
        result = fullSum(result, i)
    return result


print(mul('10', '11'))