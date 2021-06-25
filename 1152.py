a = input()

def clear(s: list):
    for i in s:
        if i == '':
            s.remove(i)      
    return s

if a == " ":
    print(0)
else:
    daa = clear([*a.split(" ")])

    print(len(daa))