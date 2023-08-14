def slow_down(text):
    return text.replace(' ', '...')

if name == "main":
    user_input = input()
    slowed_down = slow_down(user_input)
    print(slowed_down)