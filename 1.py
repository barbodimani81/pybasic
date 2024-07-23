def palindrome(s):
    return s == s[::-1]


vurudi = input("Enter a word: ")
if palindrome(vurudi):
    print("Yes")
else:
    print("No")
