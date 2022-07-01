import random
import subprocess
import string
import os
from tokenize import String

preff=[]
req_preff=[]
alf = "abcdefghijklmopqrstuvwxyz"
num = "0123456789"
ALF = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
spec_char = '''!@#$%^&*()_+{}:"<>?/.,;'[]=-'''

def generator(list):
    for i in range(len(list)):
        y=list[i]
        y=y.split()
        if len(y)==0:
            return preff
        elif len(y)==1:
            if y[0]=="num":
                preff.extend([str("".join(random.choice(num)))])
            elif y[0]=="alf":
                preff.extend([str("".join(random.choice(alf)))])      
            elif y[0]=="ALF":
                preff.extend([str("".join(random.choice(ALF)))])      
            elif y[0]=="@@@":
                preff.extend([str("".join(random.choice(spec_char)))])      
            else:
                preff.extend(y) 
        elif len(y)==2:
            if not y[1].isdigit():
                print("please, enter the no of element you wont i.e. numbers only")
                continue
                # return(0)
            if (y[0]=="num" and y[1].isdigit()):
                l=int(y[1])
                newnum=[str("".join(random.choices(num,k=l)))]
                preff.extend(newnum)

            if (y[0]=="alf" and y[1].isdigit()):
                l=int(y[1])
                newalf=[str("".join(random.choices(alf,k=l)))]
                preff.extend(newalf)
            
            if (y[0]=="ALF" and y[1].isdigit()):
                l=int(y[1])
                newALF=[str("".join(random.choices(ALF,k=l)))]
                preff.extend(newALF)

            if (y[0]=="@@@" and y[1].isdigit()):
                l=int(y[1])
                newspec_char=[str("".join(random.choices(spec_char,k=l)))]
                preff.extend(newspec_char)
            else:
                for i in range(len(y)):
                   preff.append(y[i])
        elif  len(y)>=2:
            for i in range(len(y)):
                preff.append(y[i])
    randomisor(preff)    


def randomisor(P):
    random.shuffle(P)
    password=""
    for i in range(len(P)):
        x=str(P[i])
        password+=str(x)
    print(password)

    # cmd = "ls -{0} -{1}".format(var1,var2)
    cmd = "echo {0}>>password.txt".format(password)
    os.system(cmd)


def generate_password():
    while True:
        y = input(" prefference (pls): ")
        if len(y)==0:
            break
        req_preff.append(y)
    generator(req_preff)




generate_password()



# TODP: def password_dictionary():






