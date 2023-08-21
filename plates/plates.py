#max 6 min 2
#number on the end only
#first number cant be 0
#no ",","."," ",":"
#all caps
def main():
    plate = input("Plate: ")
    if is_valid(plate):

        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    ...
    if len(s) <2 or len(s) >6:
        return False


main()