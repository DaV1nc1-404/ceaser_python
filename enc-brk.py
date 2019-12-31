def getascii(enc_str):
    ascii_strng = []
    for i in enc_str:
        n = ord(i)
        ascii_strng.append(n)
    return ascii_strng

def inc_n(n, ascii_str1):
    decr_str = []
    for i in ascii_str1:
        o = int(i+n)
        decr_str.append(o)
    return decr_str

def conf(ascii_str1, dec1):
    y = ch = n = None
    n = 0
    while ch != 1:
        print("Did you Get the Secret Message??")
        prntstr(dec1)
        ch = int(input("If yes press y or else press n "))
        if ch == 0:
            n = n+1
            inc_n(n, ascii_str1)
        elif ch == 1:
            exit(0)

def prntstr(dec1):
    final = []
    for i in dec1:
        r = chr(i)
        print(r)
        final.append(r)
    print(final_str)
    return final

final_str = []
dec1 = []
ascii_str1= []
enc_str = list(input("Enter the encrypted code!"))

ascii_str1 = list(getascii(enc_str))
dec1=(inc_n(0, ascii_str1))
conf(ascii_str1, dec1)


