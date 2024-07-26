def swap_case(s):
    k=""
    for i in s:
        if i>='A' and i<='Z':
            k+=i.lower()
        elif i>='a' and i<='z':
            k+=i.upper()
        else:
            k+=i
    return k

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
