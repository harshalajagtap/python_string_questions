def nth_index_char_rm(str1,n):
    new_str=""
    for i in range (len(str1)):
        if i != n:
            new_str = new_str + str1[i]
    print(new_str)






inpt_str = str(input("Enter string : "))
n_index = int(input("Enter index to remove char :"))
nth_index_char_rm(inpt_str,n_index)