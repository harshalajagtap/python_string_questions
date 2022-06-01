from email import charset


def is_pangram(str1):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
       if char not in str1.lower():
           return False
      
    return True

inpt_str= "The quick brown fox jumps over the lazy dog"

if(is_pangram(inpt_str)== True):
    print("given string is pangram")
else:
    print("given string is not pangram")





