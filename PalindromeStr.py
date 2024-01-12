def reverseStr(x):
    return True if x == x[::-1] else False

result = reverseStr("malayalam")
print(result)

def palindromeStr(str):
    
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str) - i -1]:
            return False
        return True
            
result = palindromeStr("abtba")
print(result)
