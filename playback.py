def slow_down(text):
    return text.replace(' ', '...')

user_input = input()
slow_down = slow_down(user_input)
print(slow_down)