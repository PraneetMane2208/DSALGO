# def rev(s):
#     rev='/'.join([' '.join(reversed(s.split(' ')))
#                    for s in s.split('.')])
#     return rev
#
# s="Pizza love I. cream ice love also I"
# a=rev(s)
# print(a)

def Streverse(s):
    res = ""
    str = ""
    for s in s.split('.'):
        a=' '.join(reversed(s.split(' ')))
        res=res + str + a
        str='. '
    return res

s="Pizza love I. cream ice love also I"
b=Streverse(s)
print(b)