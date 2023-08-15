
greeting = input("Greeting: ")

if greeting.lower().startswith("Hello"):
    print("$0")
elif greeting.startswith("h"):
    print("$20")
else:
    print("$100")

