# ":)" == "🙂" , ":( "== "🙁" can do more emojis with .raplace()





def convert(input_str):
    converted_str = input_str.replace(":)", "🙂").replace(":(", "🙁")
    return converted_str

user_input = input()
converted_input = convert(user_input)
print(converted_input)



