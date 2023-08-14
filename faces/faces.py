# ":)" == "🙂" , ":( "== "🙁"

def convert(input_str):
    input_str = input_str.replace(":)", "🙂").replace(":(", "🙁")
    return input_str
convert(input_str)


input = input("Enter a string: ")
text = convert(input)
print(text)