answer = input("What is the Answer to the Great Question of Life,the Universe,and Everything?").lower().replace(" ","")
if answer in [ 42,"42","forty-two","forty two"]:
    print("Yes")
else:
    print("No")