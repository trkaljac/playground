question = input("camelCase: ")
snake_case = ""
for character in question:
    if caracter.isupper():
        snake_case +="_"+character.lower()
    else:

print(question)
print(snake_case)