question = input("camelCase: ")
snake_case = ""
for character in question:
    if character.isupper():
        snake_case += "_" + character.lower()
    else:
        snake_case += character


print(snake_case)