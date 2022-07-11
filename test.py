import os
prev =input("give your susy name: ")
for i in range(10000):
    print(prev)
    cmd = "echo {0}>>password.txt".format(prev)
    os.system(cmd)