text = input("Enter some text : ")


def is_vowel(char):
    return char.lower() in "aeiou"


for char in text:
    if char.isalpha():
        if is_vowel(char):
            print("{0} is vowel".format(char))
        else:
            print("{0} is consonant".format(char))
