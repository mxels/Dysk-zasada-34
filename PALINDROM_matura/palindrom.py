# palindrom

def sprawdz1(s):
    dl = len(s)
    for i in range(dl // 2):
        if s[i] != s[dl - i - 1]:
            return False
    return True

def sprawdz2(s):
    return (s == s[::-1])

print(sprawdz1("kajak"))
print(sprawdz2("kajaki"))

