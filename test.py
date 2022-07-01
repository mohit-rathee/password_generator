# import random
# import subprocess
# import string
# import os
# from tokenize import String
# ''

# lower_case = "abcdefghijklmopqrstuvwxyz"
# num = "0123456789"
# upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# spec_char = "!@#$%^&*()_+}{:[]"

# ans = lower_case + upper_case + num +spec_char

# length = random.randint(8,12)
# password = "".join(random.sample(ans,length))
# print("Genrated pahhssword is ",password)


# x=['hello,hi ,teri,maa,ki,chut']
# l="".join(x)
# print(x)


# # cmd = "ls -{0} -{1}".format(var1,var2)
# cmd = "echo {0} >> cmd.txt".format(password)
# os.system(cmd)



def y(*args):
    for i in range(len(args)):
        y=str(args[i])
        print(y)
        for i in range(len(y)):
            y=y.split()
            print(y)

y(["a","b 4","4"])    