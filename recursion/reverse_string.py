# def reverse(s):
#     if(s==""):
#         return ""
#     return reverse(s[1:])+s[0]
#
# c="kayak"
# d=reverse(c)
# if(d==c):
#     print("Yes")
#
# print(reverse(c))

def palindrome(s):
    if(len(s)==0 or len(s)==1):
        return True
    if(s[0]==s[-1]):
        return palindrome(s[1:len(s)-1])
    return False

d="GadaG"
print(palindrome(d))