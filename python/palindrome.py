def isPalindrome(x: int) -> bool:
        # two pointers
        # pointer #1 left pointer #2 right
        norm = x
        rev = 0
        while x > 0:
            dig = x % 10
            rev = rev * 10 + dig
            x = x // 10
        if rev == norm:
            return True
        return False
        

def convert(arr):
    result = 0
    arrStr = ''
    for u in arr:
        arrStr += str(u)
    for i in arrStr:
        result += int(i)
    return result

assert(isPalindrome(1221))
assert(convert([11, 2, 3]) == 7)


