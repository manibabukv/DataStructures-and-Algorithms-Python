# Iterative Approach

def stringreverseIterative(s):
    reverse_string = ''
    for i in range(len(s)):
        reverse_string += s[len(s)-i-1]
    return reverse_string

print(stringreverseIterative('Mani'))

# Recursive Approach

def stringreverseRecursive(s):
    if len(s) == 0:
        return ""
    return s[len(s)-1] + stringreverseRecursive(s[:len(s)-1])

print(stringreverseRecursive("Zero To Mastery"))

basket = [2, 65, 34, 2, 1, 7, 8]

basket.sort()

print(basket)