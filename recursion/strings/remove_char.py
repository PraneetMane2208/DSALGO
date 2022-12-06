def remove_char(p, up):
    # print(char)
    if len(up) == 0:
        return p
        # return ""
    cha = up[0]

    if cha == 'a':
        return remove_char(p, up[1:])
    else:
        return remove_char(p + cha, up[1:])

def skip_apple(p, up):
    # print(char)
    if len(up) == 0:
        return ""
        # return ""


    if(up.startswith('apple')):
        return skip_apple(p, up[5:])
    else:
        return up[0] +skip_apple(p, up[1:])


c = skip_apple(" ", "acapplecad")
print(c)
