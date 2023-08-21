#max 6 min 2
#number on the end only
#first number cant be 0
#no ",","."," ",":"
#all caps
invalid_characters = set(',. :')
def is_valid(s):
    ...
    if len(s) < 2 or len(s) > 6:
        return False
    if not s [-1].isdigit():
        return False
    if s[0] == "0":
        return False

    if any(char in invalid_characters for char in s):
        return False
    if not s.isupper():
        return False
    else:
        return True


def main():
    plate = input("Plate: ").isupper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")




main()