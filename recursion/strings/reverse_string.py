# def reverse(s):
#     if(s==""):
#         return ""
#     return reverse(s[1:])+s[0]
#
# a=reverse("pran")
# print(a)

def fiboonaci(n):
    if (n == 1 or n == 0):
        return 1
    return fiboonaci(n - 1) + fiboonaci(n - 2)
a=fiboonaci(4)
print(a)