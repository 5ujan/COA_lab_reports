from addition import fullSum
from subtraction import sub

# def mul(first, second):
#     for n in range(len(first), 8):
#         first = "0"+first
#     for n in range(len(second), 8):
#         second = "0"+second
#     prodArr = []
#     for i in range(8):
#         if(second[len(second)-i-1]=='1'):
#             temp = first
#             n=0
#             while(n<i):
#                 temp+='0'
#                 n+=1
#             prodArr.append(temp)
#     result ="00000000"
#     for i in prodArr:
#         result = fullSum(result, i)
#     return result


# print(mul('10', '11'))


one = "11111111"
zero = '00000000'

def booth(m, q):
    if(m[0]=='0'):
        m = zero[-len(m):] + m
    if(m[0]=='1'):
        m = one[-len(m):] + m
    if(q[0]=='0'):
        q = zero[-len(q):] + q
    if(q[0]=='1'):
        q = one[-len(q):] + q

    a = zero
    q_prev = '0'

    for i in range(8):
        if(q[-1]=='1' and q_prev=='0'):
            a = sub(a, m)
        elif(q[-1]=='0' and q_prev=='1'):
            a = fullSum(a, m)
        a = a[-8:]
        q_prev = q[len(q)-1]
        q=a[len(a)-1]+q[0:7]
        a= a[0]+ a[0:7]
       
        # print("a", a, "q:" , q)

    mul= a+q
    return mul[-8:]

  

print('result:', booth("1101", "1011"))

# print(restoringDivision(dividend, divisor))
