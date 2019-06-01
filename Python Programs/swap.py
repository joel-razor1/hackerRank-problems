def swap_case(s):
    s1=""
    for i in range (0,len(s)):
        if s[i].islower():
            s1+=s[i].upper()
        elif s[i].isupper():
            s1+=s[i].lower()
        elif s[i].isalpha()==False:
             s1+=s[i]
    return s1

if __name__ == '__main__':
    s = raw_input()
    result = swap_case(s)
    print result