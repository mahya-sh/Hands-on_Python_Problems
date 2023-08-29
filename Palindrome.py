def palindrome(input_string):
    word = input_string.lower()
    i = 0
    for char in word:
        if char == word[-(1+i)]:
            if (i + 1) == len(word):
                output = 'palindrome'
                break
            i += 1
        else:
            output = 'not palindrome'
            break
    return output

input_string = input()
result = palindrome(input_string)
print(result)