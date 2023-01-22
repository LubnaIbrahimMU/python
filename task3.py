def is_balanced(s):
    brackets= [ "()" , "[]", "{}"]
    while any (x in s for x in brackets):
        for br in brackets:
            s=s.replace(br, "")
    if s in brackets or s== "":
        print ("YES")
    else:
        print("NO")
is_balanced("({[]})")