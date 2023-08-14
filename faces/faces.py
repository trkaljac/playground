# ":)" == "🙂" , ":( "== "🙁"

def convert(input_str):
    converted_str = input_str.replace(":)", "🙂")
    converted_str = input_str.replace(":(", "🙁")
    return converted_str

user_input = input()
converted_input = convert(user_input)
print(converted_input)



