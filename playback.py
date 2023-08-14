def slow_down_text(text):
    return text.replace(' ', '...')

if __name__ == "__main__":
    user_input = input("Enter text: ")
    slowed_down_text = slow_down_text(user_input)
    print(slowed_down_text)