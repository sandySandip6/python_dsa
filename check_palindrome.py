# 
def is_palindrome(s):
    res = s.lower().replace(" ", "")
    return res == s[::-1]

print(is_palindrome("tnent"))