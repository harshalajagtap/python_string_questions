from dataclasses import replace


def replace_occurance(str1):
    new_str=""
    for char in range(len(str1)):
            new_str = str1.replace('a','$')
    print(new_str)



inpt_str = str(input("Enter string : "))
replace_occurance(inpt_str)