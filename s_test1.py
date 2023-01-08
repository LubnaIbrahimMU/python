#first changed the string to list


string = "abracadabra"
l=list(string)
l[5]="k"
string="".join(l)
print(string)


# another way slicing string 

string = "abracadabra"
string = string[:5]+"k"+string[6:]
print(string)

# by function 

def fun(string, position, character):
    string = string[:position] + character + string[position+1:]
    return string

print(fun("abracadabra",5,"k"))
      

