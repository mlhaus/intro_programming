import re

def isPalindrome(word):
    word = word.replace(" ", "")
    word = word.lower()
    word2 = ""
    for i in range(len(word) - 1, -1, -1):
        word2 += word[i]
    return word == word2

# source: https://chatgpt.com/share/6723cc03-3e70-8007-a4ca-983797bc3a42
is_palindrome = lambda word: (cleaned := re.sub(r'[^a-zA-Z0-9]', '', word.lower())) == cleaned[::-1]
print(is_palindrome("race car"))  # True
print(is_palindrome("hello"))    # False
print(is_palindrome("A man, a plan, a canal, Panama"))  # True
print(is_palindrome("No 'x' in Nixon"))                 # True
print(is_palindrome("Hello, World!"))                   # False

word = "Taco cat"
print(isPalindrome(word))
word = "Marc"
print(isPalindrome(word))
word = "race car"
print(isPalindrome(word))


password = "Kirkw00d"

print(password[0]) #K
print(password[1]) #i
print()

for i in range(len(password) - 1, -1, -1):
    print(password[i], end="")
print()

for i in range(len(password)):
    print(password[i])
print()

for letter in password:
    print(letter)
print()




user_password = input("Enter the password: ").strip()
if(password == user_password):
    print("Success")
else:
    print("Incorrect password")


