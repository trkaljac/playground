
twttr = input("Input: ")

res = [char for char in twttr if char not in "aeiouAEIOU"]
print("Output: " + "".join(res))

